from pygame import Vector2, Surface, Color, draw
from path.commons import lerp

class CubicBezier:
    def __init__(
        self,
        start: Vector2,
        p1: Vector2,
        p2: Vector2,
        end: Vector2,
        color: Color,
        steps: int = 150
    ) -> None:
        self.start = start
        self.p1 = p1
        self.p2 = p2
        self.end = end
        self.color = color
        self.steps = steps
    
    def calculate(self, time: float):
        lerp_s_1 = lerp(self.start, self.p1, time)
        lerp_1_2 = lerp(self.p1, self.p2, time)
        lerp_2_e = lerp(self.p2, self.end, time)
        lerp_s_1_2 = lerp(lerp_s_1, lerp_1_2, time)
        lerp_1_2_e = lerp(lerp_1_2, lerp_2_e, time)
        return lerp(lerp_s_1_2, lerp_1_2_e, time)
        
    
    def draw(self, surface: Surface):
        t = 0
        step = 1/self.steps
        previous = self.calculate(t)
        while t < 1:
            t += step
            current = self.calculate(t)
            draw.line(surface, self.color, previous, current)
            previous = current
    
        current = self.calculate(1)
        draw.line(surface, self.color, previous, current)

    
if __name__ == '__main__':
    CubicBezier(Vector2(),Vector2(),Vector2(),Vector2(),).draw(Surface((0,0)))
        