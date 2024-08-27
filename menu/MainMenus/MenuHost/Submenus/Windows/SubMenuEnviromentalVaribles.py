from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuEnviromentalVariables(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def enviromental_variables(self):
        self.host.enviromental_variables.get_enviromental_variables()
        if self.host.enviromental_variables.enviromental_variables:
            print(f"{Fore.MAGENTA}Varibales de entorno{Fore.RESET}")
            print(self.host.enviromental_variables.enviromental_variables)

    def password_in_reg(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.enviromental_variables.get_password_in_reg()
        loader.stop()
        if self.host.enviromental_variables.passwords:
            print(f"{Fore.MAGENTA}Contraseñas en los registros{Fore.RESET}")
            print(self.host.enviromental_variables.passwords)