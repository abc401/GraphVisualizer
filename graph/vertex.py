import pygame as pg
from pygame import Vector2, Surface, Rect

from dataclasses import dataclass, field

import colors as clr

@dataclass(order=True, frozen=True)
class VertexLabel:
    sort_index: str = field(init=False)
    text: str
    image: Surface
    rect: Rect = field(init=False)
    
    def __post_init__(self):
        self.sort_index = self.text
        self.rect = self.image.get_rect()
    
class Vertex:
    font = pg.font.SysFont('sans-serif', 10)
    
    def __init__(
        self,
        label: str,
        position: Vector2 = Vector2(),
        color: clr.Color = clr.BLACK,
        padding_px: int = 10
    ) -> None:
        self.pos = position
        self.label = VertexLabel(
            label,
            Vertex.font.render(label, antialias=True, color=self.color)
        )
        self.color = color
        self.padding = padding_px
        self.radius = Vector2(self.rect.topright).distance_to(self.rect.center) + self.padding
        self.rect = Rect(
            -self.radius, -self.radius,
            self.radius*2, self.radius*2
        )