from IPy import IP
from netifaces import interfaces, ifaddresses, AF_INET, AF_LINK


class NetWorkInterface:
    def __init__(self):

        self.ip = " "
        self.mac = " "
        self.netmask = ""
        self.broadcast = ""
        self.vlan = ""
        self.iface = ""

    @classmethod
    def get_interface(self):

        for ifaceName in interfaces():
            if ifaceName.count("."):
                (iface, vlan) = ifaceName.split(".")
            else:
                iface = ifaceName
                vlan = "None"

        self.iface = iface
        self.vlan = vlan

        if AF_LINK in ifaddresses(ifaceName):
            mac = ifaddresses(ifaceName)[AF_LINK][0]['addr']

        else:
            mac = None

        self.mac = mac
        if AF_INET in ifaddresses(ifaceName):
            for address in ifaddresses(ifaceName)[AF_INET]:
                self.broadcast = address['broadcast']
                self.ip = address['addr']
                self.netmask = address['netmask']
        return NetWorkInterface
