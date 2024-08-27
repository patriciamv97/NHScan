from colorama import Fore

from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuFilesDirectories(MenuHost):

    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_misconfiguration_files_suid(self):
        self.host.file_directories.get_misconfiguration_files_suid()
        if self.host.file_directories.misconfiguration_files_suid:
            print(f"{Fore.MAGENTA}Archivos con configuración incorrecta{Fore.RESET}")
            print(self.host.file_directories.misconfiguration_files_suid)

    def get_writable_for_current_user(self):
        self.host.file_directories.get_writable_for_current_user()
        if self.host.file_directories.writable_for_current_user:
            print(f"{Fore.MAGENTA}Archivos con escritura para el usuario actual{Fore.RESET}")
            print(self.host.file_directories.writable_for_current_user)

    def get_global_files_without_proc(self):
        self.host.file_directories.get_global_files_without_proc()
        if self.host.file_directories.global_files_without_proc:
            print(f"{Fore.MAGENTA}Archivos globales sin incluir archivos virtuales{Fore.RESET}")
            print(self.host.file_directories.global_files_without_proc)

    def get_logs_with_passwords(self):
        self.host.file_directories.get_logs_with_passwords()
        if self.host.file_directories.logs_with_passwords:
            print(f"{Fore.MAGENTA}Logs con contraseña{Fore.RESET}")
            print(self.host.file_directories.logs_with_passwords)

    def get_configurations_files_with_password(self):
        self.host.file_directories.get_configurations_files_with_password()
        if self.host.file_directories.configurations_files_with_password:
            print(f"{Fore.MAGENTA}Archivos de configuración con contraseña{Fore.RESET}")
            print(self.host.file_directories.configurations_files_with_password)

    def get_sticky_bits(self):
        self.host.file_directories.sticky_bits()
        if self.host.file_directories.sticky_bits:
            print(f"{Fore.MAGENTA}Sticky bits{Fore.RESET}")
            print(self.host.file_directories.sticky_bits)

    def get_writable_folders(self):
        self.host.file_directories.get_writable_folders()
        if self.host.file_directories.writable_folders:
            print(f"{Fore.MAGENTA}Directorios con permiso de escritura{Fore.RESET}")
            print(self.host.file_directories.writable_folders)

    def get_writable_files_for_current_user(self):
        self.host.file_directories.get_writable_files_for_current_user()
        if self.host.file_directories.writable_files_for_current_user:
            print(f"{Fore.MAGENTA}Directorios con permiso de escritura para el usuario actual{Fore.RESET}")
            print(self.host.file_directories.writable_files_for_current_user)

