import os
import sys
import pygame
from core.databus import DataBus
from core.theme import THEME
from sensors.mock import MockSensors
from ui.pages import DashboardPage, NavigationPage, EnginePage, ElectricalPage, SystemPage

WIDTH = int(os.environ.get("BOATOS_WIDTH", "480"))
HEIGHT = int(os.environ.get("BOATOS_HEIGHT", "640"))
FPS = 60

class BoatOSApp:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("BoatOS v1")
        flags = 0
        if os.environ.get("BOATOS_FULLSCREEN") == "1":
            flags = pygame.FULLSCREEN
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        self.clock = pygame.time.Clock()
        self.bus = DataBus()
        self.sensors = MockSensors(self.bus)
        self.sensors.start()
        self.pages = [
            DashboardPage(WIDTH, HEIGHT),
            NavigationPage(WIDTH, HEIGHT),
            EnginePage(WIDTH, HEIGHT),
            ElectricalPage(WIDTH, HEIGHT),
            SystemPage(WIDTH, HEIGHT),
        ]
        self.page_index = 0
        self.running = True
        self.nav_rects = []

    def next_page(self):
        self.page_index = (self.page_index + 1) % len(self.pages)

    def prev_page(self):
        self.page_index = (self.page_index - 1) % len(self.pages)

    def handle_click(self, pos):
        for i, rect in enumerate(self.nav_rects):
            if rect.collidepoint(pos):
                self.page_index = i

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RIGHT:
                    self.next_page()
                elif event.key == pygame.K_LEFT:
                    self.prev_page()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)

    def draw_header(self):
        pygame.draw.rect(self.screen, (3, 10, 24), (0, 0, WIDTH, 64))
        pygame.draw.line(self.screen, THEME["line"], (0, 64), (WIDTH, 64), 2)
        title_font = pygame.font.SysFont("DejaVu Sans", 22, bold=True)
        small_font = pygame.font.SysFont("DejaVu Sans", 16, bold=True)
        self.screen.blit(title_font.render("BOATOS", True, THEME["line"]), (18, 18))
        self.screen.blit(title_font.render("HERWA23", True, THEME["text"]), (150, 18))
        temp = self.bus.get("engine_temp", "--")
        volt = self.bus.get("battery_v", "--")
        self.screen.blit(small_font.render(f"{temp}°C", True, THEME["text"]), (325, 22))
        self.screen.blit(small_font.render(f"{volt}V", True, THEME["text"]), (390, 22))

    def draw_nav(self):
        names = [p.name for p in self.pages]
        self.nav_rects = []
        y = HEIGHT - 62
        margin = 8
        btn_w = (WIDTH - margin * (len(names)+1)) // len(names)
        font = pygame.font.SysFont("DejaVu Sans", 13, bold=True)
        for i, name in enumerate(names):
            x = margin + i * (btn_w + margin)
            rect = pygame.Rect(x, y, btn_w, 46)
            self.nav_rects.append(rect)
            color = THEME["panel2"] if i == self.page_index else THEME["panel"]
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            pygame.draw.rect(self.screen, THEME["line"], rect, 2 if i == self.page_index else 1, border_radius=10)
            label = name[:7]
            img = font.render(label, True, THEME["text"])
            self.screen.blit(img, img.get_rect(center=rect.center))

    def draw(self):
        self.screen.fill(THEME["bg"])
        self.draw_header()
        self.pages[self.page_index].draw(self.screen, self.bus)
        self.draw_nav()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    BoatOSApp().run()
