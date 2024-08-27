from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuUser(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_users_in_sudo(self):
        if not self.host.users.users_in_sudo:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.users.get_users_in_sudo()
            loader.stop()
        print(f"{Fore.MAGENTA}Usuarios con permiso de sudo:{Fore.RESET}")
        print(self.host.users.users_in_sudo)

    def get_users(self):
        if not self.host.users.users:
            self.host.users.get_users()
        print(f"{Fore.MAGENTA}Usuarios:{Fore.RESET}")
        print(self.host.users.users)

    def get_current_user(self):
        if not self.host.users.current_user:
            self.host.users.get_current_user()
        print(f"{Fore.MAGENTA}Usuario actual:{Fore.RESET}")
        print(self.host.users.current_user)

    def get_command_history(self):
        if not self.host.users.command_history:
            self.host.users.get_command_history()
        print(f"{Fore.MAGENTA}Historial de comandos:{Fore.RESET}")
        for line in self.host.command_history:
            print(line.strip())

    def get_user_history(self):
        if not self.host.users.user_history:
            self.host.users.get_user_history()
        print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
        print(self.host.users.user_history)

    def get_logged_in_user(self):
        if not self.host.users.logged_in_user:
            self.host.users.get_user_logged()
        print(f"{Fore.MAGENTA}Usuarios logeados:{Fore.RESET}")
        print(self.host.users.logged_in_user)

    def get_local_users(self):
        if not self.host.users.local_users:
            self.host.users.get_local_users()
        print(f"{Fore.MAGENTA}Usuarios Locales:{Fore.RESET}")
        print(self.host.users.local_users)

    def get_local_groups(self):
        if not self.host.users.local_groups:
            self.host.users.get_local_groups()
        print(f"{Fore.MAGENTA}Grupos Locales:{Fore.RESET}")
        print(self.host.users.local_groups)

    def get_user_directories(self):
        if not self.host.users.user_directories:
            self.host.users.get_user_directories()
        print(f"{Fore.MAGENTA}Directorios del usuario:{Fore.RESET}")
        print(self.host.users.user_directories)

    def get_root_directories(self):
        if not self.host.users.root_directories:
            self.host.users.get_root_directories()
        print(f"{Fore.MAGENTA}Directorios de root:{Fore.RESET}")
        print(self.host.users.root_directories)

    def get_current_user_groups_pemissions(self):
        if not self.host.users.current_user_groups_pemissions:
            self.host.users.get_current_user_groups_pemissions()
        print(f"{Fore.MAGENTA}Permisos y grupos del usuario actual:{Fore.RESET}")
        print(self.host.users.current_user_groups_pemissions)

    def get_users_connected(self):
        if not self.host.users.users_connected:
            self.host.users.get_users_connected()
        print(f"{Fore.MAGENTA}Usuarios conectados:{Fore.RESET}")
        print(self.host.users.users_connected)

    def get_administrators(self):
        if not self.host.users.adm_users:
            self.host.users.get_adm_users()
        print(f"{Fore.MAGENTA}Administradores:{Fore.RESET}")
        print(self.host.users.adm_users)

    def get_currently_stored_creendentials(self):
        if not self.host.users.currently_stored_history:
            self.host.users.get_currently_stored_creendentials()
        print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
        print(self.host.users.currently_stored_history)
