from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command
from myhostinformation.HostInfo.HostRepository import HostRepository
from myhostinformation.HostInfo.Types.Windows.Components.EnviromentalVaribles import EnviromentalVaribles
from myhostinformation.HostInfo.Types.Windows.Components.FilesDirectories import FilesDirectories
from myhostinformation.HostInfo.Types.Windows.Components.NetWork import NetWork
from myhostinformation.HostInfo.Types.Windows.Components.Programs import Programs
from myhostinformation.HostInfo.Types.Windows.Components.Users import Users


class Windows(HostRepository):
    def __init__(self):
        super().__init__()
        self.users = Users()
        self.network = NetWork()
        self.file_directories = FilesDirectories()
        self.programs = Programs()
        self.enviromental_variables = EnviromentalVaribles()
        self.basic_information = self.get_basic_information()

    @staticmethod
    def get_basic_information():
        basic_info = run_powershell_command("Start-Process 'systeminfo' -NoNewWindow -Wait")
        return basic_info
