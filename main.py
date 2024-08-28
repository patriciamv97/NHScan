from datetime import datetime

from colorama import Fore

from LibModule.constants import Constants
from Report.PDFGenerator import PDFGenerator
from menu.MainMenus.MenuHost.MenuHost import MenuHost
from menu.MainMenus.MenuNetWork import MenuNetWork
from menu.MainMenus.MenuNetWorkHost import MenuNetWorkHost
from menu.Repositories.MenuRepository import MenuRepository
from menu.Repositories.Submenus.MenuLinuxHostRepository import MenuLinuxHostRepository
from menu.Repositories.Submenus.MenuWindowsHostRepository import MenuWindowsHostRepository
from myhostinformation.HostInfo.Types.Linux.Linux import Linux
from myhostinformation.HostInfo.Types.Windows.Windows import Windows
from myhostinformation.MyHost import MyHost
from networkInformation.NetWork import NetWork
from networkInformation.hosts.HostInNetWork import HostInNetwork


def display_banner():
    banner = ("\n" +
              r"     .-') _  ('-. .-.  .-')                ('-.         .-') _      .-') _   ('-.  _  .-')" "\n"
              r"    ( OO ) )( OO )  / ( OO ).             ( OO ).-.    ( OO ) )    ( OO ) )_(  OO)( \( -O )" "\n"
              r",--./ ,--,' ,--. ,--.(_)---\_)   .-----.  / . --. /,--./ ,--,' ,--./ ,--,'(,------.,------." "\n"
              r"|   \ |  |\ |  | |  |/    _ |   '  .--./  | \-.  \ |   \ |  |\ |   \ |  |\ |  .---'|   /`. '" "\n"
              r"|    \|  | )|   .|  |\  :` `.   |  |('-..-'-'  |  ||    \|  | )|    \|  | )|  |    |  /  | |" "\n"
              r"|  .     |/ |       | '..`''.) /_) |OO  )\| |_.'  ||  .     |/ |  .     |/(|  '--. |  |_.' |" "\n"
              r"|  |\    |  |  .-.  |.-._)   \ ||  |`-'|  |  .-.  ||  |\    |  |  |\    |  |  .--' |  .  '.'" "\n"
              r"|  | \   |  |  | |  |\       /(_'  '--'\  |  | |  ||  | \   |  |  | \   |  |  `---.|  |\  \ " "\n"
              r"`--'  `--'  `--' `--' `-----'    `-----'  `--' `--'`--'  `--'  `--'  `--'  `------'`--' '--' ")

    print("%s" % banner)
    print("\n", "NHScanner: ", Constants.__version__)
    print("\n" + "|" + "-" * 100 + "|", end="\n\n")
    print(
        "[!]INFORMACIÓN : \n"
        "Para calcular el cdir de tu red puedes hacerlo en : \n" +
        Constants.__enlace_cdir__)
    print("\n" + "|" + "-" * 100 + "|", end="\n\n")
    print(Fore.LIGHTWHITE_EX + "INFORMACIÓN DEL HOST")
    host = MyHost()
    print(host.__str__())
    print("\n" + "|" + "-" * 100 + "|", end="\n\n")


if __name__ == "__main__":
    display_banner()

    builder = MenuRepository()

    network = NetWork()
    menu_network = MenuNetWork()
    menu_network.set_network(network)

    host_in_network = HostInNetwork()
    menu_network_host = MenuNetWorkHost()
    menu_network_host.set_host_in_network(host_in_network)

    menu_host = MenuHost()
    if MyHost().operative_system == "Windows":
        host = Windows()
        menu_host.set_host(host)
        submenu = MenuWindowsHostRepository()
    else:
        host = Linux()
        menu_host.set_host(host)
        submenu = MenuLinuxHostRepository()

    report = PDFGenerator()
    nombre = "informe"+str(datetime.now().timestamp())+".pdf"
    report.set_file_info(nombre)
    report.set_data([network, host_in_network, host])
    builder.set_report(report)

    main_menu = (builder.network_menu(menu_network)
                 .network_host_menu(menu_network_host).my_host_menu(menu_host, submenu).build()).main_menu()
