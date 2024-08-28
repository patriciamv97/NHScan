import os
import platform


def get_downloads_folder():
    if platform.system() == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif platform.system() == "Linux":
        return os.path.join(os.path.expanduser("~"), "Descargas")
    else:
        raise NotImplementedError("El sistema operativo no es compatible")