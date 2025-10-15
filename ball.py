import pygame as pg

class Ball():
    def __init__(self, pos:pg.Vector2, speed:int, size:int):
        self.pos:pg.Vector2 = pos
        self.velocity = pg.Vector2(speed,-speed)
        self.speed = speed
        self.size = size
        self.rect = pg.Rect(self.pos.x, self.pos.y, size, size)
    
    def update_rect(self):
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)
    
    def move(self):
        self.pos += self.velocity
    
    def update_velocity(self, new_velocity):
        self.velocity = new_velocity    

    def draw(self,screen:pg.Surface):
        center = (int(self.pos.x + self.size / 2), int(self.pos.y + self.size / 2))
        pg.draw.circle(screen, "white", center, self.size)