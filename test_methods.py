from classes.Button import Button
from classes.Comment import Comment
from classes.Post import Post
from constants import COMMENT_BUTTON_X_POST, COMMENT_BUTTON_Y_POS, \
    COMMENT_BUTTON_WIDTH, COMMENT_BUTTON_HEIGHT, LIKE_BUTTON_X_POS, \
    LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT
from helpers import mouse_in_button, read_comment_from_user


def test_comment():
    comment = Comment("This is your first comment")
    comment.display(0)


def test_post():
    new_post = Post("Images/ronaldo.jpg", "Home",
                    "Your post class is working!!!!!!")
    new_post.display()


