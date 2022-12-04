import pygame as pg
from pygame import Vector2, Surface, Rect

from dataclasses import dataclass, field

import colors as clr

@dataclass(order=True)
class VertexLabel:
    sort_index: str = field(init=False, repr=False)
    text: str = ''
    image: Surface = None
    rect: Rect = field(init=False)
    
    def __post_init__(self):
        self.sort_index = self.text
        if self.image is None:
            self.image = Surface((0, 0))
        self.rect = self.image.get_rect()
    
class Vertex:
    font = pg.font.SysFont('sans-serif', 10)
    
    def __init__(
        self,
        label: str = '',
        position: Vector2 = Vector2(),
        color: clr.Color = clr.BLACK,
        padding_px: int = 10
    ) -> None:
        self.pos = position
        self.color = color

        if label:
            self.label = VertexLabel(
                label,
                Vertex.font.render(label, True, self.color)
            )
        else:
            self.label = VertexLabel()
        self.padding = padding_px
        
        self.radius = Vector2(self.label.rect.topright).distance_to(self.label.rect.center) + self.padding*2
        self.rect = Rect(
            -self.radius, -self.radius,
            self.radius*2, self.radius*2
        )