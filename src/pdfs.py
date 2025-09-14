from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import argparse
import sys
from pathlib import Path

def split_pdf(ruta_input: str, ruta_output: str):
    input_path = Path(ruta_input)
    output_path = Path(ruta_output)

    if not input_path.is_file():
        print(f"Error: El archivo '{ruta_input}' no existe.", file=sys.stderr)
        return
    
    if not output_path.is_dir():
        print(f"Error: La ruta '{ruta_output}' no existe.", file=sys.stderr)

    try:
        leer = PdfReader(input_path)
        paginas = len(leer.pages)
        
        while True:
            try:
                limite_str = input(f"El PDF tiene {paginas} páginas. Hasta qué página deseas guardar? ")
                limite = int(limite_str)
                if 0 < limite <= paginas:
                    break
                else:
                    print(f"Por favor, ingresa un número entre 1 y {paginas}.", file=sys.stderr)
            except ValueError:
                print("Ingresa un número entero.", file=sys.stderr)
                continue

        writer = PdfWriter()
        for i in range(limite):
            writer.add_page(leer.pages[i])
        
        nombre_output = output_path / f"{input_path.stem}_hasta_pagina_{limite}.pdf"
        
        with open(nombre_output, "wb") as f:
            writer.write(f)
            
        print("Se ha creado el archivo exitosamente")

    except Exception as e:
        print(f"Ocurrió un error: {e}", file=sys.stderr)
        return
    
def merge_pdf(ruta_pdf1: str, ruta_pdf2: str, ruta_output: str):
    pdf1 = Path(ruta_pdf1)
    pdf2 = Path(ruta_pdf2)
    output = Path(ruta_output)
    merger = PdfMerger()
    
    if not pdf1.is_file():
        print(f"Error: El archivo '{ruta_pdf1}' no existe.", file=sys.stderr)
        return
        
    if not pdf2.is_file():
        print(f"Error: El archivo '{ruta_pdf2}' no existe.", file=sys.stderr)
        return

    if not output.is_dir():
        print(f"Error: El directorio'{ruta_output}' no existe.", file=sys.stderr)
        return
    
    merger.append(pdf1)
    merger.append(pdf2)
    try:
        with open(output / f"{pdf1.stem}_{pdf2.stem}_fusionados.pdf", "wb") as output_stream:
            merger.write(output_stream)
        print("Se ha creado el nuevo archivo exitosamente")
    except Exception as e:
        print(f"Ocurrió un error:{e}", file=sys.stderr)
        return
    finally:
        merger.close()        

def cambiar_nombre(ruta_archivo: str, nuevo_nombre: str):
    ruta = Path(ruta_archivo)
    ruta_nueva = ruta.parent / nuevo_nombre
    
    if not ruta.is_file():
        print(f"Error: El archivo '{ruta_archivo}' no existe.", file=sys.stderr)
        return
    
    if ruta_nueva.exists():
        print(f"Error: Ya existe un archivo llamado '{nuevo_nombre}'.")
        return
    
    try:
        ruta.rename(ruta_nueva)
        print(f"Se cambio el nombre de {ruta.name} a {nuevo_nombre}")
    except Exception as e:
        print(f"Ocurrió un error:{e}", file=sys.stderr)
        return