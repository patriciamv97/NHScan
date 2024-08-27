from menu.Menu import Menu


class MenuHost(Menu):
    def __init__(self):
        super().__init__()
        self.submenu_users = None
        self.host = None

    def set_host(self, host):
        self.host = host

