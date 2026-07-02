from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class SystemScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 80, 200, 62, "CPU", lambda d: f"{d.get('system', {}).get('cpu_temp', 0):.1f} C", theme.CYAN))
        self.add(InfoBox(260, 80, 200, 62, "FPS", lambda d: f"{d.get('system', {}).get('fps', 0)}", theme.GREEN))
        self.add(InfoBox(20, 160, 200, 62, "BATTERI", lambda d: f"{d.get('battery', {}).get('voltage', 0):.1f} V", theme.GREEN))
        self.add(InfoBox(260, 160, 200, 62, "IMU", lambda d: "OK" if d.get("imu_ok") else "FEL", theme.GREEN))
        self.add(InfoBox(20, 240, 440, 62, "LOGG", lambda d: "logs/boatos.log", theme.MUTED))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 50), "SYSTEM", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
