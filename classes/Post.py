import pygame
from constants import *
from helpers import screen

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, location, description):

        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0
        self.user_name = "Imanuel"

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        pass

    def display_header(self):
        # display location
        location_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        location_to_display = location_font.render(self.location, True, LIGHT_GRAY)
        screen.blit(location_to_display, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        # display description
        description_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        description_to_display = description_font.render(self.description, True, GREY)
        screen.blit(description_to_display, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        # display header
        header_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        header_to_display = header_font.render(self.user_name, True, GREY)
        screen.blit(header_to_display, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def display_likes(self):
        likes_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        likes_to_display = likes_font.render("Liked by " + str(self.likes_counter) + " users", True, BLACK)
        screen.blit(likes_to_display, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.likes_counter += 1  # Adding like for a post

    def add_comment(self, text):
        self.comments.append(text)  # Adding comment for a post

    def view_more_comments(self):  # Moving down for other comments
        if self.comments_display_index == len(self.comments) - 1:
            self.comments_display_index = 0
        else:
            self.comments_display_index += 1

    def reset_comments_display_index(self):
        self.comments_display_index = 0





