from PIL import Image, ImageDraw

from themes import current as theme
from widgets import statusbar, infobox, horizon


def draw_dashboard(device, data):
    img = Image.new("RGB", device.size, theme.BG)
    draw = ImageDraw.Draw(img)

    w, h = device.size

    roll = data["roll"]
    pitch = data["pitch"]

    voltage = data.get("battery", {}).get("voltage", 12.8)
    cpu = data.get("system", {}).get("cpu_temp", 0.0)
    fps = data.get("system", {}).get("fps", 0)

    statusbar.draw(draw, w, voltage, cpu, fps)
    horizon.draw(draw, w, h, roll, pitch)

    draw.rectangle((0, 230, w, h), fill=theme.PANEL)

    infobox.draw(draw, 8, 242, 148, 68, "KRANGNING", f"{roll:5.1f}°", theme.GREEN)
    infobox.draw(draw, 166, 242, 148, 68, "STAMPNING", f"{pitch:5.1f}°", theme.GREEN)
    infobox.draw(draw, 324, 242, 148, 68, "BATTERI", f"{voltage:.1f} V", theme.GREEN)

    return img
