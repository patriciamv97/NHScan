from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command

commands_network = {
    1: "Get-NetRoute -AddressFamily IPv4 | Format-Table DestinationPrefix, NextHop, RouteMetric, IfIndex",
    2: "Get-PSDrive | where {$_.Provider -like 'Microsoft.PowerShell.Core\\FileSystem'}| ft",
    3: "Start-Process 'netstat' -ArgumentList '-ano' -NoNewWindow -Wait",  # Netwoekconnections,
    4: "Get-NetFirewallRule | Where-Object { $_.Enabled -eq 'True' } | Select-Object DisplayName, Direction, "
       "Profile, Enabled, Description"
}


class NetWork:

    def __init__(self):
        self.firewall_rules = ""
        self.network_connections = ""
        self.connected_drivers = ""
        self.route_table = ""

    def get_route_table(self):
        route_table, returncode = run_powershell_command(commands_network[1])
        if returncode == 0:
            self.route_table = route_table

    def get_conected_drivers(self):
        connected_drivers, returncode = run_powershell_command(commands_network[2])
        if returncode == 0:
            self.connected_drivers = connected_drivers

    def get_network_connections(self):
        network_connections, returncode = run_powershell_command(commands_network[3])
        if returncode == 0:
            self.network_connections = network_connections

    def get_firewall_rules(self):
        rules, returncode = run_powershell_command(commands_network[4])
        if returncode == 0:
            self.firewall_rules = rules

    def __str__(self):
        return (
                Fore.MAGENTA + "Reglas de firewall:\n\n" + Fore.RESET
                + self.firewall_rules + "\n\n" +
                Fore.MAGENTA + "Conexiones:\n\n" + Fore.RESET
                + self.network_connections + "\n\n" +
                Fore.MAGENTA + "Drivers conectados:\n\n" + Fore.RESET
                + self.connected_drivers + "\n\n" +
                Fore.MAGENTA + "Route Table:\n\n" + Fore.RESET
                + self.route_table + "\n\n")
