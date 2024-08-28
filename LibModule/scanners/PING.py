import platform
import re
import subprocess

from LibModule.validate import out_decode


def get_value_ttl(ip_address):
    if platform.system() == "Windows":
        command = "ping " + ip_address
    else:
        command = "ping -c 1 " + ip_address
    proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out_decode(out)
    ttl = re.findall(r"(?<=TTL=)\d{1,3}", out)
    if len(ttl) == 0:
        ttl = re.findall(r"(?<=ttl=)\d{1,3}", out)
    if len(ttl)==0:
        return None
    return ttl[0]
