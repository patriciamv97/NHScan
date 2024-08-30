import os

from colorama import Fore
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

from LibModule.Functions import get_downloads_folder
from LibModule.Loader import Loader
from Report.Template import MyDocTemplate, convert_colorama_to_reportlab


class PDFGenerator:

    def __init__(self):
        self.file_name = None
        self.file_path = None
        self.data = None

    def set_data(self, data):
        self.data = data

    def set_file_info(self, file_name):
        downloads_folder = get_downloads_folder()
        self.file_name = file_name
        self.file_path = os.path.join(downloads_folder, file_name)

    def create_pdf(self):
        loader = Loader("Loading...", "", 0.05).start()
        try:
            if not self.file_path:
                raise ValueError("La ruta del archivo no ha sido establecida. Llama a set_file_info() primero.")
            doc = MyDocTemplate(self.file_path, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []
            for obj in self.data:
                formatted_text = convert_colorama_to_reportlab(obj.__str__())
                p = Paragraph(formatted_text, style=styles['Normal'])
                story.append(p)
            doc.build(story)
            loader.stop()
            print("[!]Informe descargado. Revisa la carpeta de descargas.")
        except PermissionError:
            loader.stop()
            print(Fore.YELLOW+"[!]Comprueba que no tengas el archivo abierto."+Fore.RESET)
            pass
        except Exception as e:
            loader.stop()
            print(Fore.RED+"[X]No se ha podido generar el informe, algo ha ido mal."+Fore.RESET+"\n")
            print(e.args)
            pass
