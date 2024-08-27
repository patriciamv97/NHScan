import platform

if platform.system() == 'Windows':
    from menu.MainMenus.MenuHost.Submenus.Linux.SubMenuPossibleDenfeses import SubMenuPossibleDefenses
    from menu.MainMenus.MenuHost.Submenus.Windows.SubMenuEnviromentalVaribles import SubMenuEnviromentalVariables
    from menu.MainMenus.MenuHost.Submenus.Windows.SubMenuFilesDirecotires import SubMenuFilesDirectories
    from menu.MainMenus.MenuHost.Submenus.Windows.SubMenuNetWork import SubMenuNetWork
    from menu.MainMenus.MenuHost.Submenus.Windows.SubmenuUser import SubMenuUser
else:
    from menu.MainMenus.MenuHost.Submenus.Linux.SubMenuPossibleDenfeses import SubMenuPossibleDefenses
    from menu.MainMenus.MenuHost.Submenus.Linux.SubMenuEnviromentalVaribles import SubMenuEnviromentalVariables
    from menu.MainMenus.MenuHost.Submenus.Linux.SubMenuFilesDirecotires import SubMenuFilesDirectories
    from menu.MainMenus.MenuHost.Submenus.Linux.SubMenuNetWork import SubMenuNetWork
    from menu.MainMenus.MenuHost.Submenus.Linux.SubmenuUser import SubMenuUser

from menu.Menu import Menu
from myhostinformation.HostInfo.Types.Linux.Linux import Linux


class MenuRepository:
    def __init__(self):
        self._main_menu = Menu()
        self._network_menu = None
        self._network_host_menu = None
        self._my_host_menu = None

    def main_menu(self):
        self._main_menu.options = {
            '1': ('Escanear red', self._network_menu.main_menu),
            '2': ('Escanear host', self._network_host_menu.main_menu),
            '3': ('Obtener info de mi host', self._my_host_menu.main_menu),
            '4': ('Salir', self._main_menu.exit_program)
        }
        self._main_menu.exit = 4
        return self._main_menu

    def network_menu(self, network_menu):
        self._network_menu = network_menu
        self._network_menu.exit = 8
        self._network_menu.options = {
            '1': ('Escanear red', self._network_menu.get_network_info),
            '2': ('Obtener interfaces de red', self._network_menu.get_network_interfaces),
            '3': ('Obtener puertas de enlace', self._network_menu.get_gateways),
            '4': ('Obtener servidores DNS', self._network_menu.get_dns),
            '5': ('Obtener servidores DHCP', self._network_menu.get_dhcp),
            '6': ('Obtener hosts en la red', self._network_menu.get_network_hosts),
            '7': ('Menu principal', self._main_menu.main_menu)
        }
        return self

    def network_host_menu(self, network_host_menu):
        self._network_host_menu = network_host_menu
        self._network_host_menu.exit = 7
        self._network_host_menu.options = {
            '1': ('Obtener toda la info del host', self._network_host_menu.get_network_host),
            '2': ('Enumerar servicios en el host', self._network_host_menu.enmu_services),
            '3': ('Obtener todos los puertos abiertos del host', self._network_host_menu.get_open_ports),
            '4': ('Obtener los puertos abiertos comúmes', self._network_host_menu.get_common_open_ports),
            '5': ('Obtener los banners', self._network_host_menu.get_banners),
            '6': ('¿Hay banners vulnerables?', self._network_host_menu.check_vulns),
            '7': ('Menu principal', self._main_menu.main_menu)
        }
        return self

    def my_host_menu(self, my_host_menu, repository):
        self._my_host_menu = my_host_menu
        repository = self.build_submenu_host_repository(repository, my_host_menu)
        self._my_host_menu.exit = 7
        self._my_host_menu.options = {
            '1': ('Información Basica', self._my_host_menu.basic_information),
            '2': ('Usuarios', repository.get_submenu_user().main_menu),
            '3': ('Directorios y ficheros', repository.get_submenu_files_directories().main_menu),
            '4': ('Varibales de entorno', repository.get_submenu_enviromental_variables().main_menu),
            '5': ('NetWork', repository.get_submenu_network().main_menu),
            '6': ('Programas útiles en el sistema', self._my_host_menu.enumerate_useful_programs),
            '7': ('Menu principal', self._main_menu.main_menu),

        }
        return self

    def get_my_host_menu(self):
        return self._my_host_menu

    def build(self):
        if not self._network_host_menu or not self._network_menu or not self._my_host_menu:
            raise ValueError("All dependencies must be provided before building the use case.")
        return self.main_menu()

    @staticmethod
    def build_submenu_host_repository(repository, my_host_menu):
        repository = repository.set_menu_host(my_host_menu).submenu_user(
            SubMenuUser(my_host_menu.host)).submenu_files_directories(
            SubMenuFilesDirectories(my_host_menu.host)).submenu_enviromental_variables(
            SubMenuEnviromentalVariables(my_host_menu.host)).submenu_network(SubMenuNetWork(my_host_menu.host))
        if isinstance(my_host_menu.host, Linux):
            repository.submenu_possible_defenses(SubMenuPossibleDefenses(my_host_menu.host))
        return repository.build()
