import socket
import sys
from time import sleep

from colorama import Fore

from LibModule.HostNameFunctions import get_host_name_by_ip, nmb_look_up, avahi_resolve
from LibModule.Loader import Loader
from LibModule.constants import Constants
from LibModule.informationgatheringfunctions.Functions import get_manually_banner, manualy_grabber_manually
from LibModule.informationgatheringfunctions.Nmap import enum_scan_nmap, get_banner_nmap, open_ports_nmap
from LibModule.scanners.PING import get_value_ttl
from LibModule.validate import out_decode, out_nmap_validate


class HostInNetwork:
    def __init__(self):
        self.ip = ""
        self.mac = ""
        self.operative_system = ""
        self.host_name = ""
        self.banners = {}
        self.open_ports = []
        self.common_open_ports = []

    def get_host_name(self):
        host_name = get_host_name_by_ip(self.ip)
        if host_name == "Unknown":
            nmb_look_up(self.ip)
        if host_name == "Unknown":
            avahi_resolve(self.ip)
        self.host_name = host_name

    def get_os(self):
        ttl_value = get_value_ttl(self.ip)
        try:
            if ttl_value is not None:
                ttl_value = int(ttl_value)
        except ValueError:
            ttl_value = -1

        if ttl_value is not None:
            if 0 <= ttl_value <= 64:
                self.operative_system = "Linux"
            elif 65 <= ttl_value <= 128:
                if self.mac.startswith("a4:") or self.mac.startswith("a8:") or self.mac.startswith("ac:"):
                    self.operative_system = "Android"
                else:
                    self.operative_system = "Windows"
            else:
                self.operative_system = "Unknown"

    def get_banners(self, ports):
        loader = Loader("Loading...", "", 0.05).start()
        for port in ports:
            try:
                banner = get_banner_nmap(self.ip, str(port))
                if banner is not None:
                    banner = out_decode(banner)
                    loader.stop()
                    print(banner)
                    self.banners[port] = banner
                else:
                    self.banners[port] = manualy_grabber_manually(self.ip, int(port))
            except Exception as e:
                loader.stop()
                print(e)
                self.banners[port] = manualy_grabber_manually(self.ip, int(port))

    def check_vulnerability(self):
        try:
            banners = self.banners
            list_vuln_banners = open("vulnbanners")
            for line in list_vuln_banners.readlines():
                line = line.strip('\n')
                for banner in banners:
                    if banners[banner] in line:
                        print(Fore.GREEN + "Es vulnerable" + Fore.RESET + banner)
                    else:
                        print(Fore.RED + "No se encuentra en la lista de banners vulnerables")
        except TypeError:
            print(f"{Fore.RED}[!]No hay banners")

    def enum_services(self):
        loader = Loader("Loading...", "", 0.05).start()
        try:
            services = enum_scan_nmap(self.ip)
            if services is not None:
                services = out_decode(services)
                services, state = out_nmap_validate(services)
                loader.stop()
                return services
        except FileNotFoundError:
            loader.stop()
            print(f"{Fore.YELLOW}[!]Instala NMAP para poder usar esta utilidad.")
        except:
            loader.stop()
            print(Fore.RED + "[!]No se pudo enumerar los servicios")

    def get_common_open_ports(self):
        open_common_ports = []
        for common_port in Constants.__common_open_ports__:
            if self.is_port_open(common_port):
                print(f"Puerto {Fore.YELLOW + str(common_port) + Fore.RESET} abierto.")
                open_common_ports.append(common_port)
        self.common_open_ports = open_common_ports
        return open_common_ports

    def get_all_open_ports(self):
        loader = Loader("Loading...", "", 0.05).start()
        try:
            open_ports = open_ports_nmap(self.ip)
            loader.stop()
            if open_ports is not None:
                self.open_ports = open_ports
                for port in self.open_ports:
                    print(f"Puerto {Fore.YELLOW + str(port) + Fore.RESET} abierto.")
        except:
            open_ports = []
            for port in range(0, 65535):
                if self.is_port_open(port):
                    print(f"Puerto {Fore.YELLOW + str(port) + Fore.RESET} abierto.")
                    open_ports.append(port)
            self.open_ports = open_ports
            loader.stop()
            print(open_ports)
        return open_ports

    def is_port_open(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((self.ip, port))
            if result == 0:
                return True
            s.close()
            return False
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[X]Operación cancelada")
            pass
        except socket.gaierror:
            print(Fore.YELLOW + "\n[!]El Nombre del host no puede ser resuelto!!!")
            sys.exit(1)
        except socket.error:
            print(Fore.YELLOW + '\n[!]Host No Responde!!!')
            sys.exit(1)

    def __str__(self):
        return (
                Fore.LIGHTMAGENTA_EX + "IP: " + Fore.RESET + self.ip + "\n" +
                Fore.LIGHTMAGENTA_EX + "MAC: " + Fore.RESET + self.mac + "\n" +
                Fore.LIGHTMAGENTA_EX + "Nombre del host: " + Fore.RESET + self.host_name + "\n" +
                Fore.LIGHTMAGENTA_EX + "Sistema operativo: " + Fore.RESET + self.operative_system + "\n"
        )
