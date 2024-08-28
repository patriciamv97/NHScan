from colorama import Fore

from menu.MainMenus.MenuHost.MenuHost import MenuHost


class SubMenuPossibleDefenses(MenuHost):
    def __init__(self, host):
        super().__init__()
        self.host = host

    def get_apparmor(self):
        if not self.host.possible_defenses.apparmor:
            self.host.possible_defenses.get_apparmor()
        print(
                f"{Fore.MAGENTA}AppArmor{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[!]Es un módulo de seguridad del kernel Linux que permite al "
                f"administrador del \nsistema restringir las capacidades de un programa{Fore.RESET}")
        print(self.host.possible_defenses.apparmor)

    def get_grsecurity(self):
        if not self.host.possible_defenses.grsecurity:
            self.host.possible_defenses.get_grsecurity()
        print(
                f"{Fore.MAGENTA}Grsecurity{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[!]Es un conjunto de parches para el "
                f"kernel de Linux que incluye"
                f"características de seguridad\navanzadas, como protecciones contra escalada de privilegios y "
                f"mitigación de exploits{Fore.RESET}")
        print(self.host.possible_defenses.grsecurity)

    def get_exec_shield(self):
        if not self.host.possible_defenses.exec_shield:
            self.host.possible_defenses.get_exec_shield()
        print(
                f"{Fore.MAGENTA}Execshield{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[!]Es una característica de seguridad "
                f"del kernel de Linux que"
                f"protege contra ataques de \ndesbordamiento de búfer y otros tipos de vulnerabilidades de ejecución "
                f"de código.{Fore.RESET}")
        print(self.host.possible_defenses.exec_shield)

    def get_pax(self):
        if not self.host.possible_defenses.pax:
            self.host.possible_defenses.get_pax()
        print(
                f"{Fore.MAGENTA}PaX{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[!]Es un parche del núcleo Linux que implementa protecciones del mínimo "
                f"privilegio para las páginas de memoria{Fore.RESET}")
        print(self.host.possible_defenses.pax)

    def get_selinux(self):
        if not self.host.possible_defenses.selinux:
            self.host.possible_defenses.get_selinux()
        print(
                f"{Fore.MAGENTA}SElinux{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[!]Es un mecanismo de control de acceso "
                f"obligatorio (MAC)"
                f"implementado en el núcleo de Linux.\nProporciona políticas de seguridad mejoradas mediante el "
                f"etiquetado de los recursos del sistema y la imposición de reglas de acceso.{Fore.RESET}")
        print(self.host.possible_defenses.selinux)

    def get_alsr(self):
        if not self.host.possible_defenses.alsr:
            self.host.possible_defenses.get_aslr()
        print(
                f"{Fore.MAGENTA}ASLR{Fore.RESET}{Fore.LIGHTMAGENTA_EX}\n[!]Es una técnica de seguridad que ayuda a "
                f"prevenir ataques de"
                f"explotación al aleatorizar\nla ubicación en la memoria de áreas clave del sistema, como la pila, "
                f"la biblioteca de enlaces dinámicos y el montón.{Fore.RESET}")
        print(self.host.possible_defenses.alsr)
