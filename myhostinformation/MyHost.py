import platform

from colorama import Fore


class MyHost:
    def __init__(self):
        self.ip = None
        self.machine = platform.uname().machine
        self.release = platform.release()
        self.processor = platform.processor()
        self.operative_system = platform.uname().system
        self.node = platform.node()
        # interface

    def __str__(self):
        return (Fore.MAGENTA + "Nombre de la maquina : " + Fore.RESET + self.node + "\n" +
                Fore.MAGENTA + "Sistema operativo : " + Fore.RESET + self.operative_system + "\n" +
                Fore.MAGENTA + "Arquitectura : " + Fore.RESET + self.machine + "\n" +
                Fore.MAGENTA + "Version : " + Fore.RESET + self.release + "\n" +
                Fore.MAGENTA + "Procesador : " + Fore.RESET + self.processor)
