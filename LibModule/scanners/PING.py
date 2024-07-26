import re
import subprocess


def get_value_ttl(ip_address):
    proc = subprocess.Popen(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    ttl = re.findall(r"(?<=TTL=)\d{1,3}", str(out))
    if ttl:
        return ttl[0]


