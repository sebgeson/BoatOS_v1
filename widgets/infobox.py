from themes import current as theme


def draw(draw, x, y, w, h, title, value, color=None):
    if color is None:
        color = theme.GREEN

    draw.rectangle((x, y, x + w, y + h), outline=theme.WHITE, width=2)
    draw.text((x + 10, y + 8), title, fill=theme.WHITE)
    draw.text((x + 10, y + 34), value, fill=color)
