import subprocess

from LibModule.Loader import Loader
from LibModule.informationgatheringfunctions.OSFunctions.WindowsFunctions import run_powershell_command, run_command

commands_file_directories = {
    1: "Get-ChildItem -Path C:\\ -Include *unattend*, *sysprep*, -File -Recurse -ErrorAction SilentlyContinue "
       "| where {$_.Name -like '*.xml' -or $_.Name -like '*.txt' -or $_.Name -like '*.ini'} ",
    2: "dir C:\\Users\\%username% *.xml /s/b",
    3: "dir C:\\Windows\\ *.ini /s/b",
    4: "dir /s/b *.config",
    5: "dir C:\\ *.log /s/b",
    6: "dir /s *pass* == *cred* == *vcn* == *.config*",
    7: "findstr /si pass *.xml *.ini *.txt *.config",
    8: "dir /a:h \\",
    9: "dir /a:h \\Users",
    10: "dir /a:h \\Users\\%username%"
}


class FilesDirectories:

    def __init__(self):
        self.hidden_files_in_root = None
        self.hidden_files_in_user = None
        self.hidden_files_in_users = None
        self.passwords = None
        self.interesting_files = None
        self.logs = None
        self.config_files = None
        self.init_files = None
        self.unattended_files = None
        self.xml_files = None

    def get_unattended_files(self):
        loader = Loader("Loading...", "", 0.05).start()
        unattended_files, returncode = run_powershell_command(commands_file_directories[1])
        loader.stop()
        self.unattended_files = unattended_files

    def get_extension_files_xml(self):
        self.xml_files = (run_command(commands_file_directories[2]))

    def get_extenision_files_ini(self):
        self.init_files = (run_command(commands_file_directories[3]))

    def get_extension_files_conf(self):
        self.config_files = (run_command(commands_file_directories[4]))

    def get_logs(self):
        self.logs = run_command(commands_file_directories[5])

    def get_interesting_files(self):
        self.interesting_files = run_command(commands_file_directories[6])

    def get_find_password(self):
        self.passwords = run_command(commands_file_directories[7])

    def get_hidden_files_in_root(self):
        self.hidden_files_in_root = run_command(commands_file_directories[8])

    def get_hidden_files_in_users(self):
        self.hidden_files_in_users = run_command(commands_file_directories[9])

    def get_hidden_files_in_user(self):
        self.hidden_files_in_users = run_command(commands_file_directories[10])