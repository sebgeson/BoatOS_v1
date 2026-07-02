from ui.core.widget import Widget
from themes import current as theme
from widgets.primitives import round_rect


class InfoBox(Widget):
    def __init__(self, x, y, width, height, title, value_func, color=None, subtitle=None):
        super().__init__(x, y, width, height)
        self.title = title
        self.value_func = value_func
        self.color = color or theme.GREEN
        self.subtitle = subtitle

    def draw(self, draw, data):
        value = self.value_func(data)

        round_rect(
            draw,
            (self.x, self.y, self.x + self.width, self.y + self.height),
            radius=10,
            fill=theme.CARD,
            outline=theme.BORDER,
            width=1
        )

        draw.text((self.x + 10, self.y + 8), self.title, fill=theme.MUTED)
        draw.text((self.x + 10, self.y + 32), value, fill=self.color)

        draw.line(
            (self.x + 8, self.y + self.height - 8, self.x + self.width - 8, self.y + self.height - 8),
            fill=theme.HEADER_LINE,
            width=1
        )
