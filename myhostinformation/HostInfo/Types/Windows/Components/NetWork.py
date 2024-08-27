from LibModule.Loader import Loader
from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command
from myhostinformation.HostInfo.Types.Windows import Windows

commands_network = {
    1: "Get-NetRoute -AddressFamily IPv4 | Format-Table DestinationPrefix, NextHop, RouteMetric, IfIndex",
    2: "Get-PSDrive | where {$_.Provider -like 'Microsoft.PowerShell.Core\\FileSystem'}| ft",
    3: "Start-Process 'netstat' -ArgumentList '-ano' -NoNewWindow -Wait",  # Netwoekconnections,
    4: "Get-NetFirewallRule | Where-Object { $_.Enabled -eq 'True' } | Select-Object DisplayName, Direction, "
       "Profile, Enabled, Description"
}


class NetWork:

    def __init__(self):
        self.firewall_rules = None
        self.network_connections = None
        self.connected_drivers = None
        self.route_table = None

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
