import socket
import sys

from colorama import Fore

from LibModule.HostNameFunctions import (get_host_name_by_ip,
                                         nmb_look_up, avahi_resolve)
from LibModule.Loader import Loader
from LibModule.constants import Constants
from LibModule.informationgatheringfunctions.Functions import (
    get_manually_banner, manualy_grabber_manually)
from LibModule.informationgatheringfunctions.Nmap import (
    enum_scan_nmap, get_banner_nmap, open_ports_nmap)
from LibModule.scanners.PING import get_value_ttl
from LibModule.validate import out_decode, out_nmap_validate, check_execs


class HostInNetwork:
    def __init__(self):
        self.ip = ""
        self.mac = []
        self.operative_system = ""
        self.host_name = ""
        self.banners = {}
        self.open_ports = []
        self.common_open_ports = []
        self.enum_services = ""

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
                if str(self.mac).startswith("a4:") or str(self.mac).startswith("a8:") or str(self.mac).startswith("ac:"):
                    self.operative_system = "Android"
                else:
                    self.operative_system = "Windows"
            else:
                self.operative_system = "Unknown"

    def get_banners(self, ports):
        for port in ports:
            try:
                if check_execs("nmap"):
                    loader = Loader("Loading...", "", 0.05).start()
                    banner = get_banner_nmap(self.ip, str(port))
                    loader.stop()
                    if banner is not None:
                        banner = out_decode(banner)
                        loader.stop()
                        print(banner)
                        self.banners[port] = banner
                else:
                    print(
                        f"{Fore.YELLOW}[!]Problema detectado, se intentará obtener los banners a través de una conexión con "
                        f"socket, enviando banners.\n[!]Tenga en cuenta que con esta opción puede no obtener todos los "
                        f"resultados como pueda ser con NMAP")
                    self.banners[port] = manualy_grabber_manually(self.ip, int(port))
            except Exception as e:
                loader.stop()
                print(
                    f"{Fore.YELLOW}[!]Problema detectado, se intentará obtener los banners a través de una conexión con "
                    f"socket, enviando banners.\n[!]Tenga en cuenta que con esta opción puede no obtener todos los "
                    f"resultados como pueda ser con NMAP")
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

    def get_enum_services(self):
        loader = Loader("Loading...", "", 0.05).start()
        try:
            services = enum_scan_nmap(self.ip)
            if services is not None:
                services = out_decode(services)
                services, state = out_nmap_validate(services)
                loader.stop()
                self.enum_services = services
        except FileNotFoundError:
            loader.stop()
            print(f"{Fore.YELLOW}[!]Instala NMAP para poder usar esta utilidad.{Fore.RESET}")
        except:
            loader.stop()
            print(Fore.RED + "[!]No se pudo enumerar los servicios" + Fore.RESET)

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
            if check_execs("nmap"):
                open_ports = open_ports_nmap(self.ip)
                loader.stop()
                if open_ports is not None:
                    self.open_ports = open_ports
                    for port in self.open_ports:
                        print(f"Puerto {Fore.YELLOW + str(port) + Fore.RESET} abierto.")
            else:
                open_ports = []
                loader.stop()
                for port in range(0, 65535):
                    if self.is_port_open(port):
                        print(f"Puerto {Fore.YELLOW + str(port) + Fore.RESET} abierto.")
                        open_ports.append(port)
                self.open_ports = open_ports
                print(open_ports)
        except:
            loader.stop()
            print("[!]Algo ha ido mal.")
            pass

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
            print(Fore.YELLOW + "\n[X]Operación cancelada" + Fore.RESET)
            pass
        except socket.gaierror:
            print(Fore.YELLOW + "\n[!]El Nombre del host no puede ser resuelto!!!" + Fore.RESET)
            sys.exit(1)
        except socket.error:
            print(Fore.YELLOW + '\n[!]Host No Responde!!!' + Fore.RESET)
            sys.exit(1)

    def __str__(self):
        return (
                Fore.LIGHTMAGENTA_EX + "IP: " + Fore.RESET + str(self.ip) + "\n" +
                Fore.LIGHTMAGENTA_EX + "MAC: " + Fore.RESET + str(self.mac) + "\n" +
                Fore.LIGHTMAGENTA_EX + "Nombre del host: " + Fore.RESET + str(self.host_name) + "\n" +
                Fore.LIGHTMAGENTA_EX + "Sistema operativo: " + Fore.RESET + str(self.operative_system) + "\n"+
                Fore.LIGHTMAGENTA_EX + "Servicios: " + Fore.RESET + str(self.enum_services) + "\n"
        )
