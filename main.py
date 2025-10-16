import pygame as pg
import sys
from paddles import PlayerPaddle, ComputerPaddle
from ball import Ball
import events


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
BALL_STARTING_SIZE = 10
GAME_BALL = Ball(BALL_STARTING_POS, BALL_STARTING_SPEED, BALL_STARTING_SIZE)

COMPUTER_STARTING_POS = pg.Vector2(
    SCREEN.get_width() - 20,
    SCREEN.get_height() // 2
)
COMPUTER_STARTING_SPEED = 5
COMPUTER_STARTING_SIZE = 50

COMPUTER_PADDLE = ComputerPaddle(COMPUTER_STARTING_POS, COMPUTER_STARTING_SPEED, COMPUTER_STARTING_SIZE)

trail_surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

def fade_ball():
    fade = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)
    fade.fill((0, 0, 0, 50))  # lower alpha = longer trail
    trail_surface.blit(fade, (0, 0))

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Game logic
    PLAYER_PADDLE.move(SCREEN)
    GAME_BALL.check_collisions(SCREEN, PLAYER_PADDLE, COMPUTER_PADDLE)
    GAME_BALL.move()
    COMPUTER_PADDLE.move(GAME_BALL)
    COMPUTER_PADDLE.update_rect()

    # Drawing
    fade_ball()
    GAME_BALL.draw(trail_surface)
    SCREEN.fill(BLACK)
    SCREEN.blit(trail_surface, (0, 0))  # Add the faded trail layer
    PLAYER_PADDLE.draw(SCREEN)
    COMPUTER_PADDLE.draw(SCREEN)

    pg.display.flip()
    CLOCK.tick(FPS)

# Quit pg
pg.quit()
sys.exit()