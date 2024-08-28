from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command
from myhostinformation.HostInfo.HostRepository import HostRepository
from myhostinformation.HostInfo.Types.Linux.Components.EnviromentalVaribles import EnviromentalVaribles
from myhostinformation.HostInfo.Types.Linux.Components.FilesDirectories import FilesDirectories
from myhostinformation.HostInfo.Types.Linux.Components.NetWork import NetWork
from myhostinformation.HostInfo.Types.Linux.Components.PossibleDenfeses import PossibleDefenses
from myhostinformation.HostInfo.Types.Linux.Components.Programs import Programs
from myhostinformation.HostInfo.Types.Linux.Components.Users import Users


class Linux(HostRepository):
    def __init__(self):
        super().__init__()
        self.users = Users()
        self.network = NetWork()
        self.file_directories = FilesDirectories()
        self.programs = Programs()
        self.possible_defenses = PossibleDefenses()
        self.enviromental_variables = EnviromentalVaribles()
        self.basic_information = self.get_basic_information()

    @staticmethod
    def get_basic_information():
        information = run_command("cat /etc/os-release 2>/dev/null")
        return information

    def __str__(self):
        return (
                Fore.MAGENTA + "Información básica:\n\n" + Fore.RESET + self.basic_information + "\n" +
                Fore.MAGENTA + "Variables de entorno:\n\n" + Fore.RESET + self.enviromental_variables.__str__() + "\n" +
                Fore.MAGENTA + "Usuarios:\n\n" + Fore.RESET + self.users.__str__() + "\n" +
                Fore.MAGENTA + "Network:\n\n" + Fore.RESET + self.network.__str__() + "\n" +
                Fore.MAGENTA + "Directorios y ficheros:\n\n" + Fore.RESET + self.file_directories.__str__() + "\n" +
                Fore.MAGENTA + "Programas:\n\n" + Fore.RESET + self.programs.useful_programs + "\n"+
                Fore.MAGENTA + "Programas:\n\n" + Fore.RESET + self.possible_defenses.__str__() + "\n"
        )

