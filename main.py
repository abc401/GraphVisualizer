from graph.graph import NonDirectedGraph
import pygame
from pygame.locals import *
from app import App

import colors

class GraphVisualizer(App):
    def __init__(self, width: int = 500, height: int = 500, fps: float = 60) -> None:
        super().__init__(width, height, fps)
        self.padding = 50
        self.init_graph()
        
        
    def init_graph(self):
        self.graph = NonDirectedGraph()
        
        self.graph.add_vertices([0, 1, 2, 3, 4, 5])
        self.graph.add_edges((0, 1, "a"), (0, 3, "b"), (0, 4, "b"))
        self.graph.add_edges((1, 5, "a"), (1, 3, "a"), (1, 4, "b"))
        self.graph.add_edges((2, 4, "a"), (2, 5, "b"), (2, 1, "a"))
        
        self.graph.vert_radius = (self.surface.get_width() - self.padding)/(self.graph.n_vertices * 3)
    
    def draw(self):
        self.surface.fill(colors.WHITE)
        self.graph.draw()
    
    def event_handler(self, event):
        return super().event_handler(event)
    
    def update(self, dt):
        return super().update(dt)

if __name__ == "__main__":
    GraphVisualizer().run()
