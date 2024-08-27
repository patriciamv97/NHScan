import subprocess


def enum_scan_nmap(ip):
    nmap = subprocess.Popen(["nmap", ip, "-n", "-sS", "-A", "-T4"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        return None
    return out


def open_ports_nmap(ip):
    command = "nmap 192.168.68.102 -p- | awk '/^[0-9]/ {print $1}' | cut -d'/' -f1"
    try:
        result = subprocess.run(
            command,
            check=True,  # Levanta una excepción si el comando falla
            stdout=subprocess.PIPE,  # Captura la salida estándar
            stderr=subprocess.PIPE,  # Captura la salida de error
            text=True,  # Devuelve la salida como texto en lugar de bytes
            shell=True

        )
        return result.stdout.split()

    except subprocess.CalledProcessError as e:
        print(f"Error: El comando falló con el código de salida {e.returncode}")
        print(f"Salida estándar de error: {e.stderr}")
        if e.stdout:
            print(e.stdout)
    except FileNotFoundError:
        print("Error: El comando no existe en el sistema.")


def is_port_open_nmap(ip, port):
    nmap = subprocess.Popen(["nmap", ip, "-p", port], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        return None
    return out


def get_dhcp_nmap(ip):
    nmap = subprocess.Popen(["nmap", "--script=broadcast-dhcp-discover", ip], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        print(f"Error: {err.decode('utf-8')}")
    return out


def get_banner_nmap(ip, port):
    nmap = subprocess.Popen(["nmap", "-sV", "--script=banner", ip, "-p", port, "-Pn"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        return None
    return out
