import pygame as pg
import sys
from paddles import PlayerPaddle
from ball import Ball

# Initialize pg
pg.init()

# Game Setup
WIDTH, HEIGHT = 800, 600
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rogue Pong")

CLOCK = pg.time.Clock()
FPS = 60

# Colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Game object setup
PLAYER_STARTING_POS:pg.Vector2 = pg.Vector2(
    25,
    SCREEN.get_height()//2
)
PLAYER_STARTING_SPEED = 5
PLAYER_STARTING_HEIGHT = 50
PLAYER_PADDLE = PlayerPaddle(PLAYER_STARTING_POS, PLAYER_STARTING_SPEED, PLAYER_STARTING_HEIGHT)

BALL_STARTING_POS:pg.Vector2 = pg.Vector2(
    SCREEN.get_width()//2,
    SCREEN.get_height()//2
)
BALL_STARTING_SPEED = 5
BALL_STARTING_SIZE = 5
GAME_BALL = Ball(BALL_STARTING_POS, BALL_STARTING_SPEED, BALL_STARTING_SIZE)

# Game loop
running = True
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Game logic 
    PLAYER_PADDLE.move(SCREEN)
    GAME_BALL.update_rect()
    GAME_BALL.move()
    
    # Drawing
    SCREEN.fill(BLACK) 
    PLAYER_PADDLE.draw(SCREEN)
    GAME_BALL.draw(SCREEN)

    # Update the display
    pg.display.flip()  # or pg.display.update()

    # Control frame rate
    CLOCK.tick(FPS)

# Quit pg
pg.quit()
sys.exit()