import os

import pygame

from constants.constants import *

auxDirectory = os.path.join(os.path.dirname(__file__), '..', 'assets')

smallfont = None
score1, score2 = 0, 0

# Sound globals.
paddleHit = None
goal_whistle = None
backgroundMusic = None
mute = False

# image for mute and unmute
mute_image = pygame.image.load(os.path.join(auxDirectory, 'mute.png'))
unmute_image = pygame.image.load(os.path.join(auxDirectory, 'unmute.png'))

play_image = pygame.image.load(os.path.join(auxDirectory, 'play.png'))
pause_image = pygame.image.load(os.path.join(auxDirectory, 'pause.png'))

info_image = pygame.image.load(os.path.join(auxDirectory, "info.png"))

# game globals.
clock = None
screen = None

# timer globals
timer = None

# width and height of the screen.
width, height = WIDTH, HEIGHT

# button constants
buttonRadius = 60
squareSide = 80

# color globals
# (dimgreen, green) , (dimred, red) , (dimblue, blue ) , (yellow, dimyellow), (orange, dimorange)
colors = [
    [(28, 170, 156), (54, 204, 191)],  # Vibrant teal and bright aqua
    [(255, 69, 85), (255, 105, 135)],  # Neon pink and soft pink
    [(0, 255, 255), (102, 255, 255)],  # Electric cyan and bright cyan
    [(255, 215, 0), (255, 255, 80)],  # Bright gold and glowing yellow
    [(255, 87, 34), (255, 141, 78)]  # Neon orange and soft orange
]

theme_colors = [
    [(255, 82, 82), (255, 123, 123)],  # Neon red and soft neon red
    [(155, 255, 88), (123, 233, 62)],  # Neon green and bright green
    [(56, 183, 255), (77, 210, 255)],  # Bright blue and lighter blue
    [(255, 155, 0), (255, 190, 0)]  # Bright orange and glowing yellow-orange
]
