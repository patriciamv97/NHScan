from colorama import Fore

from LibModule.Loader import Loader
from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuNetWork(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def route_table(self):
        if not self.host.network.route_table:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.network.get_route_table()
            loader.stop()
        print(f"{Fore.MAGENTA}Tabla de ruta{Fore.RESET}")
        print(self.host.network.route_table)

    def conected_drivers(self):
        if not self.host.network.connected_drivers:
            self.host.network.get_conected_drivers()
        print(f"{Fore.MAGENTA}Drivers conectados:{Fore.RESET}")
        print(self.host.network.connected_drivers)

    def network_connections(self):
        if not self.host.network.network_connections:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.network.get_network_connections()
            loader.stop()
        print(f"{Fore.MAGENTA}Conexiones de red{Fore.RESET}")
        print(self.host.network.network_connections)

    def firewall_rules(self):
        if not self.host.network.firewall_rules:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.network.get_firewall_rules()
            loader.stop()
            print(f"{Fore.MAGENTA}Reglas del firewall{Fore.RESET}")
            print(self.host.network.firewall_rules)

    def get_list_of_available_disks_and_partitions(self):
        if not self.host.network.list_of_available_disks_and_partitions:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.network.get_list_of_available_disks_and_partitions()
            loader.stop()
            print(f"{Fore.MAGENTA}Lista de discos y particiones disponibles{Fore.RESET}")
            print(self.host.network.list_of_available_disks_and_partitions)

    def get_open_files_related_to_network_connections(self):
        if not self.host.network.open_files_related_to_network_connections:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.network.get_open_files_related_to_network_connections()
            loader.stop()
        print(f"{Fore.MAGENTA}Archivos abiertos relacionados con conexiones de red{Fore.RESET}")
        print(self.host.network.open_files_related_to_network_connections)
