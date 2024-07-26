import platform
import psutil as ps


class MyHost:
    def __init__(self):
        self.machine = platform.uname().machine
        self.release = platform.release()
        self.processor = platform.processor()
        self.operative_system = platform.uname().system
        self.node = platform.node()
        self.users = ps.users()
        #interface

    def __str__(self):
        return (self.node + " " + self.operative_system + ", " + self.machine + ", " + self.release
                + ", " + self.processor)
