from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands_network = {
    1: "route | netstat -r",
    2: "df -h",
    3: "ls /dev 2>/dev/null | grep -i 'sd'",  # Netwoekconnections,
    4: "netstat -tulpne",
    5: "iptables -L",
    6: "cat /etc/fstab  | grep -v '^#' | grep -Pv '\\W*\\#'",
    7: "lsof -i"
}


class NetWork:

    def __init__(self):
        self.firewall_rules = None
        self.network_connections = None
        self.connected_drivers = None
        self.route_table = None
        self.list_of_available_disks_and_partitions = None
        self.open_files_related_to_network_connections = None

    def get_route_table(self):
        self.route_table = run_command(commands_network[1])

    def get_conected_drivers(self):
        self.connected_drivers = run_command(commands_network[2])

    def get_network_connections(self):
        self.network_connections = run_command(commands_network[3])

    def get_firewall_rules(self):
        self.firewall_rules = run_command(commands_network[5])

    def get_list_of_available_disks_and_partitions(self):
        self.list_of_available_disks_and_partitions = run_command(commands_network[6])

    def get_open_files_related_to_network_connections(self):
        self.open_files_related_to_network_connections = run_command(commands_network[7])

    def __str__(self):
        return (
                Fore.MAGENTA + "Reglas de firewall:\n\n" + Fore.RESET
                + self.firewall_rules + "\n\n" +
                Fore.MAGENTA + "Conexiones:\n\n" + Fore.RESET
                + self.network_connections + "\n\n" +
                Fore.MAGENTA + "Drivers conectados:\n\n" + Fore.RESET
                + self.connected_drivers + "\n\n" +
                Fore.MAGENTA + "Route Table:\n\n" + Fore.RESET
                + self.route_table + "\n\n" +
                Fore.MAGENTA + "Lista de discos y particiones disponibles:\n\n" + Fore.RESET
                + self.list_of_available_disks_and_partitions + "\n\n" +
                Fore.MAGENTA + "Archivos abiertos relacionados con conexiones de red :\n\n" + Fore.RESET
                + self.open_files_related_to_network_connections + "\n\n")
