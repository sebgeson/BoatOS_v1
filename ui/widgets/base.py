import pygame
from core.theme import THEME

class Widget:
    def __init__(self, rect, title=""):
        self.rect = pygame.Rect(rect)
        self.title = title

    def draw_panel(self, surf):
        pygame.draw.rect(surf, THEME["panel"], self.rect, border_radius=14)
        pygame.draw.rect(surf, THEME["line"], self.rect, 2, border_radius=14)
        if self.title:
            font = pygame.font.SysFont("DejaVu Sans", 18, bold=True)
            surf.blit(font.render(self.title, True, THEME["muted"]), (self.rect.x + 14, self.rect.y + 10))

class ValueWidget(Widget):
    def __init__(self, rect, title, key, suffix="", big=False):
        super().__init__(rect, title)
        self.key = key
        self.suffix = suffix
        self.big = big

    def draw(self, surf, bus):
        self.draw_panel(surf)
        value = bus.get(self.key, "--")
        size = 54 if self.big else 30
        font = pygame.font.SysFont("DejaVu Sans", size, bold=True)
        text = f"{value} {self.suffix}".strip()
        img = font.render(text, True, THEME["text"])
        surf.blit(img, (self.rect.x + 16, self.rect.y + self.rect.h - img.get_height() - 18))
