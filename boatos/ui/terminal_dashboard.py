import os


class TerminalDashboard:
    def __init__(self, bus, config):
        self.bus = bus
        self.config = config

    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")

    def draw_card(self, title, value, unit=""):
        text = f"{value} {unit}".strip()
        print("┌──────────────────────────────┐")
        print(f"│ {title:<14} {text:>13} │")
        print("└──────────────────────────────┘")

    def render(self):
        snap = self.bus.snapshot()
        g = self.bus.get

        self.clear()
        boat_name = self.config.get("boat_name", "BOAT")
        print("════════════════════════════════")
        print(f" BOATOS              {boat_name}")
        print("════════════════════════════════")
        print(f" GPS: {g('gps.status', '--')}   WiFi: {g('system.wifi', '--')}")
        print(f" CPU: {g('system.cpu_temp_c', '--')}°C  OpenCPN: {g('system.opencpn', '--')}")
        print("────────────────────────────────")

        self.draw_card("FART", g("nav.speed_kn", "--"), "kn")
        self.draw_card("KURS", g("nav.course_deg", "--"), "°")
        self.draw_card("POSITION", g("nav.position", "--"))
        self.draw_card("MOTORTEMP", g("engine.temp_c", "--"), "°C")
        self.draw_card("STARTBATT", g("battery.start_v", "--"), "V")
        self.draw_card("FÖRBR.BATT", g("battery.house_v", "--"), "V")

        print("────────────────────────────────")
        print(" Sidor: DASHBOARD | NAV | MOTOR | EL | SYSTEM")
        print(" Ctrl+C för att avsluta")
