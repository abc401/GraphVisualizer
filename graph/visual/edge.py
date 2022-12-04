from vertex import Vertex
from pygame import Vector2

class Edge:
    
    def __init__(self, vertex1: Vertex, vertex2: Vertex) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        
        self.p1 = self.vertex1.pos
        self.p2 = self.vertex2.pos
        self.center = (self.p1 + self.p2)/2
        self.offset = 0