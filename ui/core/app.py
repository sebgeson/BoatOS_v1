import time


class App:
    def __init__(self, device):
        self.device = device
        self.screens = {}
        self.active_screen = None
        self.start_time = time.time()

    def add_screen(self, name, screen):
        self.screens[name] = screen

        if self.active_screen is None:
            self.active_screen = name

    def set_screen(self, name):
        if name in self.screens:
            self.active_screen = name

    def render(self, data):
        if self.active_screen is None:
            return None

        return self.screens[self.active_screen].render(self.device, data)