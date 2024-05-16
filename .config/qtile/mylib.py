import os
import random


WALLPEPERS_PATH = os.path.expanduser("~/Wallpapers")


def get_wallpepers() -> list[str]:
    return [
        os.path.join(WALLPEPERS_PATH, p)
        for p in os.listdir(WALLPEPERS_PATH)
        if p.lower().endswith((".png", ".jpg", ".jpeg"))
    ]


def get_random_wallpaper(wallpepers: list[str]) -> str | None:
    return random.choice(wallpepers) if wallpepers else None
