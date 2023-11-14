#  I'm Imanuel Moiseev, and I hope you will like my project.

import pywhatkit
import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Post import *
from test_methods import test_comment
from buttons import like_button, click_post_button, view_more_comments_button, share_button
from helpers import *
from buttons import comment_button
from classes.Button import *
from classes.Comment import *
from classes.ImagePost import *
from classes.TextPost import *
from classes.Filter import *
from constants import BAD_WORDS


def main():

    # Set up the game display, clock and headline
    pygame.init()


    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()
    purple_filter = Filter((30, 12, 121), 80)
    green_filter = Filter((0, 102, 0), 80)
    pink_filter = Filter((255, 153, 255), 100)
    imagePost1 = ImagePost("Images/forest.jpg", "Haifa", "Look how beautiful is our nature...", purple_filter)
    imagePost2 = ImagePost("Images/psychology.jpg", "Brain", "Guess what's happening?", pink_filter)
    textPost1 = TextPost((11, 7, 224), "Hello, that's my first post!", (250, 254, 255), "Israel", "I hope!")
    post_list = [imagePost1, imagePost2, textPost1]
    current_index = 0
    current_post = post_list[current_index]

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                elif mouse_in_button(comment_button, pos):
                    comment1 = read_comment_from_user()

                    if len(comment1) != 0:  # Blocking the option to send an empty response
                        c1 = Comment(comment1)
                        c1.text = c1.censor(c1.text, BAD_WORDS)
                        current_post.add_comment(c1)
                elif mouse_in_button(click_post_button, pos):
                    current_index += 1
                    if current_index >= len(post_list):
                        current_index = 0
                    current_post = post_list[current_index]
                    current_post.reset_comments_display_index()
                elif mouse_in_button(view_more_comments_button, pos):
                    current_post.view_more_comments()
                elif mouse_in_button(share_button, pos):
                    phone_num = read_comment_from_user()
                    current_post.share(phone_num)

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
