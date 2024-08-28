from colorama import Fore
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

from LibModule.constants import Constants


class MyDocTemplate(SimpleDocTemplate):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def afterPage(self):
        header_footer(self.canv, self)


def header_footer(canvas, doc):
    canvas.drawImage("logo.png", 0.5 * inch, 10 * inch, width=2 * inch,
                     height=1 * inch)
    canvas.setFont('Helvetica', 8)  # Usa la fuente 'HelveticaSmall' y el tamaño de 8 puntos
    canvas.drawString(7.5 * inch, 0.5 * inch, f"Page {canvas.getPageNumber()}")


def convert_colorama_to_reportlab(text):
    # Escapa caracteres especiales
    def escape_html(text):
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#039;"))

    # Convierte códigos ANSI de colorama a HTML para reportlab
    text = escape_html(text)  # Primero escapa caracteres especiales

    # Inicializa el estado del color
    current_color = None

    # Reemplaza cada código de color
    for colorama_code, reportlab_color in Constants().__colorama_to_reportlab__.items():
        if colorama_code == Fore.RESET:
            # Cierra cualquier etiqueta de color abierta
            text = text + "</font>"
        else:
            # Reemplaza el código de color por la etiqueta HTML
            text = text.replace(colorama_code, f"<font color='{reportlab_color}'>")

    # Reemplaza el código de reseteo de color con la etiqueta de cierre </font>
    text = text.replace(Fore.RESET, "</font>")

    # Reemplaza los saltos de línea con <br />
    text = text.replace("\n", "<br />")

    return text
