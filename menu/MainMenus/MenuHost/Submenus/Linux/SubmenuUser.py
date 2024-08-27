from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuUser(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_users_in_sudo(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.users.get_users_in_sudo()
        loader.stop()
        if self.host.users.users_in_sudo:
            print(f"{Fore.MAGENTA}Usuarios con permiso de sudo:{Fore.RESET}")
            print(self.host.users.users_in_sudo)

    def get_users(self):
        users = self.host.users.get_users()
        if users:
            print(f"{Fore.MAGENTA}Usuarios:{Fore.RESET}")
            print(self.host.users.user)

    def get_current_user(self):
        self.host.users.get_current_user()
        if self.host.users.current_user:
            print(f"{Fore.MAGENTA}Usuario actual:{Fore.RESET}")
            print(self.host.users.current_user)

    def get_command_history(self):
        self.host.users.get_command_history()
        if self.host.users.command_history:
            print(f"{Fore.MAGENTA}Historial de comandos:{Fore.RESET}")
            for line in self.host.users.command_history:
                print(line.strip())

    def get_user_history(self):
        self.host.users.get_user_history()
        if self.host.users.user_history:
            print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
            print(self.host.users.user_history)

    def get_logged_in_user(self):
        self.host.users.get_logged_in_user()
        if self.host.users.logged_in_user:
            print(f"{Fore.MAGENTA}Usuarios logeados:{Fore.RESET}")
            print(self.host.users.logged_in_user)

    def get_user_directory(self):
        self.host.users.get_user_directory()
        if self.host.users.user_directory:
            print(f"{Fore.MAGENTA}Directorios:{Fore.RESET}")
            print(self.host.users.user_directory)

    def get_local_users(self):
        self.host.users.get_local_users()
        if self.host.users.local_users:
            print(f"{Fore.MAGENTA}Usuarios Locales:{Fore.RESET}")
            print(self.host.users.local_users)

    def get_local_groups(self):
        self.host.users.get_local_groups()
        if self.host.users.local_groups:
            print(f"{Fore.MAGENTA}Grupos Locales:{Fore.RESET}")
            print(self.host.users.local_groups)

    def get_user_directories(self):
        self.host.users.get_user_directories()
        if self.host.users.user_directories:
            print(f"{Fore.MAGENTA}Directorios del usuario:{Fore.RESET}")
            print(self.host.users.user_directories)

    def get_root_directories(self):
        self.host.users.get_root_directories()
        if self.host.users.root_directories:
            print(f"{Fore.MAGENTA}Directorios de root:{Fore.RESET}")
            print(self.host.users.root_directories)

    def get_current_user_groups_pemissions(self):
        self.host.users.get_current_user_groups_pemissions()
        if self.host.users.current_user_groups_pemissions:
            print(f"{Fore.MAGENTA}Permisos y grupos del usuario actual:{Fore.RESET}")
            print(self.host.users.current_user_groups_pemissions)

    def get_users_connected(self):
        self.host.users.get_users_connected()
        if self.host.users.users_connected:
            print(f"{Fore.MAGENTA}Usuarios conectados:{Fore.RESET}")
            print(self.host.users.users_connected)

    def get_administrators(self):
        self.host.users.get_adm_users()
        if self.host.users.adm_users:
            print(f"{Fore.MAGENTA}Administradores:{Fore.RESET}")
            print(self.host.users.adm_users)

    def get_currently_stored_creendentials(self):
        self.host.users.get_currently_stored_creendentials()
        if self.host.users.currently_stored_history:
            print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
            print(self.host.users.currently_stored_history)
