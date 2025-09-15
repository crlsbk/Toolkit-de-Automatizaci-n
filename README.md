# **Toolkit de Automatización**

Un conjunto de herramientas de línea de comandos diseñada para automatizar tareas comunes del día a día, como la organización de archivos, la manipulación de documentos PDF y la búsqueda de ofertas de empleo.

## **Funcionalidades**

- **Organizador de Archivos:** Analiza una carpeta y mueve los archivos a subcarpetas categorizadas por su tipo de extensión (Documentos, Imágenes, Video, etc.).
- **Herramientas para PDF:** Permite fusionar dos archivos PDF en uno, dividir un archivo PDF hasta una página específica y renombrar archivos.
- **Scraper de Empleos:** Busca ofertas de trabajo en OCC.com.mx para un puesto específico, mostrando los resultados en la terminal o guardándolos en un archivo CSV.

---

## **Instalación**

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/crlsbk/Toolkit-de-Automatizacion
    cd Toolkit-de-Automatizacion
    ```

2.  **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```

> Recomiendo crear un entorno virtual para evitar conflictos con paquetes.

## **Uso**

Todas las herramientas se ejecutan desde el archivo principal `main.py`, tienes que especificar la herramienta y sus opciones.

### 1. Organizar Archivos (`organizar`)

Mueve los archivos de un directorio a carpetas según su tipo.

**Comando:**

```bash
python3 main.py organizar -p <ruta_del_directorio>
```

**Ejemplo:**

```bash
python3 main.py organizar -p "/home/usuario/Descargas"
```

### 2. Herramientas de PDF (`pdf`)

Permite realizar varias acciones en archivos PDF.

#### Fusionar dos PDFs (`fusionar`)

**Comando:**

```bash
python3 main.py pdf fusionar -i <pdf1> <pdf2> -o <directorio_salida>
```

- **`-i`, `--input`** es requerido,
  **`-o`, `--output`**: (Opcional) Directorio donde se guardará el PDF resultante. Por defecto, es el directorio actual.

**Ejemplo:**

```bash
python3 main.py pdf fusionar -i reporte1.pdf reporte2.pdf -o ./documentos
```

#### Dividir un PDF (`dividir`)

Crea un nuevo PDF con las páginas desde el inicio hasta un número de página especificado.
**Comando:**

```bash
python3 main.py pdf dividir -i <archivo.pdf> -o <directorio_salida>
```

- **`-i`, `--input`**: (Requerido) El archivo PDF que se va a dividir.
- **`-o`, `--output`**: (Opcional) Directorio donde se guardará el nuevo PDF. Por defecto, es el directorio actual.

**Ejemplo:**

```bash
python3 main.py pdf dividir -i mi_libro.pdf
```

#### Renombrar un archivo (`renombrar`)

**Comando:**

```bash
python3 main.py pdf renombrar -i <archivo_actual> -n <nuevo_nombre>
```

- **`-i`, `--input`**: (Requerido) El archivo que se va a renombrar.
- **`-n`, `--nombre`**: (Requerido) El nuevo nombre para el archivo.

**Ejemplo:**

```bash
python3 main.py pdf renombrar -i "documento (1).pdf" "documento_final.pdf"
```

### 3. Scraper de Empleos (`scraper`)

Busca vacantes en OCC.com.mx.

**Comando:**

```bash
python3 main.py scraper -p <puesto> [-v] [-g <directorio_salida>]
```

- **`-p`, `--puesto`**: (Requerido) El puesto de trabajo a buscar. Si contiene espacios, ponlo entre comillas.
- **`-v`, `--ver`**: (Opcional) Muestra los resultados directamente en la terminal.
- **`-g`, `--guardar`**: (Opcional) Guarda los resultados en un archivo CSV. Puedes especificar un directorio o usarlo sin argumentos para guardar en el directorio actual.

**Ejemplos:**

```bash
# Ver vacantes de "ingeniero de software" en la terminal
python3 main.py scraper -p "ingeniero de software" -v

# Guardar vacantes de "analista de datos" en el directorio actual
python3 main.py scraper -p "analista de datos" -g

# Guardar vacantes en un directorio específico
python3 main.py scraper -p "diseñador ux" -g ./resultados/
```
