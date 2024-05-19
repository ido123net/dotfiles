import os
import random

WALLPEPERS_PATH = os.path.expanduser("~/Wallpapers")


def get_wallpapers() -> list[str]:
    if not os.path.exists(WALLPEPERS_PATH):
        return []

    return sorted(
        [
            os.path.join(WALLPEPERS_PATH, p)
            for p in os.listdir(WALLPEPERS_PATH)
            if p.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    )


def get_random_wallpaper() -> str | None:
    wallpapers = get_wallpapers()
    return random.choice(wallpapers) if wallpapers else None
