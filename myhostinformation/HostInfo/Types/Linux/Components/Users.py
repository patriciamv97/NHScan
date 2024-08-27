import os

from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands_user = {
    1: "id -un",  # currentuser
    2: "id",
    3: "who",  # user connected
    4: "grep -VE 'nologin' /etc/passwd",  # Logged in user
    5: "ls -ahlR /root",  # Root directories, permiso de sudo
    6: "ls -ahlR /home/",  # Directorios de usuario
    7: "last",  # Historial usuario
    8: "history 20",  # Historial comandos
    9: "getent group",  # Local group
    10: "awk -F '{print $1}' /etc/passwd",  # Local users
    11: "getent adm",
    # Usuarios autorizados a super usuario
    12: 'getent group sudo',
    13: 'getent group wheel',
    14: 'geten group users'  # Ususarios normales
}


class Users:
    def __init__(self):
        self.users_in_sudo = None
        self.users = None
        self.adm_users = None
        self.local_users = None
        self.local_group = None
        self.user_history = None
        self.user_directories = None
        self.root_directories = None
        self.logged_in_user = None
        self.command_history = None
        self.current_user_groups_pemissions = None
        self.users_connected = None
        self.current_user = None

    def get_current_user(self):
        self.current_user = run_command(commands_user[1].split())

    def get_current_user_groups_pemissions(self):
        self.current_user_groups_pemissions = run_command(commands_user[2].split())

    def get_users_connected(self):
        self.users_connected = run_command(commands_user[3].split())

    def get_user_logged(self):
        self.logged_in_user = run_command(commands_user[4].split())

    def get_root_directories(self):
        try:
            self.root_directories = run_command(commands_user[5].split())
        except:
            print(f"{Fore.RED}[!]Se necesita permiso sudo{Fore.RESET}")

    def get_user_directories(self):
        self.user_directories = run_command(commands_user[6].split())

    def get_user_history(self):
        self.user_history = run_command(commands_user[7].split())

    def get_command_history(self):
        self.command_history = run_command(commands_user[8].split())

    def get_local_group(self):
        self.local_group = run_command(commands_user[9].split())

    def get_local_users(self):
        self.local_users = run_command(commands_user[10].split())

    def get_amd_user(self):
        self.adm_users = run_command(commands_user[11].split())

    def get_users_in_sudo(self):
        try:
            self.users_in_sudo = run_command(commands_user[12].split())
        except:
            try:
                self.users_in_sudo = run_command(commands_user[13].split())
            except:
                print(f"{Fore.RED}Algo ha fallado{Fore.RESET}")

    def get_users(self):
        self.users = run_command(commands_user[14].slpit())
