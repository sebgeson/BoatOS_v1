import pygame

class Fonts:
    def __init__(self):
        pygame.font.init()
        self.small = pygame.font.SysFont("dejavusans", 18)
        self.normal = pygame.font.SysFont("dejavusans", 24)
        self.large = pygame.font.SysFont("dejavusans", 42, bold=True)
        self.huge = pygame.font.SysFont("dejavusans", 82, bold=True)
        self.title = pygame.font.SysFont("dejavusans", 30, bold=True)


def text(surface, font, value, pos, color, center=False):
    img = font.render(str(value), True, color)
    rect = img.get_rect()
    rect.center = pos if center else rect.center
    if not center:
        rect.topleft = pos
    surface.blit(img, rect)


def card(surface, rect, title, value, unit, theme, fonts):
    pygame.draw.rect(surface, theme.card, rect, border_radius=18)
    pygame.draw.rect(surface, theme.accent, rect, 2, border_radius=18)
    x, y, w, h = rect
    text(surface, fonts.normal, title, (x+18, y+14), theme.muted)
    text(surface, fonts.large, value, (x+w//2, y+h//2+12), theme.text, center=True)
    if unit:
        text(surface, fonts.normal, unit, (x+w-55, y+h-40), theme.muted)


def topbar(surface, bus, theme, fonts, width):
    pygame.draw.rect(surface, theme.panel, (0, 0, width, 68))
    text(surface, fonts.title, "BoatOS", (22, 17), theme.text)
    text(surface, fonts.normal, "HERWA23", (160, 22), theme.accent)
    text(surface, fonts.small, f"GPS {bus.data['gps']}", (width-405, 15), theme.muted)
    text(surface, fonts.small, f"WiFi {bus.data['wifi']}", (width-405, 39), theme.good)
    text(surface, fonts.title, f"{bus.data['battery_v']}V", (width-140, 17), theme.text)
