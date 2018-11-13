"""This file concern the gestion of items"""

import random
import pygame
from pygame.locals import *

from constants import black_sprite, item_1, item_2, item_3, len_spr
from maze import *

"""Manage the items"""
class Items:

    got_i1 = 0
    got_i2 = 0
    got_i3 = 0

    def __init__(self, image):
        self.image = image

    """Display the items and manage the items recuperation"""
    @staticmethod
    def check_items(pos_item1, pos_item2, pos_item3, pos_macgyver):
        pos_y, pos_x = pos_macgyver
        pos_x = pos_x * 40
        pos_y = pos_y * 40
        mg_pixpos = (pos_x, pos_y)
        if mg_pixpos == pos_item1:
            Items.got_i1 = 1
        if mg_pixpos == pos_item2:
            Items.got_i2 = 1
        if mg_pixpos == pos_item3:
            Items.got_i3 = 1
        if Items.got_i1 == 0:
            window.blit(item_1, (pos_item1))
        else:
            window.blit(black_sprite, (pos_item1))
        if Items.got_i2 == 0:
            window.blit(item_2, (pos_item2))
        else:
            window.blit(black_sprite, (pos_item2))
        if Items.got_i3 == 0:
            window.blit(item_3, (pos_item3))
        else:
            window.blit(black_sprite, (pos_item3))
        pygame.display.flip()

    """Generate an aleatory position"""
    @staticmethod
    def random_position(struct):
        pos_x = random.randint(0, 14)
        pos_y = random.randint(0, 14)
        while int(Maze.struct[pos_y][pos_x]) != 1:
            pos_x = random.randint(0, 14)
            pos_y = random.randint(0, 14)
        Maze.struct[pos_y][pos_x] = 3
        pos_x *= len_spr
        pos_y *= len_spr
        return(pos_x, pos_y)
