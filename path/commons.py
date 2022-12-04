from pygame import Vector2

def lerp(p1: Vector2, p2: Vector2, t: float):
    return p1 + (p2 - p1) * t