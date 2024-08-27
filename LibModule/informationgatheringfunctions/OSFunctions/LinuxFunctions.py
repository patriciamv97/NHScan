import re
import subprocess

from LibModule.validate import out_decode, out_nmap_validate


def run_command(command):
    try:
        result = subprocess.run(
            command,
            check=True,  # Levanta una excepción si el comando falla
            stdout=subprocess.PIPE,  # Captura la salida estándar
            stderr=subprocess.PIPE,  # Captura la salida de error
            text=True  # Devuelve la salida como texto en lugar de bytes
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        # Si el comando falla, entra aquí
        print(f"Error: El comando falló con el código de salida {e.returncode}")
        print(f"Salida estándar de error: {e.stderr}")  # Muestra la salida de error

    except FileNotFoundError:
        # Si el comando no se encuentra (por ejemplo, ejecutable inexistente)
        print("Error: El comando no existe en el sistema.")

def get_dns_linux():
    cat = subprocess.Popen(["cat", "/etc/resolv.conf"], stdout=subprocess.PIPE)
    grep = subprocess.Popen(["grep", "nameserver"], stdin=cat.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cat.stdout.close()
    out, err = grep.communicate()
    if len(out) > 0:
        nameservers = out.decode().replace("nameserver", "").split()
        return nameservers
    else:
        return err.decode()


def get_arp_cache_linux(interface_address):
    arp_cache = subprocess.check_output(["arp", "-e", interface_address])
    return arp_cache.decode('utf-8')


def get_dhcp_linux():
    out = get_dhcp_linux()
    if out is not None:
        dhcp = out_decode(out)
        dhcp, status = out_nmap_validate(dhcp)
        if status == 1:
            lines = dhcp.split("\n")
            for line in lines:
                if "DHCP" in line:
                    return line.split(" ")[-1]