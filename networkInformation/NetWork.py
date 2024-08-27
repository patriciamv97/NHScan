from colorama import Fore
from netifaces import gateways

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import get_dns_linux, get_dhcp_linux
from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import get_dns_client_server_address, \
    get_wmi_adapter_dns, get_dhcp_windows
from LibModule.scanners.ARP import get_hosts_with_arp
from myhostinformation.MyHost import MyHost
from networkInformation.hosts.HostInNetWork import HostInNetwork
from networkInformation.interfaces.NetWorkInterfaces import NetWorkInterfaces


class NetWork:
    def __init__(self):
        self.network_gateways = []
        self.network_interfaces = []
        self.network_dhcp = ""
        self.network_dns = []
        self.host_in_network = []

    def get_gateways(self):
        all_gateways = gateways()[2]
        for gateway in all_gateways:
            if gateway[0] not in self.network_gateways:
                self.network_gateways.append(gateway[0])

    def get_interfaces(self):
        network_interfaces = NetWorkInterfaces()
        network_interfaces.get_interfaces()
        self.network_interfaces = network_interfaces.interfaces

    def get_other_host(self, ip_range):
        hosts = get_hosts_with_arp(network_range=ip_range)
        for host in hosts:
            discovered_host = HostInNetwork()
            discovered_host.ip = host["ip"]
            discovered_host.mac = host["mac"]
            if discovered_host.ip:
                discovered_host.get_host_name()
                discovered_host.get_os()
                if discovered_host not in self.host_in_network:
                    self.host_in_network.append(discovered_host)

    def get_dns(self):
        my_host = MyHost()
        if my_host.operative_system == "Linux":
            self.network_dns = get_dns_linux()
        elif my_host.operative_system == "Windows":
            dns = get_wmi_adapter_dns()
            if dns is not None:
                self.network_dns = dns
            else:
                self.network_dns = get_dns_client_server_address()

    def get_dhcp(self):
        my_host = MyHost()
        if my_host.operative_system == "Linux":
            self.network_dhcp = get_dhcp_linux()
        elif my_host.operative_system == "Windows":
            self.network_dhcp = get_dhcp_windows()

    def get_str_host(self):
        host_str = ""
        for host in self.host_in_network:
            host_str += host.__str__() + "\n"
        return host_str

    def get_str_interfaces(self):
        interface_str = ""
        for interface in self.network_interfaces:
            interface_str += interface.__str__() + "\n"
        return interface_str

    def __str__(self):
        return (
                Fore.MAGENTA + "Servidores DNS:\n\n" + Fore.RESET + str(', '.join(self.network_dns)) + "\n\n" +
                Fore.MAGENTA + "Servidores DHCP:\n\n" + Fore.RESET + str(self.network_dhcp) + "\n\n" +
                Fore.MAGENTA + "Host conectados:\n\n" + Fore.RESET + self.get_str_host() + "\n\n" +
                Fore.MAGENTA + "Interfaces de red:\n\n" + Fore.RESET + self.get_str_interfaces() + "\n\n" +
                Fore.MAGENTA + "Puertas de enlace:\n\n" + Fore.RESET + '\n'.join(self.network_gateways)
        )
