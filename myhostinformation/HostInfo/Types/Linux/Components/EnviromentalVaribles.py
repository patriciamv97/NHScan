import subprocess


class EnviromentalVaribles:
    def __init__(self):
        self.enviromental_variables = ""

    def get_enviromental_variables(self):
        try:
            result = subprocess.run(['set'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        except FileNotFoundError:
            result = subprocess.run(['env'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

        self.enviromental_variables = result
