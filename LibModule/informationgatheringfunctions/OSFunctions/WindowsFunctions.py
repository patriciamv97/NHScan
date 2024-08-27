import re
import subprocess

import wmi
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
    proc = subprocess.Popen(("cmd /c" + command).split())
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()


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
