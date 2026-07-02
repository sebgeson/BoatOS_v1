from PIL import Image, ImageDraw
import time
from themes import current as theme
from config import BOAT_NAME
from widgets.primitives import round_rect


def draw_startup(device):
    img = Image.new("RGB", device.size, theme.BG)
    draw = ImageDraw.Draw(img)
    w, h = device.size
    cx = w // 2

    draw.rectangle((0, 0, w, h), fill=theme.BG)
    round_rect(draw, (55, 60, 425, 260), radius=18, fill=theme.CARD, outline=theme.BORDER, width=2)

    draw.text((cx - 52, 92), "BoatOS", fill=theme.CYAN)
    draw.text((cx - 82, 126), BOAT_NAME, fill=theme.WHITE)
    draw.text((cx - 105, 158), "MARINE COMPUTER", fill=theme.MUTED)

    draw.rectangle((95, 215, 385, 230), outline=theme.BORDER, width=2)

    for i in range(0, 286, 18):
        draw.rectangle((97, 217, 97 + i, 228), fill=theme.CYAN)
        device.display(img)
        time.sleep(0.035)

    draw.text((cx - 44, 238), "STARTAR...", fill=theme.WHITE)
    device.display(img)
    time.sleep(0.5)
