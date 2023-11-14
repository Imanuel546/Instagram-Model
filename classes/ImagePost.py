import time

import pygame
import pywhatkit
from classes.Post import Post
from constants import *
from helpers import screen
from classes.Filter import *


class ImagePost(Post):

    def __init__(self, image_src, location, description, filter_type=None):
        image = pygame.image.load(image_src)
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        self.image_src = image_src
        self.image = image
        self.filter = filter_type
        Post.__init__(self, location, description)

    def display_content(self):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        if self.filter is not None:
            Filter.apply_filter(self.filter)

    def share(self, phnum):
        path = fr"C:/Users/manul/PycharmProjects/NitzagaramWorking/Images/{self.image_src[7:]}"
        information = f"The post has {self.likes_counter} likes\nThe post made in {self.location}, " \
                      f"\nThe description of the post is: '{self.description}'."
        pywhatkit.sendwhats_image(phnum, path, information, wait_time=10)

    def to_list(self):
        return f"img|{self.location}|{self.description}|{self.likes_counter}|{self.image_src}"



