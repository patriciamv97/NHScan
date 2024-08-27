from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuUser(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def gpo_user(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.users.get_gpo_user()
        loader.stop()
        if self.host.users.gpo_user:
            print(f"{Fore.MAGENTA}Directiva de usuario:{Fore.RESET}")
            print(self.host.users.gpo_user)

    def gpo_computer(self):
        gpo_computer = self.host.users.get_gpo_computer()
        if gpo_computer:
            print(f"{Fore.MAGENTA}Directiva de equipo:{Fore.RESET}")
            print(gpo_computer)

    def get_current_user(self):
        self.host.users.get_current_user()
        if self.host.users.current_user:
            print(f"{Fore.MAGENTA}Usuario actual:{Fore.RESET}")
            print(self.host.users.current_user)

    def get_powershell_history(self):
        self.host.users.get_powershell_history()
        if self.host.users.powershell_history:
            print(f"{Fore.MAGENTA}Historial de PowerShell:{Fore.RESET}")
            for line in self.host.users.powershell_history:
                print(line.strip())

    def get_user_login_history(self):
        self.host.users.get_user_login_history()
        if self.host.users.user_login_history:
            print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
            print(self.host.users.user_login_history)

    def get_remote_desktop_user(self):
        self.host.users.get_remote_desktop_user()
        if self.host.users.remote_desktop_users:
            print(f"{Fore.MAGENTA}Usuarios de escritorio remoto:{Fore.RESET}")
            print(self.host.users.remote_desktop_users)
        else:
            print(f"{Fore.YELLOW}No se encontraron usuarios asociados a este grupo.")

    def get_user_directory(self):
        self.host.users.get_user_directory()
        if self.host.users.user_directory:
            print(f"{Fore.MAGENTA}Directorios:{Fore.RESET}")
            print(self.host.users.user_directory)

    def get_logged_in_user(self):
        self.host.users.get_logged_in_user()
        if self.host.users.logged_in_user:
            print(f"{Fore.MAGENTA}Usuarios con sesión:{Fore.RESET}")
            print(self.host.users.logged_in_user)

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

    def get_administrators(self):
        self.host.users.get_administrators()
        if self.host.users.administrators:
            print(f"{Fore.MAGENTA}Administradores:{Fore.RESET}")
            print(self.host.users.administrators)

    def get_currently_stored_creendentials(self):
        self.host.users.get_currently_stored_creendentials()
        if self.host.users.currently_stored_history:
            print(f"{Fore.MAGENTA}Historial:{Fore.RESET}")
            print(self.host.users.currently_stored_history)
