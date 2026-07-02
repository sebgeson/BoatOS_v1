from PIL import Image, ImageDraw

from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar, horizon


class DashboardV2(Screen):
    def __init__(self):
        super().__init__()

        self.add(
            InfoBox(
                8, 242, 148, 68,
                "KRANGNING",
                lambda data: f"{data['roll']:5.1f}°"
            )
        )

        self.add(
            InfoBox(
                166, 242, 148, 68,
                "STAMPNING",
                lambda data: f"{data['pitch']:5.1f}°"
            )
        )

        self.add(
            InfoBox(
                324, 242, 148, 68,
                "BATTERI",
                lambda data: f"{data.get('battery', {}).get('voltage', 0):.1f} V"
            )
        )

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)

        w, h = device.size

        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        horizon.draw(draw, w, h, data["roll"], data["pitch"])

        draw.rectangle((0, 230, w, h), fill=theme.PANEL)

        self.draw_widgets(draw, data)

        return img