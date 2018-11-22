"""This file concern the gestion of characters"""

import random
import pygame
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE

from constants import MACGYVER, BLACK_SPRITE, LEN_SPR, WINDOW
from maze import Maze
from items import Items

pygame.init()

class Characters:
    """Manage characters and moves"""

    def __init__(self, dep_x, dep_y, image):
        self.dep_x = dep_x
        self.dep_y = dep_y
        self.image = image

    @staticmethod
    def find_guardian():
        """Find the guardian in the structure"""
        for pos_x in range(0, 15):
            for pos_y in range(0, 15):
                if int(Maze.struct[pos_x][pos_y]) == 9:
                    return (pos_x, pos_y)


class MacGyver(Characters):
    """Child class of Characters for all specifics things to MacGyver"""

    act_position = (0, 0)

    @staticmethod
    def print_mg(position):
        """Print Mg on the new position and print a black sprite on the old"""
        WINDOW.blit(MACGYVER, (position))
        if MacGyver.old_position != 0:
            pos_y, pos_x = MacGyver.old_position
            WINDOW.blit(BLACK_SPRITE, (pos_x * LEN_SPR, pos_y * LEN_SPR))
        pygame.display.flip()

    @staticmethod
    def asleep_guardian(guardian_position, macgyver_position):
        """Check if the 3 items are captured and if Mg reached the exit"""
        if not guardian_position == macgyver_position:
            return 0
        if guardian_position == macgyver_position:
            if Items.got_i1 and Items.got_i2 and Items.got_i3:
                return 1
            else:
                return 2

    @staticmethod
    def movements_and_quit(position):
        """Interpret keyboard input and manage the differents positions"""
        pos_x, pos_y = position
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.key == K_LEFT:
                    pos_y -= 1
                    if Maze.is_wall((pos_x, pos_y)):
                        pos_y += 1
                if event.key == K_RIGHT:
                    pos_y += 1
                    if Maze.is_wall((pos_x, pos_y)):
                        pos_y -= 1
                if event.key == K_UP:
                    pos_x -= 1
                    if Maze.is_wall((pos_x, pos_y)):
                        pos_x += 1
                if event.key == K_DOWN:
                    pos_x += 1
                    if Maze.is_wall((pos_x, pos_y)):
                        pos_x -= 1
        MacGyver.act_pos = (pos_x, pos_y)
        MacGyver.pix_position = (pos_y * LEN_SPR, pos_x * LEN_SPR)
        if MacGyver.act_pos != position:
            MacGyver.old_position = position
        else:
            MacGyver.old_position = 0

    @staticmethod
    def find_macgyver():
        """Find Macgyver in the structure"""
        for pos_x in range(0, 15):
            for pos_y in range(0, 15):
                if int(Maze.struct[pos_x][pos_y]) == 2:
                    return (pos_x, pos_y)
