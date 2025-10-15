import pygame as pg
from ball import Ball


class Paddle:
    def __init__(self, pos:pg.Vector2=pg.Vector2(20,0), speed:int=5, size:int=50) -> None:
        self.pos = pos
        self.speed = speed
        self.size = size #represents height
        self.rect = pg.Rect(self.pos, (10, self.size))
    
    def update_rect(self):
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)
        self.rect.height = self.rect.height
        
    def draw(self,surface:pg.Surface) -> None:
        self.update_rect()
        pg.draw.rect(surface, "white", self.rect)
        
    def update_speed(self, new_speed:int):
        self.speed = new_speed
    
    def update_size(self, new_size:int):
        self.size = new_size

class PlayerPaddle(Paddle):
    def __init__(self, pos:pg.Vector2, speed:int, size:int):
        super().__init__(pos, speed, size)
    
    def move(self, screen:pg.Surface):
        current_pressed = pg.key.get_pressed() #get all pressed keys
        if current_pressed[pg.K_UP]: 
            updated_pos = self.pos - pg.Vector2(0,self.speed) #move paddle pos up
        elif current_pressed[pg.K_DOWN]:
            updated_pos = self.pos + pg.Vector2(0,self.speed) #move paddle pos down
        else:
            return None #if the player didn't press either, don't continue
        
        if updated_pos.y < 0: #check if new pos too high
            updated_pos = pg.Vector2(self.pos.x, 0) #cap height
        if updated_pos.y > screen.get_height() - self.rect.height: #check if new pos too low
            updated_pos = pg.Vector2(self.pos.x, screen.get_height() - self.rect.height) #set height lower limit
        
        self.pos = updated_pos #after all checks and final pos given, update the player pos
        
class ComputerPaddle(Paddle):
    def __init__(self, pos:pg.Vector2, speed:int, size:int):
        super().__init__(pos, speed, size)
    
    def move(self, ball:Ball):
        y_dist = ball.rect.y - self.rect.y
        if abs(y_dist) < self.speed:
            self.rect.y = int(ball.pos.y)
        
        