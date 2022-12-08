# from graph.graph import NonDirectedGraph
# from path.cubicbezier import CubicBezier
from path.arcpath import ArcPath
import pygame
from pygame.locals import *
from app import App
from math import radians

import colors as clr

# class GraphVisualizer(App):
#     def __init__(self, width: int = 500, height: int = 500, fps: float = 60) -> None:
#         super().__init__(width, height, fps)
#         self.padding = 50
#         self.init_graph()
        
        
#     def init_graph(self):
#         self.graph = NonDirectedGraph()
        
#         self.graph.add_vertices([0, 1, 2, 3, 4, 5])
#         self.graph.add_edges((0, 1, "a"), (0, 3, "b"), (0, 4, "b"))
#         self.graph.add_edges((1, 5, "a"), (1, 3, "a"), (1, 4, "b"))
#         self.graph.add_edges((2, 4, "a"), (2, 5, "b"), (2, 1, "a"))
        
#         self.graph.vert_radius = (self.surface.get_width() - self.padding)/(self.graph.n_vertices * 3)
    
#     def draw(self):
#         self.surface.fill(colors.WHITE)
#         self.graph.draw()
    
#     def event_handler(self, event):
#         return super().event_handler(event)
    
#     def update(self, dt):
#         return super().update(dt)

# class Bezier(App):
#     def __init__(self, width: int = 500, height: int = 500, fps: float = 60) -> None:
#         super().__init__(width, height, fps)
#         self.bezier = CubicBezier(
#             pygame.Vector2(10, 10),
#             pygame.Vector2(480, 10),
#             pygame.Vector2(480, 10),
#             pygame.Vector2(480, 480),
#             clr.BLACK
#         )
    
#     def draw(self):
#         self.surface.fill(clr.WHITE)
#         self.bezier.draw(self.surface)
    
#     def event_handler(self, event):
#         super().event_handler(event)
    
#     def update(self, dt):
#         super().update(dt)

class Bezier(App):
    def __init__(self, width: int = 500, height: int = 500, fps: float = 60) -> None:
        super().__init__(width, height, fps)

        v1 = pygame.Vector2(200, 100)
        v2 = pygame.Vector2(300, 100)
        offset = pygame.Vector2(250, 150)
        self.arc = ArcPath(v1, offset, v2)
        
    
    def draw(self):
        self.surface.fill(clr.WHITE)
        self.arc.draw(self.surface)
        # self.running = False
    
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.arc.update(pygame.Vector2(pygame.mouse.get_pos()))
    
    def update(self, dt):
        super().update(dt)


class A(App):
    def __init__(self, width: int = 500, height: int = 500, fps: float = 60) -> None:
        super().__init__(width, height, fps)

        self.rect = pygame.Rect(50, 50, 100, 100)
        p1 = pygame.Vector2(200, 10)
        p2 = pygame.Vector2()
        
    
    def draw(self):
        self.surface.fill(clr.WHITE)
        # pygame.draw.rect(self.surface, (0,0,0), self.rect, 1)
        pygame.draw.arc(self.surface, clr.BLACK, self.rect, radians(90), radians(360))
        # self.running = False
    
    def event_handler(self, event):
        pass
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # self.arc.update(pygame.Vector2(pygame.mouse.get_pos()))
    
    def update(self, dt):
        super().update(dt)
    
        

if __name__ == "__main__":
    # GraphVisualizer().run()
    # Bezier().run()
    A().run()
