from netifaces import gateways
from networkInformation.hosts.HostInNetWork import HostInNetwork
from networkInformation.interfaces.NetWorkInterfaces import NetWorkInterfaces
from LibModule.scanners.ARP import get_hosts_with_arp


class NetWork:
    def __init__(self):
        self.network_gateways = []
        self.network_interfaces = []
        self.network_dhcp = []
        self.network_dns = []
        self.host_in_network = []

    def get_gateways(self):
        all_gateways = gateways()[2]
        for gateway in all_gateways:
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
            if discovered_host.ip != "":
                discovered_host.get_host_name(discovered_host.ip)
                discovered_host.get_os(discovered_host.ip)
                self.host_in_network.append(discovered_host)
