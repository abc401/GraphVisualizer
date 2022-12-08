# from graph.visual.vertex import Vertex
from pygame import Vector2, Surface, draw, Rect
from math import radians

class ArcPath:
    """
    This class will be called through the Edge class. This class is basically just a wrapper class
    for an arc that goes from the center of one vertex to the center of another vertex.It can be
    used to graphically represent the edges of a graph.
    """
    
    def __init__(self, end1: Vector2, offset: Vector2, end2: Vector2) -> None:
        self.end1 = end1
        self.off = offset
        self.end2 = end2
        

        self.calc_vals()
    
    def calc_vals(self):
        
        x21 = self.off.x - self.end1.x
        x23 = self.off.x - self.end2.x
        # sx21 = pos2.x ** 2 - pos1.x ** 2
        # sx23 = pos2.x ** 2 - pos3.x ** 2
        
        ms1 = self.end1.magnitude_squared()
        ms2 = self.off.magnitude_squared()
        ms3 = self.end2.magnitude_squared()
        
        y21 = self.off.y - self.end1.y
        y32 = self.end2.y - self.off.y
        # sy21 = pos2.y ** 2 - pos1.y ** 2
        # sy23 = pos2.y ** 2 - pos3.y ** 2
        
        center_x = (y32/(2*(x21*y32 + x23*y21))) * (ms2 - ms1 + (ms2 - ms3) * (y21 / y32))
        
        # Center of the circle that the arc is a part of
        self.center = Vector2(
            center_x,
            (ms3 - ms2 + 2*x23*center_x)/(2*y32)
        )
        self.radius = self.center.distance_to(self.end1)
        self.calc_rect()
    
    def calc_rect(self):
        self.rect = Rect(
            self.center - (self.radius, self.radius),
            (self.radius*2, self.radius*2)
        )
        
    
    def update(self, pos: Vector2):
        self.off = pos
        self.calc_vals()
        
        
    def draw(self, surface: Surface):
        pointr = 4
        draw.circle(surface, (0,0,0), self.end1, pointr, 1)
        draw.circle(surface, (0,0,0), self.end2, pointr, 1)
        draw.circle(surface, (0,0,0), self.off, pointr, 1)
        
        # draw.circle(surface, (0,0,0), self.center, self.radius, 1)
        print(self.rect)
        draw.arc(
            surface, (0,0,0),
            self.rect,
            radians(self.center.angle_to(self.end1)),
            radians(self.center.angle_to(self.end2))
        )
        # draw.rect(surface, (0,0,0), self.rect, 1)
        draw.circle(surface, (0,0,255), self.center, 2)