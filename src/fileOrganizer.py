import shutil
from pathlib import Path
import sys

def organizarArchivos(path_str: str):
    path = Path(path_str)

    if not path.is_dir():
        print(f"Error: El directorio {path_str} no existe")
        return
        
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

    archivos = [f for f in path.iterdir() if f.is_file()]

    for file in archivos:
        try:
            ext = file.suffix.lower()
            organizado = False
            for categoria, extension in tipos_archivo.items():
                if ext in extension:
                    folder = path / categoria
                    if not folder.is_dir():
                        folder.mkdir()
                    shutil.move(file, folder / file.name)
                    print(f"Se movio {file.name} correctamente")
                    organizado = True
                    break            
            if not organizado:
                otros_folder = path / "Otros"
                if not otros_folder.is_dir():
                    otros_folder.mkdir()
                shutil.move(file, otros_folder / file.name)
                print(f"Se movio {file.name} a Otros")
        except (OSError, shutil.Error) as e:
            print(f"Error al mover {file.name}: {e}", file=sys.stderr)
    
    print("Archivos organizados correctamente")
