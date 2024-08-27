import socket
import subprocess
import re

import psutil
from networkInformation.interfaces.NetworkInterface import NetWorkInterface


class NetWorkInterfaces:
    def __init__(self):
        self.interfaces = []

    def get_interfaces(self):
        addresses = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        for intface, addr_list in addresses.items():
            if intface in stats:
                interface = NetWorkInterface()
                interface.iface_name = intface or 'None'
                for addr in addr_list:
                    if addr.family == socket.AF_INET or addr.family == socket.AF_INET6:
                        interface.ip.append(addr.address)
                        interface.netmask = addr.netmask or 'None'
                        interface.broadcast = addr.broadcast or 'None'
                        interface.state = getattr(stats[intface], "isup")
                        interface.mtu = getattr(stats[intface], "mtu") or 'None'
                        interface.speed = getattr(stats[intface], "speed") or 'None'
                        interface.flags = getattr(stats[intface], "flags") or 'None'
                        interface.duplex = getattr(stats[intface], "duplex") or 'None'
                    if hasattr(socket, "AF_LINK"):
                        if addr.family == socket.AF_LINK:
                            interface.mac.append(addr.address)
                    interface.get_arp_cache()
                self.interfaces.append(interface)

