import pygame
from .. import setup
from .. import tools

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()

    def setup_background(self, parameter_list):
        pass

    def setup_player(self, parameter_list):
        pass

    def setup_cursor(self, parameter_list):
        pass

    def update(self, surface):
        import random
        surface.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))