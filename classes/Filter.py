from constants import *
import pygame
from helpers import screen


class Filter:

    def __init__(self, filter_color, alpha):
        self.filter_color = filter_color
        self.alpha = alpha

    def apply_filter(self):
        rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        rect.set_alpha(self.alpha)
        rect.fill(self.filter_color)
        screen.blit(rect, (POST_X_POS, POST_Y_POS))




