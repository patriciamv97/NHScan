from menu.Repositories.MenuRepository import MenuRepository


class MenuWindowswindowsRepository(MenuRepository):
    def __init__(self):
        super().__init__()
        self._menu_host = None
        self._submenu_user = None
        self._submenu_file_directories = None
        self._submenu_enviromental_variables = None
        self._submenu_network = None
        self._submenu_programs = None
        self._submenu_possible_defenses = None

    def set_menu_host(self, menu_host):
        self._menu_host = menu_host
        return self

    def submenu_possible_defenses(self, submenu_possible_defenses):
        self._submenu_possible_defenses = submenu_possible_defenses
        self._submenu_possible_defenses.exit = 8
        self._submenu_possible_defenses.options = {
            '1': ('AppArmor', self._submenu_possible_defenses.get_apparmor),
            '2': ('Grsecurity', self._submenu_possible_defenses.get_grsecurity),
            '3': ('Execshield', self._submenu_possible_defenses.get_exec_shield),
            '4': ('PaX', self._submenu_possible_defenses.get_pax),
            '6': ('SElinux', self._submenu_possible_defenses.get_selinux),
            '7': ('ASLR', self._submenu_possible_defenses.get_alsr),
            '8': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_user(self, submenu_user):
        self._submenu_user = submenu_user
        self._submenu_user.exit = 14
        self._submenu_user.options = {
            '1': ('Usuario actual', self._submenu_user.get_current_user),
            '2': ('Permisos y grupos del usuario actual', self._submenu_user.get_current_user_groups_pemissions),
            '3': ('Usuarios conectados', self._submenu_user.get_users_connected),
            '4': ('Historial de comandos', self._submenu_user.get_command_history),
            '6': ('Directorios de root', self._submenu_user.get_root_directories),
            '7': ('Directorios del usuario', self._submenu_user.get_user_directory),
            '8': ('Usuarios con sesión', self._submenu_user.get_user_logged),
            '9': ('Usuarios locales', self._submenu_user.get_local_users),
            '10': ('Grupos locales', self._submenu_user.get_local_groups),
            '11': ('Administradores', self._submenu_user.get_administrators),
            '12': ('Usuarios con permiso sudo', self._submenu_user.get_users_in_sudo),
            '13': ('Usuarios', self._submenu_user.get_users),
            '14': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_files_directories(self, submenu_file_directories):
        self._submenu_file_directories = submenu_file_directories
        self._submenu_file_directories.exit = 11
        self._submenu_file_directories.options = {
            '1': (
                'Archivos con configuración incorrecta',
                self._submenu_file_directories.get_misconfiguration_files_suid),
            '2': ('Archivos con escritura para el usuario actual',
                  self._submenu_file_directories.get_writable_for_current_user),
            '3': ('Archivos globales sin incluir archivos virtuales',
                  self._submenu_file_directories.get_global_files_without_proc),
            '4': ('Logs con contraseña', self._submenu_file_directories.get_logs_with_passwords),
            '5': ('Archivos de configuración con contraseña',
                  self._submenu_file_directories.get_configurations_files_with_password),
            '6': ('Sticky bits', self._submenu_file_directories.get_sticky_bits),
            '7': ('Obtener directorios con permiso de escritura', self._submenu_file_directories.get_writable_folders),
            '8': ('Obtener directorios con permiso de escritura para el usuario actual',
                  self._submenu_file_directories.get_writable_files_for_current_user),
            '9': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_enviromental_variables(self, submenu_enviromental_variables):
        self._submenu_enviromental_variables = submenu_enviromental_variables
        self._submenu_enviromental_variables.exit = 2
        self._submenu_enviromental_variables.options = {
            '1': ('Obtener las varibles de entorno', self._submenu_enviromental_variables.enviromental_variables),
            '3': ('Menu Host', self._menu_host.main_menu)
        }
        return self

    def submenu_network(self, submenu_network):
        self._submenu_network = submenu_network
        self._submenu_network.exit = 7
        self._submenu_network.options = {
            '1': ('Obtener la tabla de ruta', self._submenu_network.route_table),
            '2': ('Obtener los drivers conectados', self._submenu_network.conected_drivers),
            '3': ('Obtener las conexiones de red', self._submenu_network.network_connections),
            '4': ('Obtener las reglas del firewall', self._submenu_network.firewall_rules),
            '5': ('Obtener lista de discos y particiones disponibles',
                  self._submenu_network.get_list_of_available_disks_and_partitions),
            '6': ('Obtener archivos abiertos relacionados con conexiones de red',
                  self._submenu_network.get_open_files_related_to_network_connections),
            '7': ('Menu Host', self._menu_host.main_menu)
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

    def get_submenu_possible_defenses(self):
        return self._submenu_possible_defenses

    def build(self):
        if (not self._submenu_user or not self._submenu_file_directories or not self._submenu_network
                or not self._submenu_possible_defenses):
            raise ValueError("All dependencies must be provided before building the use case.")
        return self
