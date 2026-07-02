from themes import current as theme


def round_rect(draw, xy, radius=10, fill=None, outline=None, width=1):
    try:
        draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)
    except Exception:
        draw.rectangle(xy, fill=fill, outline=outline, width=width)


def gradient_vertical(draw, xy, top, bottom):
    x1, y1, x2, y2 = [int(v) for v in xy]
    height = max(1, y2 - y1)
    for y in range(y1, y2):
        t = (y - y1) / height
        r = int(top[0] * (1 - t) + bottom[0] * t)
        g = int(top[1] * (1 - t) + bottom[1] * t)
        b = int(top[2] * (1 - t) + bottom[2] * t)
        draw.line((x1, y, x2, y), fill=(r, g, b))


def centered_text(draw, box, text, fill):
    x1, y1, x2, y2 = box
    try:
        bbox = draw.textbbox((0, 0), text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
    except Exception:
        tw, th = draw.textsize(text)
    draw.text((x1 + (x2-x1-tw)//2, y1 + (y2-y1-th)//2), text, fill=fill)
