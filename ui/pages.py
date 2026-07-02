import pygame
from core.theme import THEME
from ui.widgets.base import ValueWidget

class Page:
    name = "PAGE"
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.widgets = []

    def draw_title(self, surf, title):
        font = pygame.font.SysFont("DejaVu Sans", 22, bold=True)
        surf.blit(font.render(title, True, THEME["line"]), (22, 76))

    def draw(self, surf, bus):
        self.draw_title(surf, self.name)
        for widget in self.widgets:
            widget.draw(surf, bus)

class DashboardPage(Page):
    name = "DASHBOARD"
    def __init__(self, w, h):
        super().__init__(w, h)
        self.widgets = [
            ValueWidget((20, 110, 210, 120), "FART", "speed_kn", "kn", True),
            ValueWidget((250, 110, 210, 120), "KURS", "heading_deg", "°", True),
            ValueWidget((20, 250, 210, 105), "DJUP", "depth_m", "m"),
            ValueWidget((250, 250, 210, 105), "MOTOR", "engine_temp", "°C"),
            ValueWidget((20, 375, 210, 105), "BATTERI", "battery_v", "V"),
            ValueWidget((250, 375, 210, 105), "WIFI", "wifi", ""),
        ]

class NavigationPage(Page):
    name = "NAVIGATION"
    def __init__(self, w, h):
        super().__init__(w, h)
        self.widgets = [
            ValueWidget((20, 115, 440, 90), "GPS", "gps_status"),
            ValueWidget((20, 220, 210, 95), "FART", "speed_kn", "kn"),
            ValueWidget((250, 220, 210, 95), "KURS", "heading_deg", "°"),
            ValueWidget((20, 335, 440, 95), "OPENCPN", "opencpn"),
        ]

class EnginePage(Page):
    name = "MOTOR"
    def __init__(self, w, h):
        super().__init__(w, h)
        self.widgets = [
            ValueWidget((20, 115, 210, 100), "TEMP", "engine_temp", "°C"),
            ValueWidget((250, 115, 210, 100), "VARVTAL", "rpm", "rpm"),
            ValueWidget((20, 235, 210, 100), "LADDNING", "battery_v", "V"),
            ValueWidget((250, 235, 210, 100), "OLJETRYCK", "oil", "OK"),
        ]

class ElectricalPage(Page):
    name = "ELSYSTEM"
    def __init__(self, w, h):
        super().__init__(w, h)
        self.widgets = [
            ValueWidget((20, 115, 210, 100), "STARTBATTERI", "battery_v", "V"),
            ValueWidget((250, 115, 210, 100), "FÖRBRUKNING", "house_v", "V"),
            ValueWidget((20, 235, 210, 100), "GENERATOR", "charge", ""),
            ValueWidget((250, 235, 210, 100), "STRÖM", "amps", "A"),
        ]

class SystemPage(Page):
    name = "SYSTEM"
    def __init__(self, w, h):
        super().__init__(w, h)
        self.widgets = [
            ValueWidget((20, 115, 210, 100), "CPU", "cpu_temp", "°C"),
            ValueWidget((250, 115, 210, 100), "WIFI", "wifi"),
            ValueWidget((20, 235, 440, 100), "OPENCPN", "opencpn"),
        ]
