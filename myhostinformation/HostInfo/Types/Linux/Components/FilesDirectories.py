from LibModule.informationgatheringfunctions.OSFunctions.LinuxFunctions import run_command

commands_file_directories = {
    1: "find / -perm -u=s -type f",
    2: "find / -perm -g=s -type f",
    3: "find / -path /proc -prune -o -perm -0002 -type f",  #
    4: "find /var/log -name '*.log' | xargs -l10 egrep 'pwd|password'",
    5: "find /etc -name '*.c*' 2>/dev/null | xargs  egrep 'pwd|password' 2>/dev/null",
    6: "find / -perm -1000 -type d",
    7: "find / -perm -0002 -type d",
    8: "find / -path /proc -prune -o -writable",
}


class FilesDirectories:

    def __init__(self):
        self.misconfiguration_files_suid = None
        self.writable_for_current_user = None
        self.global_files_without_proc = None
        self.logs_with_passwords = None
        self.configurations_files_with_password = None
        self.sticky_bits = None
        self.writable_folders = None
        self.writable_files_for_current_user = None

    def get_misconfiguration_files_suid(self):
        suid = run_command(commands_file_directories[1])
        if suid:
            self.misconfiguration_files_suid = suid
        guid = run_command(commands_file_directories[2])
        if guid:
            self.misconfiguration_files_suid += guid

    def get_global_files_without_proc(self):
        self.global_files_without_proc = run_command(commands_file_directories[3])

    def get_logs_with_passwords(self):
        self.logs_with_passwords = run_command(commands_file_directories[4])

    def get_configurations_files_with_password(self):
        self.configurations_files_with_password = run_command(commands_file_directories[5])

    def get_sticky_bits(self):
        self.sticky_bits = run_command(commands_file_directories[6])

    def get_writable_folders(self):
        self.writable_folders = run_command(commands_file_directories[7])

    def get_writable_files_for_current_user(self):
        self.writable_for_current_user = run_command(commands_file_directories[8])
