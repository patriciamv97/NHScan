from colorama import Fore

from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuFilesDirectories(MenuHost):

    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_unattended_files(self):
        self.host.file_directories.get_unattended_files()
        if self.host.file_directories.unattended_files:
            print(f"{Fore.MAGENTA}Archivos desatendidos{Fore.RESET}")
            print(self.host.file_directories.unattended_files)

    def get_extension_files_xml(self):
        self.host.file_directories.get_extension_files_xml()
        if self.host.file_directories.xml_files:
            print(f"{Fore.MAGENTA}Archivos con extensión xml{Fore.RESET}")
            print(self.host.file_directories.xml_files)

    def get_extenision_files_ini(self):
        self.host.file_directories.get_extenision_files_ini()
        if self.host.file_directories.init_files:
            print(f"{Fore.MAGENTA}Archivos con extensión ini{Fore.RESET}")
            print(self.host.file_directories.init_files)

    def get_extension_files_conf(self):
        self.host.file_directories.get_extension_files_conf()
        if self.host.file_directories.config_files:
            print(f"{Fore.MAGENTA}Archivos de configuración{Fore.RESET}")
            print(self.host.file_directories.config_files)

    def get_logs(self):
        self.host.file_directories.get_logs()
        if self.host.file_directories.logs:
            print(f"{Fore.MAGENTA}Logs{Fore.RESET}")
            print(self.host.file_directories.logs)

    def get_interesting_files(self):
        self.host.file_directories.get_interesting_files()
        if self.host.file_directories.interesting_files:
            print(f"{Fore.MAGENTA}Archivos con contraseñas{Fore.RESET}")
            print(self.host.file_directories.interesting_files)

    def get_passwords(self):
        self.host.file_directories.find_password()
        if self.host.file_directories.get_passwords:
            print(f"{Fore.MAGENTA}Contraseñas{Fore.RESET}")
            print(self.host.file_directories.passwords)

    def get_hidden_files_in_root(self):
        self.host.file_directories.get_hidden_files_in_root()
        if self.host.file_directories.hidden_files_in_root:
            print(f"{Fore.MAGENTA}Archivos ocultos en la raiz{Fore.RESET}")
            print(self.host.file_directories.hidden_files_in_root)

    def get_hidden_files_in_users(self):
        self.host.file_directories.get_hidden_files_in_users()
        if self.host.file_directories.hidden_files_in_users:
            print(f"{Fore.MAGENTA}Archivos de ocultos en Users{Fore.RESET}")
            print(self.host.file_directories.hidden_files_in_users)

    def get_hidden_files_in_user(self):
        self.host.file_directories.get_hidden_files_in_user()
        if self.host.file_directories.hidden_files_in_user:
            print(f"{Fore.MAGENTA}Archivos ocultos de el usuario actual{Fore.RESET}")
            print(self.host.file_directories.hidden_files_in_user)
