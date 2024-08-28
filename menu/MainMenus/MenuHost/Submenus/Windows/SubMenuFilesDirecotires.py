from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuFilesDirectories(MenuHost):

    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_unattended_files(self):
        if not self.host.file_directories.unattended_files:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_unattended_files()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos desatendidos{Fore.RESET}")
        print(self.host.file_directories.unattended_files)

    def get_extension_files_xml(self):
        if not self.host.file_directories.xml_files:
            self.host.file_directories.get_extension_files_xml()
        print(f"{Fore.MAGENTA}Archivos con extensión xml{Fore.RESET}")
        print(self.host.file_directories.xml_files)

    def get_extenision_files_ini(self):
        if not self.host.file_directories.init_files:
            self.host.file_directories.get_extenision_files_ini()
        print(f"{Fore.MAGENTA}Archivos con extensión ini{Fore.RESET}")
        print(self.host.file_directories.init_files)

    def get_extension_files_conf(self):
        if not self.host.file_directories.config_files:
            self.host.file_directories.get_extension_files_conf()
        print(f"{Fore.MAGENTA}Archivos de configuración{Fore.RESET}")
        print(self.host.file_directories.config_files)

    def get_logs(self):
        if not self.host.file_directories.logs:
            self.host.file_directories.get_logs()
        print(f"{Fore.MAGENTA}Logs{Fore.RESET}")
        print(self.host.file_directories.logs)

    def get_interesting_files(self):
        if not self.host.file_directories.interesting_files:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_interesting_files()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos interesantes{Fore.RESET}")
        print(self.host.file_directories.interesting_files)

    def get_find_password(self):
        if not self.host.file_directories.passwords:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_find_password()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos con contraseñas{Fore.RESET}")
        print(self.host.file_directories.passwords)

    def get_hidden_files_in_root(self):
        if not self.host.file_directories.hidden_files_in_root:
            self.host.file_directories.get_hidden_files_in_root()
        print(f"{Fore.MAGENTA}Archivos ocultos en la raiz{Fore.RESET}")
        print(self.host.file_directories.hidden_files_in_root)

    def get_hidden_files_in_users(self):
        if not self.host.file_directories.hidden_files_in_users:
            self.host.file_directories.get_hidden_files_in_users()
        print(f"{Fore.MAGENTA}Archivos de ocultos en Users{Fore.RESET}")
        print(self.host.file_directories.hidden_files_in_users)

    def get_hidden_files_in_user(self):
        if not self.host.file_directories.hidden_files_in_user:
            self.host.file_directories.get_hidden_files_in_user()
        print(f"{Fore.MAGENTA}Archivos ocultos de el usuario actual{Fore.RESET}")
        print(self.host.file_directories.hidden_files_in_user)
