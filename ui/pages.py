import pygame
from ui.widgets import card, text, topbar

PAGES = ["dashboard", "navigation", "motor", "el", "larm"]
PAGE_TITLES = {
    "dashboard": "Dashboard",
    "navigation": "Navigation",
    "motor": "Motor",
    "el": "Elsystem",
    "larm": "Larmcentral",
}


def draw_page(surface, bus, theme, fonts):
    w, h = surface.get_size()
    surface.fill(theme.bg)
    topbar(surface, bus, theme, fonts, w)
    page = bus.page
    text(surface, fonts.title, PAGE_TITLES.get(page, page), (28, 86), theme.text)

    if page == "dashboard":
        text(surface, fonts.huge, f"{bus.data['speed_kn']:.1f}", (w//2, 180), theme.text, center=True)
        text(surface, fonts.title, "knop", (w//2, 245), theme.muted, center=True)
        card(surface, (35, 330, 215, 150), "Kurs", f"{bus.data['heading']}°", "", theme, fonts)
        card(surface, (275, 330, 215, 150), "Djup", f"{bus.data['depth_m']:.1f}", "m", theme, fonts)
        card(surface, (515, 330, 215, 150), "Motor", f"{bus.data['engine_temp']}°", "C", theme, fonts)
        card(surface, (755, 330, 215, 150), "Batteri", f"{bus.data['battery_v']}", "V", theme, fonts)
    elif page == "navigation":
        card(surface, (35, 140, 290, 150), "Fart", f"{bus.data['speed_kn']:.1f}", "kn", theme, fonts)
        card(surface, (365, 140, 290, 150), "Kurs", f"{bus.data['heading']}°", "", theme, fonts)
        card(surface, (695, 140, 290, 150), "GPS", bus.data['gps'], "", theme, fonts)
        card(surface, (35, 330, 455, 150), "Position", "INGEN FIX", "", theme, fonts)
        card(surface, (530, 330, 455, 150), "OpenCPN", bus.data['opencpn'], "", theme, fonts)
    elif page == "motor":
        card(surface, (35, 140, 290, 150), "Motortemp", f"{bus.data['engine_temp']}", "°C", theme, fonts)
        card(surface, (365, 140, 290, 150), "Varvtal", "----", "rpm", theme, fonts)
        card(surface, (695, 140, 290, 150), "Laddning", f"{bus.data['battery_v']}", "V", theme, fonts)
        card(surface, (35, 330, 455, 150), "Oljetryck", "OK", "", theme, fonts)
        card(surface, (530, 330, 455, 150), "Drifttid", f"{bus.data['runtime_h']}", "h", theme, fonts)
    elif page == "el":
        card(surface, (35, 140, 290, 150), "Startbatteri", f"{bus.data['battery_v']}", "V", theme, fonts)
        card(surface, (365, 140, 290, 150), "Förbrukning", "12.4", "V", theme, fonts)
        card(surface, (695, 140, 290, 150), "Generator", "VÄNTAR", "", theme, fonts)
        card(surface, (35, 330, 455, 150), "Landström", "AV", "", theme, fonts)
        card(surface, (530, 330, 455, 150), "Total ström", "--", "A", theme, fonts)
    elif page == "larm":
        alerts = ["Ingen GPS-fix", "OpenCPN ej ansluten", "Motortemp OK", "Batterispänning OK"]
        y = 145
        for a in alerts:
            color = theme.warn if "Ingen" in a or "ej" in a else theme.good
            pygame.draw.rect(surface, theme.card, (55, y, w-110, 70), border_radius=14)
            pygame.draw.circle(surface, color, (85, y+35), 11)
            text(surface, fonts.normal, a, (115, y+22), theme.text)
            y += 88

    if bus.dimmed:
        overlay = pygame.Surface((w,h), pygame.SRCALPHA)
        overlay.fill(theme.dim_overlay)
        surface.blit(overlay, (0,0))
