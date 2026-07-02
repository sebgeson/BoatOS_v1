from config import THEME

if THEME == "day":
    from themes import day as current
else:
    from themes import dark as current
