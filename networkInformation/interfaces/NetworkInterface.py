import psutil


class NetWorkInterface:

    def __init__(self):
        self.iface_name = ""
        self.ip = []
        self.mac = []
        self.netmask = ""
        self.broadcast = ""
        self.state = ""
        self.mtu = ""
        self.flags = ""
        self.speed = ""
        self.duplex = ""

    def get_duplex(self):
        match self.duplex:
            case psutil.NIC_DUPLEX_FULL:
                return "FULL DUPLEX"
            case psutil.NIC_DUPLEX_HALF:
                return "HALF FULL DUPLEX"
            case psutil.NIC_DUPLEX_HALF:
                return "UNKNOWN"

    def get_state(self):
        return "Activo" if self.state else "Desconectado"

    def __str__(self):
        return (self.iface_name + "," + ','.join(self.ip) + "," + ','.join(self.mac) + "," + self.netmask
                + "," + self.broadcast + "," + self.get_state() + "," + str(self.mtu) + "," + self.flags + "," + str(
                    self.speed) + ", " + self.get_duplex())
