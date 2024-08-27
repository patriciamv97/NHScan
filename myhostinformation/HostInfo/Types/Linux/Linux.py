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
