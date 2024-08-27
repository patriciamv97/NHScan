import sys

from colorama import Fore


class Menu:
    def __init__(self):
        self.options = None
        self.exit = None

    def show_menu(self):
        print(Fore.MAGENTA + 'Seleccione una opción:')
        for key in self.options:
            print(Fore.LIGHTMAGENTA_EX + f'\t{key}) {Fore.RESET + self.options[key][0]}')

    def read_option(self):
        while (a := input('Opción: ')) not in self.options:
            print(Fore.RED + 'Opción incorrecta, vuelva a intentarlo.')
        return a

    def run_menu(self, opcion):
        self.options[opcion][1]()

    def main_menu(self):
        option = None
        while option != self.exit:
            self.show_menu()
            option = self.read_option()
            self.run_menu(option)
            print()

    @staticmethod
    def exit_program():
        print(Fore.MAGENTA+'¡Saliendo!')
        sys.exit()


