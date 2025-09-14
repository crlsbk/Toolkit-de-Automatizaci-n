import os
import shutil

path = input("Ingresa la ruta de la carpeta a organizar:")

if not os.path.exists(path):
    print("No existe el folder")
    exit()
    
tipos_archivo = {
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".xlsx", ".xls", ".pptx", ".ppt"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".tif", ".ico"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".wmv", ".flv", ".webm", ".m4v"],
    "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Archivos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Codigo": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css", ".php", ".rb", ".go"],
    "Ejecutables": [".exe", ".msi", ".bat", ".sh", ".app", ".dmg"],
    "Data": [".csv", ".json", ".xml", ".yaml", ".yml", ".sql", ".db"]
}

archivos = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in archivos:
    ext = os.path.splitext(file)[1].lower()
    organizado = False
    for categoria, extension in tipos_archivo.items():
        if ext in extension:
            folder = os.path.join(path, categoria)
            if not os.path.isdir(folder):
                os.mkdir(folder)
            shutil.move(os.path.join(path,file), os.path.join(folder, file))
            print (f"Se movio {file} correctamente")
            organizado = True
            break            
    if not organizado:
        if not os.path.isdir(os.path.join(path, "Otros")):
            os.mkdir(os.path.join(path, "Otros"))
        shutil.move(os.path.join(path, file), os.path.join(path, "Otros"))
        print(f"Se movio {file} a Otros")
        
print ("Completado")
