class Theme:
    def __init__(self, night=False, dimmed=False):
        if night:
            self.bg = (5, 0, 0)
            self.panel = (28, 8, 8)
            self.card = (45, 12, 12)
            self.text = (255, 205, 160)
            self.muted = (170, 90, 70)
            self.accent = (255, 65, 35)
            self.good = (80, 220, 120)
            self.warn = (255, 180, 50)
        else:
            self.bg = (5, 11, 20)
            self.panel = (10, 24, 42)
            self.card = (14, 35, 60)
            self.text = (230, 245, 255)
            self.muted = (110, 145, 175)
            self.accent = (0, 190, 255)
            self.good = (80, 230, 140)
            self.warn = (255, 190, 50)
        self.dim_overlay = (0, 0, 0, 130 if dimmed else 0)
