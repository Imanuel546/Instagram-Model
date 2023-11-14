import pygame
import pywhatkit
from classes.Post import Post
from constants import *
from helpers import screen
from helpers import from_text_to_array
from helpers import center_text


class TextPost(Post):

    def __init__(self, background_color, text, color_text, location, description):
        Post.__init__(self, location, description)
        self.background_color = background_color
        self.color_text = color_text
        self.text = text
        self.text_array = from_text_to_array(self.text)
    
    def display_content(self):
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        
        for row in range(len(self.text_array)):
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text_array[row], True, self.color_text)
            text_pos = center_text(len(self.text_array), text, row)
            screen.blit(text, text_pos)

    def share(self, phnum):
        pywhatkit.sendwhatmsg_instantly(phnum, self.text)

    def to_list(self):
        return f"txt|{self.location}|{self.description}|{self.likes_counter}|{self.text}"
