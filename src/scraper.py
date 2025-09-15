import requests
from pathlib import Path
import csv
from bs4 import BeautifulSoup
import sys

def obtener_trabajos(puesto: str):
    puesto_url = puesto.replace(' ', '-')
    url = f"https://www.occ.com.mx/empleos/de-{puesto_url}"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/128.0.0.0 Safari/537.36",
        "Accept-Language": "es-MX,es;q=0.9,en;q=0.8",
        "Referer": "https://www.google.com/",
    }
    respuesta = requests.get(url, headers=headers)
    
    if respuesta.status_code != 200:
        print(f"No se pudo obtener la página. Código: {respuesta.status_code}", file=sys.stderr)
        return [] 
    
    sopahermosa = BeautifulSoup(respuesta.text, "html.parser")
    trabajos = sopahermosa.find_all("div", class_="flex flex-col relative z-1 m-0 p-0 box-border mx-auto")
    
    if not trabajos:
        print("No se encontraron trabajos con el puesto indicado", file=sys.stderr)
        return []
    
    data = []
    for trabajo in trabajos:
        tag_titulo = trabajo.find("h2", class_="text-grey-900 text-lg break-words inline-block mt-0 mr-2 mb-0 ellipsis")
        titulo = tag_titulo.text.strip() if tag_titulo else "N/A"
        
        tag_compania = trabajo.find("a", class_="text-grey-900 hover:text-grey-900 focus:text-grey-900 active:text-grey-900 no-underline")
        compania = tag_compania.text.strip() if tag_compania else "N/A"
        
        tag_ubi = trabajo.find("p", class_="text-grey-900 m-0 text-sm font-light hover:text-decoration-none")
        ubi = tag_ubi.text.strip() if tag_ubi else "N/A"
        
        tag_fecha = trabajo.find("span", class_="mr-2 text-sm font-light")
        fecha = tag_fecha.text.strip() if tag_fecha else "N/A"
        
        link_relativo = trabajo.find('a')['href'] if trabajo.find('a') else ""
        link_url = f"https://www.occ.com.mx{link_relativo}" if link_relativo else "N/A"
        
        data.append({
            "Título": titulo,
            "Empresa": compania,
            "Ubicación": ubi,
            "Fecha": fecha,
            "URL": link_url
        })
        
    print(f"Se encontraron {len(data)} trabajos")
    return data
      
def ejecutar_scraper(puesto: str, ver: bool, guardar: str, **kwargs):
    if not ver and not guardar:
        print("Error: Debes elegir una acción: --ver o --guardar RUTA", file=sys.stderr)
        return

    datos = obtener_trabajos(puesto)
    if not datos:
        return

    if ver:
        for i, trabajo in enumerate(datos, 1):
            print(f"\n--- TRABAJO #{i} ---")
            print(f"Título: {trabajo['Título']}")
            print(f"Empresa: {trabajo['Empresa']}")
            print(f"Ubicación: {trabajo['Ubicación']}")
            print(f"Fecha: {trabajo['Fecha']}")
            print(f"URL: {trabajo['URL']}")

    if guardar:
        ruta_archivo = guardar
        rutaP = Path(ruta_archivo)
        
        if not rutaP.is_dir():
            print("La ruta ingresada no existe")
            return

        puesto_archivo = puesto.replace(' ', '_')
        ruta_final = rutaP / f"vacantes_{puesto_archivo}.csv"
        try:
            with open(ruta_final, 'w', newline='', encoding='utf-8') as f:
                fieldnames = datos[0].keys()
                escribe = csv.DictWriter(f, fieldnames=fieldnames)
                escribe.writeheader()
                escribe.writerows(datos)
            print(f"Datos guardados exitosamente como '{ruta_final}'")
        except IOError as e:
            print(f"Ocurrio un error: {e}", file=sys.stderr)

    
def parser_scraper(parser):
    parser.add_argument("-p", "--puesto", required=True, help="El puesto de trabajo a buscar")
    parser.add_argument("-v", "--ver", action="store_true", help="Muestra los resultados en la terminal")
    parser.add_argument("-g", "--guardar", nargs='?', const='.', default=None, help="Guarda los resultados en un archivo CSV. Si se usa sin ruta, guarda en el directorio actual. Opcionalmente especifica un DIRECTORIO.")
    
    parser.set_defaults(func=ejecutar_scraper)
