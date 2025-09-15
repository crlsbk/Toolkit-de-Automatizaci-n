import argparse
import sys
from src.scraper import parser_scraper
from src.fileOrganizer import organizarArchivos
from src.pdfs import parser_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Toolkit de Automatización: organiza archivos, maneja PDFs y busca trabajos con scraper"
    )

    subparsers = parser.add_subparsers(
        dest="tool", required=True, help="Elige una herramienta"
    )

    archivos_parser = subparsers.add_parser(
        "organizar",
        help="Organiza archivos moviendolos a carpetas dependiendo de su extensión",
    )
    archivos_parser.add_argument(
        "-p", "--path", required=True, help="Ruta de la carpeta que se desea organizar"
    )
    archivos_parser.set_defaults(func=lambda args: organizarArchivos(args.path))

    parser_pdf_tool = subparsers.add_parser(
        "pdf", help="Herramientas para manipular archivos PDF."
    )
    parser_pdf(parser_pdf_tool)

    parser_scrap = subparsers.add_parser(
        "scraper", help="Scraper de OCC para buscar vacantes"
    )
    parser_scraper(parser_scrap)

    args = parser.parse_args()

    try:
        if args.tool == "scraper":
            args.func(**vars(args))
        else:
            args.func(args)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
