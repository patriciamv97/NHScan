import subprocess


def enum_scan_nmap(ip):
    nmap = subprocess.Popen(["nmap", ip, "-n", "-sS", "-A", "-T4"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        return None
    return out


def open_ports_nmap(ip):
    nmap = subprocess.Popen(["nmap", ip, "-n", "-sS", "-A", "-T4"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, err = nmap.communicate()
    if err:
        return None
    return out


def get_dhcp_nmap():
    nmap = subprocess.Popen(["nmap", "--script=broadcast-dhcp-discover"], stdout=subprocess.PIPE,
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
