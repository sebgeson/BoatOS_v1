import time
from config import BOAT_NAME
from themes import current as theme


def draw(draw, width, voltage, cpu_temp, fps):
    draw.rectangle((0, 0, width, 38), fill=theme.HEADER)
    draw.text((10, 10), f"BoatOS - {BOAT_NAME}", fill=theme.WHITE)
    draw.text((245, 10), f"{cpu_temp:.0f}C", fill=theme.WHITE)
    draw.text((305, 10), f"{fps} FPS", fill=theme.WHITE)
    draw.text((370, 10), f"{voltage:.1f}V", fill=theme.GREEN)
    draw.text((425, 10), time.strftime("%H:%M"), fill=theme.WHITE)
