from colorama import Fore


class HostRepository:
    def __init__(self):
        self.basic_information = None
        self.enviromental_variables = None
        self.users = None
        self.network = None
        self.file_directories = None
        self.programs = None
        self.possible_defenses = None

    def __str__(self):
        return (
                Fore.MAGENTA + "Información básica:\n\n" + Fore.RESET + self.basic_information + "\n\n" +
                Fore.MAGENTA + "Variables de entorno:\n\n" + Fore.RESET + self.enviromental_variables.__str__() + "\n\n" +
                Fore.MAGENTA + "Usuarios:\n\n" + Fore.RESET + self.users.__str__() + "\n\n" +
                Fore.MAGENTA + "Network:\n\n" + Fore.RESET + self.network.__str__() + "\n\n" +
                Fore.MAGENTA + "Directorios y ficheros:\n\n" + Fore.RESET + self.file_directories.__str__() + "\n\n" +
                Fore.MAGENTA + "Programas:\n\n" + Fore.RESET + self.programs.useful_programs + "\n\n")
