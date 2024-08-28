from reportlab.lib import colors


class Constants:
    __version__ = 1.0
    __enlace_cdir__ = ("https://www.rohde-schwarz.com/es/soluciones/networks-and-cybersecurity/ciberseguridad/landing"
                       "-pages/calculadora-de-cidr_256249.html")

    __common_open_ports__ = {21, 22, 23, 25, 53, 69, 80, 88, 109, 110,
                             123, 137, 138, 139, 143, 156, 161, 389, 443,
                             445, 500, 546, 547, 587, 660, 995, 993, 2086,
                             2087, 2082, 2083, 3306, 8443, 10000}

    __colorama_to_reportlab__ = {

        '\033[30m': colors.black,
        '\033[31m': colors.red,
        '\033[32m': colors.green,
        '\033[33m': colors.yellow,
        '\033[34m': colors.blue,
        '\033[35m': colors.magenta,
        '\033[36m': colors.cyan,
        '\033[37m': colors.white,
        '\033[90m': colors.grey,
        '\033[91m': colors.red,
        '\033[92m': colors.green,
        '\033[93m': colors.yellow,
        '\033[94m': colors.blue,
        '\033[95m': colors.magenta,
        '\033[96m': colors.cyan,
        '\033[97m': colors.white,

    }

