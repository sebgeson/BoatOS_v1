import time
from config import BOAT_NAME
from themes import current as theme
from widgets.primitives import round_rect


def draw(draw, width, voltage, cpu_temp, fps):
    draw.rectangle((0, 0, width, 40), fill=theme.HEADER)
    draw.line((0, 39, width, 39), fill=theme.HEADER_LINE, width=1)

    draw.text((10, 10), "BOATOS", fill=theme.CYAN)
    draw.text((78, 10), BOAT_NAME, fill=theme.WHITE)

    round_rect(draw, (235, 7, 286, 31), radius=7, fill=theme.CARD2, outline=theme.BORDER)
    draw.text((244, 13), f"{cpu_temp:.0f}C", fill=theme.MUTED)

    round_rect(draw, (292, 7, 352, 31), radius=7, fill=theme.CARD2, outline=theme.BORDER)
    draw.text((302, 13), f"{fps}FPS", fill=theme.MUTED)

    round_rect(draw, (358, 7, 416, 31), radius=7, fill=theme.CARD2, outline=theme.BORDER)
    draw.text((368, 13), f"{voltage:.1f}V", fill=theme.GREEN)

    draw.text((426, 13), time.strftime("%H:%M"), fill=theme.WHITE)
