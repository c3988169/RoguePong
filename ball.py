import pygame as pg
import random
import events

class Ball():
    def __init__(self, pos:pg.Vector2, speed:int, size:int):
        self.pos:pg.Vector2 = pos #top left
        self.velocity = pg.Vector2(speed,-speed)
        self.speed = speed
        self.size = size
        self.rect = pg.Rect(self.pos.x, self.pos.y, size, size)
    
    def draw_trail(self, screen:pg.Surface, fade=40):
        s = pg.Surface(screen.get_size(), pg.SRCALPHA)  # transparent surface
        s.fill((0, 0, 0, fade))  # black with alpha for fade strength
        screen.blit(s, (0, 0))
    
    def update_rect(self):
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)
    
    def move(self):
        self.pos += self.velocity
        self.update_rect()
    
    def update_velocity(self, new_velocity:pg.Vector2):
        self.velocity = new_velocity    

    def draw(self,screen:pg.Surface):
        center = (int(self.pos.x + self.size / 2), int(self.pos.y + self.size / 2))
        pg.draw.circle(screen, "white", center, self.size)
    
    def get_center_pos(self):
        return pg.Vector2(
            self.pos.x + self.size/2,
            self.pos.y + self.size/2
                          )

    def collision_with_paddle(self):
        self.update_velocity( 
                pg.Vector2(
                    -self.velocity.x,
                    -self.velocity.y
                )
            )
    
    def collision_with_top_or_bottom(self):
        self.update_velocity( 
                pg.Vector2(
                    self.velocity.x,
                    -self.velocity.y
                )
            )
    
    def player_loss(self):
        pg.event.post(pg.event.Event(events.PLAYER_LOSS_EVENT))

    def check_collisions(self, screen:pg.Surface, player_paddle, computer_paddle): 
        if self.rect.top <= 0: #colliding with top wall
            self.collision_with_top_or_bottom()
            return False

        if self.rect.bottom >= screen.get_height(): #colliding with bottom wall
            self.collision_with_top_or_bottom()
            

        if self.rect.colliderect(player_paddle.rect):
            self.collision_with_paddle()
            

        if self.rect.colliderect(computer_paddle.rect):
            self.collision_with_paddle()
            
        
        if self.rect.left <= 0: #colliding with left wall
            self.player_loss()

        
        
