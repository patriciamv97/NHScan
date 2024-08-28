import os

from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command

commands_user = {
    # Directivas de grupo
    1: "gpresult /scope user /v",
    2: "gpresult /scope computer /v",  # Sólo con permiso de administrador
    # HostInfo
    3: "Write-Host $env:UserDomain\\$env:UserName",  # Current user
    4: "Start-Process 'qwinsta' -NoNewWindow -Wait | ft",  # Logged in user
    5: "Get-ChildItem C:\\Users | ft Name",  # User directories
    6: "Get-LocalGroup | ft Name",  # Grupos Locales
    7: "Get-LocalUser | ft Name, Enabled, LastLogon",  # Usuarios Locales
    # Uusarios del grupo administradores  tiene en cuenta el idioma del so
    8: "Get-LocalGroupMember Administradores | ft Name , PrincipalSource",
    9: "Get-LocalGroupMember Administrators | ft Name , PrincipalSource",
    # Uusarios del grupo escritorio remoto se tiene en cuenta el idioma del so
    10: "Get-LocalGroupMember 'Usuarios de escritorio remoto' | ft Name , PrincipalSource",
    11: "Get-LocalGroupMember 'Remote Desktop HostInfo' | ft Name , PrincipalSource",
    # Inicios de sesión de usuario se tiene en cuenta el idioma del so
    12: 'Wevtutil qe security /q:"*[System[EventID=4624]]" /f:text /rd:true /c:10 | findstr /C:"Date:" '
        '/C:"Nombre de'
        'cuenta"',
    13: 'Wevtutil qe security /q:"*[System[EventID=4624]]" /f:text /rd:true /c:10 | findstr /C:"Date:" '
        '/C:"Account Name"',
    14: 'cmdkey /list'  # Creendenciales almacenadas en la actualidad
}


class Users:
    def __init__(self):
        self.currently_stored_history = ""
        self.user_login_history = ""
        self.remote_desktop_users = ""
        self.administrators = ""
        self.local_users = ""
        self.local_groups = ""
        self.user_directory = ""
        self.logged_in_user = ""
        self.gpo_user = ""
        self.gpo_computer = ""
        self.powershell_history = ""
        self.current_user = ""

    def get_gpo_user(self):
        gpo_user, returncode = run_powershell_command(commands_user[1])
        if returncode == 0:
            self.gpo_user = gpo_user

    def get_gpo_computer(self):
        print(f"{Fore.YELLOW}[!]Sólo con permiso de administrador")
        gpo_computer, returncode = run_powershell_command(commands_user[2])
        if returncode != 0:
            print(f"{Fore.YELLOW}[!]Debes ser administrador para ejecutar este comando.")
        self.gpo_computer = gpo_computer

    def get_powershell_history(self):
        history_file = os.path.expandvars(
            r"%USERPROFILE%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt")

        if os.path.exists(history_file):
            with open(history_file, "r") as file:
                history = file.readlines()
            self.powershell_history = history
        else:
            print("No se encontró el archivo de historial de PowerShell.")

    def get_current_user(self):
        user, returncode = run_powershell_command(commands_user[3])
        if returncode == 0:
            self.current_user = user

    def get_logged_in_user(self):
        logged_in_user, returncode = run_powershell_command(commands_user[4])
        if returncode == 0:
            self.logged_in_user = logged_in_user

    def get_user_directory(self):
        user_directory, returncode = run_powershell_command(commands_user[5])
        if returncode == 0:
            self.user_directory = user_directory

    def get_local_groups(self):
        local_groups, returncode = run_powershell_command(commands_user[6])
        if returncode == 0:
            self.local_groups = local_groups

    def get_local_users(self):
        local_users, returncode = run_powershell_command(commands_user[7])
        if returncode == 0:
            self.local_users = local_users

    def get_administrators(self):
        admin, returncode = run_powershell_command(commands_user[9])
        if returncode != 0:
            admin, returncode = run_powershell_command(commands_user[8])
        self.administrators = admin

    def get_remote_desktop_user(self):
        users, returncode = run_powershell_command(commands_user[11])
        if returncode != 0:
            users, returncode = run_powershell_command(commands_user[10])
        self.remote_desktop_users = users

    def get_user_login_history(self):
        history, returncode = run_powershell_command(commands_user[13])
        if returncode != 0:
            history, returncode = run_powershell_command(commands_user[12])
        self.user_login_history = history

    def get_currently_stored_creendentials(self):
        currently_stored_history, returncode = run_powershell_command(commands_user[14])
        if returncode == 0:
            self.currently_stored_history = currently_stored_history

    def __str__(self):
        return (
                Fore.LIGHTMAGENTA_EX + 'Obtener directivas de grupo\n\n' + Fore.RESET + self.gpo_user + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Obtener directivas de la máquina\n\n' + Fore.RESET + self.gpo_computer + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Usuario actual\n\n' + Fore.RESET + self.current_user + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Historial de PowerShell\n\n' + Fore.RESET + str(self.powershell_history) + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Historial de incio de sesón del usuario\n\n' + Fore.RESET
                + self.user_login_history + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Usuarios del grupo Escritorio remoto\n\n' + Fore.RESET
                + self.remote_desktop_users + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Directorios del usuario\n\n' + Fore.RESET + self.user_directory + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Usuarios con sesión\n\n' + Fore.RESET + self.logged_in_user + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Usuarios locales\n\n' + Fore.RESET + self.local_users + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Grupos locales\n\n' + Fore.RESET + self.local_groups + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Administradores\n\n' + Fore.RESET + self.administrators + "\n" +
                Fore.LIGHTMAGENTA_EX + 'Historial actual de creendenciales\n\n' + Fore.RESET
                + self.currently_stored_history
        )
