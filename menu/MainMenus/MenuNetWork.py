import sys

from colorama import Fore

from LibModule.Loader import Loader
from LibModule.validate import get_network_range, get_ip_address
from menu.Menu import Menu
from networkInformation.interfaces.NetWorkInterfaces import NetWorkInterfaces


class MenuNetWork(Menu):
    def __init__(self):
        super().__init__()
        self.network = None

    def set_network(self, network):
        self.network = network

    def get_network_info(self):
        valid_ip_range = get_network_range()
        loader = Loader("Loading...", "", 0.05).start()
        try:
            if not self.network.network_dns:
                self.network.get_dns()
            if not self.network.network_dhcp:
                self.network.get_dhcp(valid_ip_range)
            if not self.network.network_interfaces:
                self.network.get_interfaces()
            if not self.network.network_gateways:
                self.network.get_gateways()
            if not self.network.host_in_network:
                self.network.get_other_host(valid_ip_range)
            loader.stop()
            print(self.network.__str__())
        except KeyboardInterrupt:
            loader.stop()
            pass

    @staticmethod
    def get_network_interfaces():
        network_interfaces = NetWorkInterfaces()
        if not network_interfaces.interfaces:
            loader = Loader("Loading...", "", 0.05).start()
            network_interfaces.get_interfaces()
            loader.stop()
        for interface in network_interfaces.interfaces:
            print(interface.__str__())

    def get_gateways(self):
        if len(self.network.network_gateways) == 0:
            self.network.get_gateways()
        for gateway in self.network.network_gateways:
            print(
                Fore.CYAN + "Puerta de enlace:\n" + Fore.RESET + "\t" +
                gateway
            )

    def get_dns(self):
        if len(self.network.network_dns) ==0:
            self.network.get_dns()
        for dns in self.network.network_dns:
            print(
                Fore.CYAN + "Servidor DNS:\n" + Fore.RESET + "\t" +
                dns
            )

    def get_dhcp(self):
        if len(self.network.network_dhcp) == 0:
            self.network.get_dhcp()
        print(
            Fore.CYAN + "Servidor DHCP:\n" + Fore.RESET + "\t" +
            str(self.network.network_dhcp)
            )

    def get_network_hosts(self):
        if len(self.network.host_in_network) == 0:
            self.network.get_other_host(get_network_range())
        for host in self.network.host_in_network:
            print(host.__str__())
