from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuNetWork(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def route_table(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.network.get_route_table()
        loader.stop()
        if self.host.network.route_table:
            print(f"{Fore.MAGENTA}Tabla de ruta{Fore.RESET}")
            print(self.host.network.route_table)

    def conected_drivers(self):
        self.host.network.get_conected_drivers()
        if self.host.network.connected_drivers:
            print(f"{Fore.MAGENTA}Drivers conectados:{Fore.RESET}")
            print(self.host.network.connected_drivers)

    def network_connections(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.network.get_network_connections()
        loader.stop()
        if self.host.network.network_connections:
            print(f"{Fore.MAGENTA}Conexiones de red{Fore.RESET}")
            print(self.host.network.network_connections)

    def firewall_rules(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.network.get_firewall_rules()
        loader.stop()
        if self.host.network.firewall_rules:
            print(f"{Fore.MAGENTA}Reglas del firewall{Fore.RESET}")
            print(self.host.network.firewall_rules)