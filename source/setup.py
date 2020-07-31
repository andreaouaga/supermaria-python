import pygame
from . import constants as C
from . import tools

pygame.init()
pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))

GRAPHICS = tools.load_graphics('resources/graphics')