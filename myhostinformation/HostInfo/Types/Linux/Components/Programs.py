from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands_network = {
    1: "route | netstat -r",
    2: "df -h",
    3: "ls /dev 2>/dev/null | grep -i",  # Netwoekconnections,
    4: "netstat -tulpne ",
    5: "iptables -L",
    6: "cat /etc/fstab 2>dev/null | grep -v '^#' | grep -Pv '\\W*\\#'",
    7: "lsof -i"
}


class Programs:
    commands_programs = {
        1: "which nmap aws nc ncat netcat nc.traditional wget curl ping gcc make gdb base64 socat python python2 "
           "python3 python2.7 python2.6 python3.6 python3.7 pearl php ruby xterm doas sudo fetch docker lxc ctr "
           "runc rkt kubectl 2>null"
    }

    def __init__(self):
        self.useful_programs = None

    def enumerate_useful_programs(self):
        self.useful_programs = run_command(self.commands_programs[1])
