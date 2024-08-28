from colorama import Fore

from LibModule.Loader import Loader
from menu.Menu import Menu


class MenuHost(Menu):
    def __init__(self):
        super().__init__()
        self.submenu_users = None
        self.host = None

    def set_host(self, host):
        self.host = host

    def basic_information(self):
        print(f"{Fore.MAGENTA}Información básica{Fore.RESET}\n{self.host.basic_information}")

    def enumerate_useful_programs(self):
        if not self.host.programs.useful_programs:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.programs.enumerate_useful_programs()
            loader.stop()
        print(f"{Fore.MAGENTA}Programas{Fore.RESET}\n{self.host.programs.useful_programs}")
