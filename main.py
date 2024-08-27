from colorama import Fore

from LibModule.constants import Constants
from menu.MainMenus.MenuHost.MenuHost import MenuHost
from menu.MainMenus.MenuNetWork import MenuNetWork
from menu.MainMenus.MenuNetWorkHost import MenuNetWorkHost
from menu.Repositories.MenuRepository import MenuRepository
from menu.Repositories.Submenus.MenuWindowsHostRepository import MenuWindowswindowsRepository
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

    menu_network = MenuNetWork()
    menu_network.set_network(NetWork())

    menu_network_host = MenuNetWorkHost()
    menu_network_host.set_host_in_network(HostInNetwork())

    menu_host = MenuHost()
    menu_host.set_host(Windows())
    submenu = MenuWindowswindowsRepository()
    main_menu = (builder.network_menu(menu_network)
                 .network_host_menu(menu_network_host).my_host_menu(menu_host, submenu).build()).main_menu()
