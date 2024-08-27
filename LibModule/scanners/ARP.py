from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp


def get_mac_by_ip(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    mac = []

    for sent, recieved in result:
        mac.append(recieved.hwsrc)

    return mac


def get_hosts_with_arp(network_range):
    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, recieved in result:
        clients.append({"ip": recieved.psrc, "mac": recieved.hwsrc})

    return clients
