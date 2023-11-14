import pygame
from constants import *
from helpers import screen


class Comment:

    def __init__(self, text):
        self.text = text

    def display(self, comment_num):
        comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment_to_display = comment_font.render(self.text, True, BLACK)
        screen.blit(comment_to_display, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + comment_num * COMMENT_LINE_HEIGHT])

    def censor(self, text, bad_words):
        for word in bad_words:
            text = text.replace(word, '*' * len(word))
        return text

