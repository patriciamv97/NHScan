import sys

from colorama import Fore

from LibModule.Loader import Loader
from LibModule.constants import Constants
from LibModule.scanners.ARP import get_mac_by_ip
from LibModule.validate import get_ip_address
from menu.Menu import Menu


class MenuNetWorkHost(Menu):
    def __init__(self):
        super().__init__()
        self.host = None

    def set_host_in_network(self, host_in_network):
        self.host = host_in_network

    def main_menu(self):
        try:
            ip_address = get_ip_address()
            if ip_address:
                self.host.ip = ip_address
                super().main_menu()
            else:
                print(Fore.RED + "Tienes que meter una direccion correcta.")
                super().exit_program()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[X]Operación cancelada")
            pass

    def get_network_host(self):
        loader = Loader("Loading...", "", 0.05).start()
        self.host.get_os()
        self.host.get_host_name()
        self.host.mac = get_mac_by_ip(self.host.ip)
        loader.stop()
        print(Fore.MAGENTA + "IP: " + Fore.RESET + self.host.ip + "\n" +
              Fore.MAGENTA + "MAC: " + Fore.RESET + ' '.join(self.host.mac) + "\n" +
              Fore.MAGENTA + "Nombre del host: " + Fore.RESET + self.host.host_name + "\n" +
              Fore.MAGENTA + "Sistema operativo: " + Fore.RESET + self.host.operative_system)

    def enmu_services(self):
        if not self.host.enum_services:
            loader = Loader("Loading...", "", 0.05).start()
            self.host.get_enum_services()
            loader.stop()
        print(self.host.enum_services)

    def get_common_open_ports(self):
        self.host.get_common_open_ports()

    def get_open_ports(self):
        self.host.get_all_open_ports()

    # TODO-> REFACTORIZAR
    def get_banners(self):
        opciones = ["Banners de todos puertos abiertos", "Banners de los puertos comunes",
                    "Introduce un puerto para sacar el banner"]
        for i, opcion in enumerate(opciones):
            print(f"{Fore.LIGHTMAGENTA_EX}\t{i + 1}){Fore.RESET} {opcion}")
        seleccion = input("Selecciona una opción: ")
        eleccion = int(seleccion)

        if eleccion == 1:
            print(
                Fore.YELLOW + "[!]Debes hacer un escaneo de puertos abiertos para poder obtener los banners." + Fore.RESET)
            if self.host.open_ports:
                self.host.get_banners(self.host.open_ports)
        elif eleccion == 2:
            self.host.get_banners(Constants.__common_open_ports__)
        elif eleccion == 3:
            ports = input(
                Fore.CYAN + "Introduce, un puerto o varios puertos para obtener el banner.\n" + Fore.YELLOW +
                "En el caso de introducir varios puertos, hagalo separandolos por comas. Ej: 22, 23, 25\n" + Fore.RESET).split(
                ',')
            self.host.get_banners(ports)
        else:
            print(Fore.RED + "Formato no válido. Debes elegir una opción de las tres anteriores")

    def check_vulns(self):
        if len(self.host.banners) > 0:
            self.host.check_vulnerability()
        else:
            print(f"{Fore.YELLOW}[!]No hay banners")
