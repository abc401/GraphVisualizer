import pygame as pg
import colors as clr

class Vertex:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pos = pg.Vector2()