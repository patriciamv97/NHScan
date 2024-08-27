import psutil
from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import get_arp_cache_linux
from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import get_arp_cache_windows
from myhostinformation.MyHost import MyHost


class NetWorkInterface:

    def __init__(self):
        self.iface_name = ""
        self.ip = []
        self.mac = []
        self.netmask = ""
        self.broadcast = ""
        self.state = ""
        self.mtu = ""
        self.flags = ""
        self.speed = ""
        self.duplex = ""
        self.arp_cache = ""

    def get_arp_cache(self):
        my_host = MyHost()
        if len(self.ip) > 0:
            if my_host.operative_system == "Linux":
                self.arp_cache = get_arp_cache_linux(self.ip[0]) or 'None'
            elif my_host.operative_system == "Windows":
                self.arp_cache = get_arp_cache_windows(self.ip[0])

    def get_duplex(self):
        match self.duplex:
            case psutil.NIC_DUPLEX_FULL:
                return "FULL DUPLEX"
            case psutil.NIC_DUPLEX_HALF:
                return "HALF FULL DUPLEX"
            case psutil.NIC_DUPLEX_HALF:
                return "UNKNOWN"

    def get_state(self):
        return "Activo" if self.state else "Desconectado"

    def __str__(self):
        return (Fore.LIGHTMAGENTA_EX + "Interface: " + Fore.RESET + self.iface_name + "\n" +
                Fore.LIGHTMAGENTA_EX + "IP: " + Fore.RESET + ','.join(self.ip) + "\n" +
                Fore.LIGHTMAGENTA_EX + "MAC: " + Fore.RESET + ','.join(self.mac) + "\n" +
                Fore.LIGHTMAGENTA_EX + "Netmask: " + Fore.RESET + self.netmask + "\n" +
                Fore.LIGHTMAGENTA_EX + "Broadcast: " + Fore.RESET + self.broadcast + "\n" +
                Fore.LIGHTMAGENTA_EX + "Estado: " + Fore.RESET + self.get_state() + "\n" +
                Fore.LIGHTMAGENTA_EX + "MTU: " + Fore.RESET + str(self.mtu) + "\n" +
                Fore.LIGHTMAGENTA_EX + "Flags:" + Fore.RESET + self.flags + "\n" +
                Fore.LIGHTMAGENTA_EX + "Velocidad: " + Fore.RESET + str(self.speed) + "\n" +
                Fore.LIGHTMAGENTA_EX + "Canal: " + Fore.RESET + self.get_duplex() + "\n" +
                Fore.LIGHTMAGENTA_EX + "ARP Cache: " + Fore.RESET + self.arp_cache)
