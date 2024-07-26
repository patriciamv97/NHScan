import subprocess


def get_dns_linux():
    dns = subprocess.check_output(["cat", "/etc/resolv.conf", "|", "grep", "nameserver"])
    print(dns)