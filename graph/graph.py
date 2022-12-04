import pygame as pg
import colors as clr

class NonDirectedGraph:
    def __init__(
        self,
        surface: pg.Surface,
        vertices: set = set(),
        vert_radius: int = 100,
        edges: dict = dict(),
    ) -> None:
        self.surface = surface
        
        self.vertices = vertices
        self.edges = edges
        
        self.vert_radius = vert_radius
        self.n_vertices = 0
        self.n_edges = 0
    
    def add_edges(self, *edges):
        for edge in edges:
            self.add_edge(*edge)
    
    def add_edge(self, from_vert, to_vert, token):
        self.edges[from_vert][token] = to_vert
        self.edges[to_vert][token] = from_vert
        self.n_edges += 1
    
    def add_vertices(self, vert_names: list):
        for name in vert_names:
            self.add_vertex(name)
    
    def get_vertices(self):
        for vert in self.vertices:
            yield vert
    
    def add_vertex(self, vert_name):
        self.vertices.add(Vertex(vert_name))
        self.edges[vert_name] = dict()
        self.n_vertices += 1
        
    def draw(self) -> None:
        position = pg.Vector2()
        for vert in self.get_vertices():
            vert.pos = position.copy()
            pg.draw.circle(self.surface, clr.BLACK, vert.pos, self.graph.vert_radius)
            position.x += self.graph.vert_radius * 2 + self.graph.vert_radius/3