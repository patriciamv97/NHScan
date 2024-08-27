import ipaddress
import re

from colorama import Fore

from LibModule.constants import Constants
from myhostinformation.MyHost import MyHost


def validate_ip_address_r(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        print(f"{ip} no es una dirección IPV4 o IPV6 válida.")
        ip = input("Introduce un rango de red válido:\n")
        ip_validate = validate_ip_address_r(ip)
        if ip_validate:
            return ip_validate


def validate_network_r(network_range):
    try:
        network_range_validate = ipaddress.ip_network(network_range, False)
        return network_range_validate
    except ValueError:
        print(f"{network_range} no es rango de red válido.")
        network_range = input("Introduce un rango de red válido:\n")
        network_range_validate = validate_network_r(network_range)
        if network_range_validate:
            return network_range_validate


def validate_ip(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        print(f"{Fore.YELLOW + ip + Fore.RESET} no es una dirección IPV4 o IPV6 válida.")


def validate_network(network_range):
    try:
        return ipaddress.ip_network(network_range, False)
    except ValueError:
        print(f"{Fore.YELLOW + network_range + Fore.RESET} no es rango de red válido.")


def get_network_range():
    num_attemps_max = 5
    network_range = input(Fore.BLUE + "Introduce el rango de red que quieres escanera. "
                          + "Ej: 192.168.1.0/24\n" + Fore.RESET
                          + Fore.WHITE + "[!]INFORMACION: Puedes comprobar el cdir en el siguiente enlace:"
                          + Fore.RESET + Fore.CYAN + "\n" + Constants.__enlace_cdir__ + "\n")
    network_validate = validate_network(network_range)
    while network_validate is None and num_attemps_max > 0:
        num_attemps_max -= 1
        network_range = input(Fore.BLUE + "Introduce un rango de red válido:\n" + Fore.RESET)
        network_validate = validate_network(network_range)
    if network_validate:
        return network_range


def get_ip_address():
    num_attemps_max = 5
    ip = input(Fore.BLUE + "Introduce la direccion del host que quieres escanear.\n" + Fore.RESET)
    ip_validate = validate_ip(ip)
    while ip_validate is None and num_attemps_max > 0:
        num_attemps_max -= 1
        ip = input(Fore.BLUE + "Introduce una dirección válida:\n" + Fore.RESET)
        ip_validate = validate_network(ip)
    if ip_validate:
        return ip


def out_decode(out):
    os = MyHost().operative_system
    if os == "Windows":
        return out.decode('latin-1')
    elif os == "Linux":
        return out.decode('utf-8')
    else:
        return f"{Fore.YELLOW}Codificación desconociad: \n{Fore.RESET}{out}"


def out_nmap_validate(out):
    no_host = re.findall(r'0 hosts up', out)
    if no_host:

        return (
            f"{Fore.YELLOW}[!]La máquina no está activa y disponible.\nSi se tiene constancia de que la máquina sí "
            f"está activa, revisa la configuración de la red o de las infertaces."), 0
    else:
        return out, 1
