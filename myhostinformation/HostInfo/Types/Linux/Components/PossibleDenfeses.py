from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands = {
    1: 'uname -r',
    2: 'grep grsecurity /etc/sysctl.conf',
    3: 'which paxctl-ng paxctl 2>/dev/null',
    4: 'grep "exec-shield" /etc/sysctl.conf 2>/dev/null',
    5: 'sestatus 2>/dev/null',
    6: 'cat /proc/sys/kernel/randomize_va_space 2>/dev/null',
    7: 'which aa-status 2>/dev/null',
    8: 'aa-status',
    9: 'which apparmor_status 2>/dev/null',
    10: 'apparmor_status',
    11: 'ls -d /etc/apparmor* 2>/dev/null',
}


class PossibleDefenses:

    def __init__(self):
        self.apparmor = None
        self.grsecurity = None
        self.exec_shield = None
        self.pax = None
        self.selinux = None
        self.alsr = None

    def get_apparmor(self):
        if run_command(commands[7].split()):
            self.apparmor = run_command(commands[8].split())
        elif run_command(commands[9].split()):
            self.apparmor = run_command(commands[10].split())
        elif run_command(commands[11].split()):
            self.apparmor = run_command(commands[11].split())
        else:
            print("No se ha encontrado")

    def get_grsecurity(self):
        try:
            uname_check = run_command(commands[1].split())

            if "-grsec" in uname_check:
                self.grsecurity = uname_check

            sysctl_check = run_command(commands[2].split())

            if sysctl_check:
                self.grsecurity = sysctl_check
            else:
                print("Not found grsecurity")

        except Exception as e:
            print(f"Error al ejecutar el comando: {e}")

    def get_pax(self):
        self.pax = run_command(commands[3].split())

    def get_exec_shield(self):
        self.exec_shield = run_command(commands[4].split())

    def get_ses_linux(self):
        self.selinux = run_command(commands[5].split())

    def get_aslr(self):
        self.alsr = run_command(commands[6].split())
