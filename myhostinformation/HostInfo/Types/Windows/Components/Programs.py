from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_command


class Programs:

    commands_programs = {
        1: "where nmap aws nc ncat netcat nc.traditional wget curl ping gcc make gdb base64 socat python python2 "
           "python3 python2.7 python2.6 python3.6 python3.7 pearl php ruby xterm doas sudo fetch docker lxc ctr "
           "runc rkt kubectl 2>null"
    }

    def __init__(self):
        self.useful_programs = ""

    def enumerate_useful_programs(self):
        self.useful_programs = run_command(self.commands_programs[1])
