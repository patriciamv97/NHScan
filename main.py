import os
import subprocess
import psutil as ps
from hostinformation.host import Host

if __name__ == "__main__":
    host = Host()
    print(host.__str__())

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
