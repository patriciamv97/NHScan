import importlib
import os
import re
import subprocess
import platform

if platform.system() == 'Windows':
    wmi = importlib.import_module('wmi')
from colorama import Fore


def run_powershell_command(command):
    out = run(command)
    if out.returncode != 0:
        if out.stdout is not None:
            return (f"{Fore.YELLOW}[!]Algo pudo haber fallado.{Fore.RESET}\n{out.stdout.decode('latin1')}"
                    f"\n{out.stderr.decode('latin1')}"), out.returncode
        return None
    return out.stdout.decode('latin1'), out.returncode


def run_command(command):
    try:
        search_directory = os.getenv('USERPROFILE')
        result = subprocess.run(
            ("cmd /c " + command).split(),
            cwd=search_directory,
            stdout=subprocess.PIPE,  # Captura la salida estándar
            stderr=subprocess.PIPE,  # Captura la salida de error
            text=True,  # Devuelve la salida como texto en lugar de bytes
            encoding='latin-1'
        )

        if result.returncode == 0:
            return result.stdout  # Retorna la salida si encuentra coincidencias
        else:
            return result.stderr

    except subprocess.CalledProcessError as e:
        # Si el comando falla, entra aquí
        print(f"Error: El comando falló con el código de salida {e.returncode}")
        print(f"Salida estándar de error: {e.stderr}")  # Muestra la salida de error

    except FileNotFoundError:
        # Si el comando no se encuentra (por ejemplo, ejecutable inexistente)
        print("Error: El comando no existe en el sistema.")


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def get_dns_client_server_address():
    dns = run("Get-DnsClientServerAddress -AddressFamily IPv4 |ft")
    if dns.returncode != 0:
        print("An error occured: %s", dns.stderr)
    else:
        dns_ips = []
        out = dns.stdout.decode('latin-1')
        lines = out.splitlines()
        for line in lines:
            ips = re.findall(r'\{([^}]+)\}', line)
            for ip in ips:
                if ip.strip():
                    dns_ips.extend([x.strip() for x in ip.split(',') if x.strip()])
        return dns_ips


def get_dhcp_windows():
    c = wmi.WMI()
    for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if adapter.DHCPServer:
            return adapter.DHCPServer
    return None


def get_wmi_adapter_dns():
    c = wmi.WMI()
    for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if adapter.DNSServerSearchOrder:
            return adapter.DNSServerSearchOrder
    return None


def get_arp_cache_windows(interface_address):
    arp_cache = run("arp /a /n " + interface_address)
    if arp_cache.returncode != 0:
        return "None"
    return arp_cache.stdout.decode('latin1')
