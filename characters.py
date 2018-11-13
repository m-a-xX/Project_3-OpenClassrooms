"""This file concern the gestion of characters"""

import pygame
from pygame.locals import *

from constants import guardian, macgyver, black_sprite, len_spr
from maze import *
from items import *

pygame.init()

"""Manage characters and moves"""
class Characters:

    def __init__(self, dep_x, dep_y, image):
        self.dep_x = dep_x
        self.dep_y = dep_y
        self.image = image

    @staticmethod
    def find_guardian():
        for pos_x in range(0, 15):
            for pos_y in range(0, 15):
                if int(Maze.struct[pos_x][pos_y]) == 9:
                    return (pos_x, pos_y)


"""Child class of Characters for all specifics things to MacGyver"""
class MacGyver(Characters):

    act_position = (0, 0)

    @staticmethod
    def print_mg(position):
        window.blit(macgyver, (position))
        if MacGyver.old_position != 0:
            pos_y, pos_x = MacGyver.old_position
            window.blit(black_sprite, (pos_x * len_spr, pos_y * len_spr))
        pygame.display.flip()

    @staticmethod
    def asleep_guardian(guardian_position, macgyver_position):
        if not guardian_position == macgyver_position:
            return 0
        if guardian_position == macgyver_position:
            if Items.got_i1 and Items.got_i2 and Items.got_i3:
                return 1

    @staticmethod
    def movements(position):
        pos_x, pos_y = position
        for event in pygame.event.get():
            if event.type == KEYDOWN:
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
        MacGyver.act_position = (pos_x, pos_y)
        MacGyver.pix_position = (pos_y * len_spr, pos_x * len_spr)
        if MacGyver.act_position != position:
            MacGyver.old_position = position
        else:
            MacGyver.old_position = 0

    @staticmethod
    def find_macgyver():
        for pos_x in range(0, 15):
            for pos_y in range(0, 15):
                if int(Maze.struct[pos_x][pos_y]) == 2:
                    return (pos_x, pos_y)
