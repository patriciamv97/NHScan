from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands = {
    2: '((uname -r | grep "\-grsec" >/dev/null 2>&1 || grep "grsecurity" /etc/sysctl.conf >/dev/null 2>&1) && echo '
       '"Yes" || echo "Not found grsecurity")',
    3: '(which paxctl-ng paxctl >/dev/null 2>&1 && echo "Yes" || echo "Not found PaX")',
    4: '(grep "exec-shield" /etc/sysctl.conf || echo "Not found Execshield")',
    5: '(sestatus 2>/dev/null || echo "Not found sestatus")',
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
        if run_command(commands[7]):
            self.apparmor = run_command(commands[8])
        elif run_command(commands[9]):
            self.apparmor = run_command(commands[10])
        elif run_command(commands[11]):
            self.apparmor = run_command(commands[11])
        else:
            print("No se ha encontrado")

    def get_grsecurity(self):
        self.grsecurity = run_command(commands[2])

    def get_pax(self):
        self.pax = run_command(commands[3])

    def get_exec_shield(self):
        self.exec_shield = run_command(commands[4])

    def get_selinux(self):
        self.selinux = run_command(commands[5])

    def get_aslr(self):
        alsr = run_command(commands[6])
        match int(alsr):
            case 0:
                self.alsr = "Sin aleatorización. Todo es estático."

            case 1:
                self.alsr = (
                    "Aleatorización conservadora. Se aleatorizan las bibliotecas compartidas, la pila, mmap(), "
                    "\nla página VDSO.")

            case 2:
                self.alsr = ("Aleatorización completa. Además de los elementos aleatorizados por la aleatorización "
                             "conservadora,\n la memoria gestionada a través de brk() se aleatoriza.")
            case default:
                self.alsr = "No se ha obtenido información"
