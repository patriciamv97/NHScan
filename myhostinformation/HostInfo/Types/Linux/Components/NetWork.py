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
        self.network_connections = None
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
