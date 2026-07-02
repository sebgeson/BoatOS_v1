from ui.core.widget import Widget
from themes import current as theme


class InfoBox(Widget):
    def __init__(self, x, y, width, height, title, value_func, color=None):
        super().__init__(x, y, width, height)
        self.title = title
        self.value_func = value_func
        self.color = color or theme.GREEN

    def draw(self, draw, data):
        value = self.value_func(data)
        draw.rectangle(
            (self.x, self.y, self.x + self.width, self.y + self.height),
            outline=theme.WHITE,
            width=2
        )
        draw.text((self.x + 10, self.y + 8), self.title, fill=theme.WHITE)
        draw.text((self.x + 10, self.y + 34), value, fill=self.color)
