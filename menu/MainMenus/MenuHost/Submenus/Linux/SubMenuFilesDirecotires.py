from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuFilesDirectories(MenuHost):

    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_misconfiguration_files_suid(self):
        if self.host.file_directories.misconfiguration_files_suid is None:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_misconfiguration_files_suid()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos con configuración incorrecta{Fore.RESET}")
        print(self.host.file_directories.misconfiguration_files_suid)

    def get_writable_for_current_user(self):
        if self.host.file_directories.writable_for_current_user is None:
            self.host.file_directories.get_writable_files_for_current_user()
        print(f"{Fore.MAGENTA}Archivos con escritura para el usuario actual{Fore.RESET}")
        print(self.host.file_directories.writable_for_current_user)

    def get_global_files_without_proc(self):
        if self.host.file_directories.global_files_without_proc is None:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_global_files_without_proc()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos globales sin incluir archivos virtuales{Fore.RESET}")
        print(self.host.file_directories.global_files_without_proc)

    def get_logs_with_passwords(self):
        if self.host.file_directories.logs_with_passwords is None:
            self.host.file_directories.get_logs_with_passwords()
        print(f"{Fore.MAGENTA}Logs con contraseña{Fore.RESET}")
        print(self.host.file_directories.logs_with_passwords)

    def get_configurations_files_with_password(self):
        if self.host.file_directories.configurations_files_with_password is None:
            self.host.file_directories.get_configurations_files_with_password()
        print(f"{Fore.MAGENTA}Archivos de configuración con contraseña{Fore.RESET}")
        print(self.host.file_directories.configurations_files_with_password)

    def get_sticky_bits(self):
        if self.host.file_directories.sticky_bits is None:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_sticky_bits()
            loader.stop()
        print(f"{Fore.MAGENTA}Sticky bits{Fore.RESET}")
        print(self.host.file_directories.sticky_bits)

    def get_writable_folders(self):
        if self.host.file_directories.writable_folders is None:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_writable_folders()
            loader.stop()
        print(f"{Fore.MAGENTA}Directorios con permiso de escritura{Fore.RESET}")
        print(self.host.file_directories.writable_folders)

    def get_writable_files_for_current_user(self):
        if self.host.file_directories.writable_files_for_current_user is None:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.file_directories.get_writable_files_for_current_user()
            loader.stop()
        print(f"{Fore.MAGENTA}Directorios con permiso de escritura para el usuario actual{Fore.RESET}")
        print(self.host.file_directories.writable_files_for_current_user)

