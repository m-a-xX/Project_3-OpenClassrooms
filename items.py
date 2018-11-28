"""This file concern the gestion of items"""

import random
import pygame

from constants import BLACK_SPRITE, ITEM_1, ITEM_2, ITEM_3, LEN_SPR, WINDOW
from maze import Maze

class Items:
    """Manage the items"""

    got_i1 = 0
    got_i2 = 0
    got_i3 = 0

    def __init__(self, image):
        self.image = image


    @staticmethod
    def check_items(pos_item1, pos_item2, pos_item3, pos_macgyver):
        """Display the items and manage the items recuperation"""
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
            WINDOW.blit(ITEM_1, (pos_item1))
        if Items.got_i2 == 0:
            WINDOW.blit(ITEM_2, (pos_item2))
        if Items.got_i3 == 0:
            WINDOW.blit(ITEM_3, (pos_item3))
        pygame.display.flip()


    @staticmethod
    def random_position():
        """Generate an aleatory position"""
        pos_x = random.randint(0, 14)
        pos_y = random.randint(0, 14)
        while int(Maze.struct[pos_y][pos_x]) != 1:
            pos_x = random.randint(0, 14)
            pos_y = random.randint(0, 14)
        Maze.struct[pos_y][pos_x] = '3'
        pos_x *= LEN_SPR
        pos_y *= LEN_SPR
        return(pos_x, pos_y)
