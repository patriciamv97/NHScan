import psutil

from LibModule.scanners.DNSFunctions import get_dns_linux
from myhostinformation.MyHost import MyHost
from networkInformation.NetWork import NetWork

'''def obtener_dns():
    dns_servidores = psutil.net_if_addrs()
    dns = []
    for interfaz, direcciones in dns_servidores.items():
        for direccion in direcciones:
            if socket.AF_INET == direccion.family and direccion.address:
                try:
                    hostname = socket.gethostbyaddr(direccion.address)
                    dns.append(direccion.address)
                except socket.herror:
                    pass
    return dns'''

if __name__ == "__main__":
    print(
        "Para calcular el cdir de tu red puedes hacerlo en : "
        "https://www.rohde-schwarz.com/es/soluciones/networks-and-cybersecurity/ciberseguridad/landing-pages"
        "/calculadora-de-cidr_256249.html")

    host = MyHost()

    print(host.operative_system)

    '''dns_servidores = psutil.net_if_addrs()
    for interfaz, direcciones in dns_servidores.items():
        print(interfaz)'''

    print("*****************************************")

    get_dns_linux()
    '''
    network = NetWork()
    network.get_interfaces()
    for interfaz in network.network_interfaces:
        print(interfaz.__str__())'''

    ''' ip_range="192.168.68.101/22"
    hosts_in_network = HostsInNetwork()
    hosts_in_network.get_hosts(ip_range)
    for host in hosts_in_network.hosts:
        print(host.__str__())'''

    '''  users = ps.users()

    for user in users:
        print(user)

    net_connection = ps.net_connections()

    for connection in net_connection:
        print(connection)



    host = Host()

    print(host.__str__())
    print(host.ip)

    nodeInfo =subprocess.check_output(["nmcli","-p", "device","show"], stderr=subprocess.STDOUT)
    nodeInfo = nodeInfo.decode('utf-8')
    print(nodeInfo)'''
