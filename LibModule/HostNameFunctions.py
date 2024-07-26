import subprocess
from socket import gethostbyaddr, herror


def get_host_name_by_ip(ip):
    try:
        return gethostbyaddr(ip)[0]
    except herror:
        return "Unknown"


def nmb_look_up(ip):
    try:
        output = subprocess.check_output(['nmblookup', '-A', ip])
        return output.decode().split('\n')[1].split()[0]
    except:
        return "Unknown"


def avahi_resolve(ip):
    try:
        output = subprocess.check_output(['avahi-resolve', '-a', ip])
        return output.decode().split('\t')[1].strip()
    except:
        return "Unknown"
