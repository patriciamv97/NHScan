from colorama import Fore

from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command

commands_enviromental_variables = {
    1: "reg query HKLM /f password /t REG_SZ /s",
    2: "reg query HKCU /f password /t REG_SZ /s",
    3: "Get-ChildItem Env:* | Select-Object -Property Name,Value"
}


class EnviromentalVaribles:
    def __init__(self):
        self.enviromental_variables = ""
        self.passwords = ""

    def get_enviromental_variables(self):
        enviromental_variables, returncode = run_powershell_command(commands_enviromental_variables[3])
        if returncode == 0:
            self.enviromental_variables = enviromental_variables

    def get_password_in_reg(self):
        password_in_reg_hklm, returncode_hklm = run_powershell_command(commands_enviromental_variables[1])
        password_in_reg_hcku, returncode_hcku = run_powershell_command(commands_enviromental_variables[2])
        if returncode_hcku == 0 and returncode_hklm == 0:
            self.passwords = (f"{Fore.MAGENTA}Registros en HKCU:{Fore.RESET} \n{password_in_reg_hcku}\n\n{Fore.MAGENTA}"
                              f"Registros en HKLM:{Fore.RESET} \n{password_in_reg_hklm}\n\n")

    def __str__(self):
        return (
                Fore.MAGENTA + "Todas las variables:\n\n" + Fore.RESET
                + self.enviromental_variables + "\n\n" +
                Fore.MAGENTA + "Contraseñas en los registros:\n\n" + Fore.RESET
                + self.enviromental_variables.__str__() + "\n\n")

