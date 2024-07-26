from LibModule.HostNameFunctions import get_host_name_by_ip, nmb_look_up, avahi_resolve
from LibModule.scanners.PING import get_value_ttl


class HostInNetwork:
    def __init__(self):
        self.ip = ""
        self.mac = ""
        self.operative_system = ""
        self.host_name = ""

    def __str__(self):
        return self.ip + " " + self.mac + ", " + self.host_name + ", " + self.operative_system

    def get_host_name(self, ip):
        host_name = get_host_name_by_ip(ip)
        if host_name == "Unknown":
            nmb_look_up(ip)
        if host_name == "Unknown":
            avahi_resolve(ip)

        self.host_name = host_name

    def get_os(self, ip):
        ttl_value = get_value_ttl(ip)
        try:
            if ttl_value is not None:
                ttl_value = int(ttl_value)
        except ValueError:
            ttl_value = -1

        if ttl_value is not None:
            if 0 <= ttl_value <= 64:
                self.operative_system = "Linux"
            elif 65 <= ttl_value <= 128:
                if self.mac.startswith("a4:") or self.mac.startswith("a8:") or self.mac.startswith("ac:"):
                    self.operative_system = "Android"
                else:
                    self.operative_system = "Windows"
            else:
                self.operative_system = "Unknown"
