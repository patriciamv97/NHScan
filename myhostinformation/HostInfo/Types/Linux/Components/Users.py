import os

from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands_user = {
    1: "id -un",  # currentuser
    2: "id",
    3: "who",  # user connected
    4: "grep -vE 'nologin' /etc/passwd",  # Logged in user
    5: "ls -ahlR /root",  # Root directories, permiso de sudo
    6: "ls -ahlR /home/",  # Directorios de usuario
    7: "last",  # Historial usuario
    8: "history 20",  # Historial comandos
    9: "getent group",  # Local group
    10: "awk -F : '{print $1}' /etc/passwd",  # Local users
    11: "getent group adm",
    # Usuarios autorizados a super usuario
    12: 'getent group sudo',
    13: 'getent group wheel',
    14: 'getent group users'  # Ususarios normales
}


class Users:
    def __init__(self):
        self.users_in_sudo = None
        self.users = None
        self.adm_users = None
        self.local_users = None
        self.local_groups = None
        self.user_history = None
        self.user_directories = None
        self.root_directories = None
        self.logged_in_user = None
        self.command_history = None
        self.current_user_groups_pemissions = None
        self.users_connected = None
        self.current_user = None

    def get_current_user(self):
        self.current_user = run_command(commands_user[1])

    def get_current_user_groups_pemissions(self):
        self.current_user_groups_pemissions = run_command(commands_user[2])

    def get_users_connected(self):
        self.users_connected = run_command(commands_user[3])

    def get_user_logged(self):
        self.logged_in_user = run_command(commands_user[4])

    def get_root_directories(self):
        try:
            self.root_directories = run_command(commands_user[5])
        except:
            print(f"{Fore.RED}[!]Se necesita permiso sudo{Fore.RESET}")

    def get_user_directories(self):
        self.user_directories = run_command(commands_user[6])

    def get_user_history(self):
        self.user_history = run_command(commands_user[7])

    def get_command_history(self):
        try:
            history_file = os.path.expanduser('~/.zsh_history')
            with open(history_file, 'r') as file:
                history = file.readlines()
                self.command_history = history
        except Exception as e:
            print(f"{Fore.RED}[!]No se pudo obtener el historial{Fore.RESET}\n{e}")

    def get_local_groups(self):
        self.local_groups = run_command(commands_user[9])

    def get_local_users(self):
        self.local_users = run_command(commands_user[10])

    def get_adm_users(self):
        self.adm_users = run_command(commands_user[11])

    def get_users_in_sudo(self):
        try:
            self.users_in_sudo = run_command(commands_user[12])
        except:
            try:
                self.users_in_sudo = run_command(commands_user[13])
            except:
                print(f"{Fore.RED}Algo ha fallado{Fore.RESET}")

    def get_users(self):
        self.users = run_command(commands_user[14])
