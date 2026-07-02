import os
import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CONTROL_WIDTH, CONTROL_HEIGHT, FPS
from core.databus import DataBus
from ui.theme import Theme
from ui.widgets import Fonts
from ui.pages import draw_page, PAGES
from control.panel import ControlPanel


def main():
    pygame.init()
    bus = DataBus()
    main_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("BoatOS HDMI Main UI")
    fonts = Fonts()
    panel = ControlPanel(bus, fonts)
    clock = pygame.time.Clock()
    running = True

    # Controlpanelen renderas som en yta. På Pi kan den skickas till separat framebuffer senare.
    control_surface = pygame.Surface((CONTROL_WIDTH, CONTROL_HEIGHT))
    show_control_preview = True

    while running:
        bus.update_mock()
        theme = Theme(bus.night_mode, bus.dimmed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1: bus.set_page("dashboard")
                elif event.key == pygame.K_2: bus.set_page("navigation")
                elif event.key == pygame.K_3: bus.set_page("motor")
                elif event.key == pygame.K_4: bus.set_page("el")
                elif event.key == pygame.K_5: bus.set_page("larm")
                elif event.key == pygame.K_n: bus.toggle_night()
                elif event.key == pygame.K_d: bus.toggle_dim()
                elif event.key == pygame.K_TAB: show_control_preview = not show_control_preview
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Om kontrollpanelens preview syns nere till höger kan den klickas även på HDMI.
                if show_control_preview:
                    px = WINDOW_WIDTH - CONTROL_WIDTH - 18
                    py = WINDOW_HEIGHT - CONTROL_HEIGHT - 18
                    mx, my = event.pos
                    if px <= mx <= px+CONTROL_WIDTH and py <= my <= py+CONTROL_HEIGHT:
                        panel.handle_pos((mx-px, my-py))

        draw_page(main_screen, bus, theme, fonts)
        panel.draw(control_surface, theme)
        if show_control_preview:
            px = WINDOW_WIDTH - CONTROL_WIDTH - 18
            py = WINDOW_HEIGHT - CONTROL_HEIGHT - 18
            pygame.draw.rect(main_screen, theme.panel, (px-6, py-6, CONTROL_WIDTH+12, CONTROL_HEIGHT+12), border_radius=12)
            main_screen.blit(control_surface, (px, py))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
