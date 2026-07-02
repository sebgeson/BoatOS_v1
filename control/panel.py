import pygame
from ui.pages import PAGES, PAGE_TITLES
from ui.widgets import text

class ControlPanel:
    def __init__(self, bus, fonts):
        self.bus = bus
        self.fonts = fonts
        self.buttons = []

    def draw(self, surface, theme):
        w, h = surface.get_size()
        surface.fill(theme.bg)
        text(surface, self.fonts.title, "BoatOS Kontroll", (18, 12), theme.text)
        self.buttons = []
        labels = [
            ("dashboard", "HEM"), ("navigation", "NAV"),
            ("motor", "MOTOR"), ("el", "EL"),
            ("larm", "LARM"), ("night", "NATT"),
            ("dim", "DIM"), ("ack", "KVITTERA")
        ]
        x, y = 18, 60
        bw, bh, gap = 135, 56, 12
        for i, (action, label) in enumerate(labels):
            col = i % 3
            row = i // 3
            rect = pygame.Rect(x + col*(bw+gap), y + row*(bh+gap), bw, bh)
            active = action == self.bus.page or (action == "night" and self.bus.night_mode) or (action == "dim" and self.bus.dimmed)
            color = theme.accent if active else theme.card
            pygame.draw.rect(surface, color, rect, border_radius=12)
            pygame.draw.rect(surface, theme.text, rect, 1, border_radius=12)
            text(surface, self.fonts.normal, label, rect.center, theme.text, center=True)
            self.buttons.append((rect, action))
        text(surface, self.fonts.small, f"Aktiv sida: {PAGE_TITLES.get(self.bus.page)}", (18, h-34), theme.muted)

    def handle_pos(self, pos):
        for rect, action in self.buttons:
            if rect.collidepoint(pos):
                if action in PAGES:
                    self.bus.set_page(action)
                elif action == "night":
                    self.bus.toggle_night()
                elif action == "dim":
                    self.bus.toggle_dim()
                return True
        return False
