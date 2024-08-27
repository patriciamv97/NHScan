from menu.Repositories.MenuRepository import MenuRepository


class MenuWindowsHostRepository(MenuRepository):
    def __init__(self):
        super().__init__()
        self._menu_host = None
        self._submenu_user = None
        self._submenu_file_directories = None
        self._submenu_enviromental_variables = None
        self._submenu_network = None
        self._submenu_programs = None

    def set_menu_host(self, menu_host):
        self._menu_host = menu_host
        return self

    def submenu_user(self, submenu_user):
        self._submenu_user = submenu_user
        self._submenu_user.exit = 13
        self._submenu_user.options = {
            '1': ('Obtener directivas de grupo', self._submenu_user.gpo_user),
            '2': ('Obtener directivas de la máquina', self._submenu_user.gpo_computer),
            '3': ('Usuario actual', self._submenu_user.get_current_user),
            '4': ('Historial de PowerShell', self._submenu_user.get_powershell_history),
            '5': ('Historial de incio de sesón del usuario', self._submenu_user.get_user_login_history),
            '6': ('Usuarios del grupo Escritorio remoto', self._submenu_user.get_remote_desktop_user),
            '7': ('Directorios del usuario', self._submenu_user.get_user_directory),
            '8': ('Usuarios con sesión', self._submenu_user.get_logged_in_user),
            '9': ('Usuarios locales', self._submenu_user.get_local_users),
            '10': ('Grupos locales', self._submenu_user.get_local_groups),
            '11': ('Administradores', self._submenu_user.get_administrators),
            '12': ('Historial actual de creendenciales', self._submenu_user.get_currently_stored_creendentials),
            '13': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_files_directories(self, submenu_file_directories):
        self._submenu_file_directories = submenu_file_directories
        self._submenu_file_directories.exit = 11
        self._submenu_file_directories.options = {
            '1': ('Obtener archivos desatendidos', self._submenu_file_directories.get_unattended_files),
            '2': ('Archivos con extensión xml', self._submenu_file_directories.get_extension_files_xml),
            '3': ('Archivos con extensión ini', self._submenu_file_directories.get_extenision_files_ini),
            '4': ('Archivos de configuración', self._submenu_file_directories.get_extension_files_conf),
            '5': ('Logs', self._submenu_file_directories.get_logs),
            '6': ('Otros archivos interesantes', self._submenu_file_directories.get_interesting_files),
            '7': ('Obtener contraseñas', self._submenu_file_directories.get_find_password),
            '8': ('Archivos ocultos en la raiz', self._submenu_file_directories.get_hidden_files_in_root),
            '9': ('Archivos ocultos en Users', self._submenu_file_directories.get_hidden_files_in_users),
            '10': ('Archivos ocultos en el usuario actual', self._submenu_file_directories.get_hidden_files_in_user),
            '11': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_enviromental_variables(self, submenu_enviromental_variables):
        self._submenu_enviromental_variables = submenu_enviromental_variables
        self._submenu_enviromental_variables.exit = 3
        self._submenu_enviromental_variables.options = {
            '1': ('Obtener las varibles de entorno', self._submenu_enviromental_variables.enviromental_variables),
            '2': ('Obtener contraseñas en los registros', self._submenu_enviromental_variables.password_in_reg),
            '3': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_network(self, submenu_network):
        self._submenu_network = submenu_network
        self._submenu_network.exit = 5
        self._submenu_network.options = {
            '1': ('Obtener la tabla de ruta', self._submenu_network.route_table),
            '2': ('Obtener los drivers conectados', self._submenu_network.conected_drivers),
            '3': ('Obtener las conexiones de red', self._submenu_network.network_connections),
            '4': ('Obtener las reglas del firewall', self._submenu_network.firewall_rules),
            '5': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def get_submenu_user(self):
        return self._submenu_user

    def get_submenu_files_directories(self):
        return self._submenu_file_directories

    def get_submenu_network(self):
        return self._submenu_network

    def get_submenu_enviromental_variables(self):
        return self._submenu_enviromental_variables

    def build(self):
        if (not self._submenu_user or not self._submenu_file_directories or not self._submenu_network):
            raise ValueError("All dependencies must be provided before building the use case.")
        return self
