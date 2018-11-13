"""Jeu de labyrinthe
Python3
UTF-8"""

import random
import pygame

from constants import WINDOW, YOUWIN, YOULOST
from maze import Maze
from characters import Characters, MacGyver
from items import Items

pygame.init()

MAZE = Maze('structure.txt')
MAZE.read()

ITEM1_POS = Items.random_position(Maze.struct)
ITEM2_POS = Items.random_position(Maze.struct)
ITEM3_POS = Items.random_position(Maze.struct)

MacGyver.act_position = (MacGyver.find_macgyver())
GUARDIAN_POS = (Characters.find_guardian())

"""Principal loop"""
GAME = 1
while GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME = 0

    MAZE.display()
    pygame.display.flip()

    Items.check_items(ITEM1_POS, ITEM2_POS, ITEM3_POS, MacGyver.act_position)

    MacGyver.movements((MacGyver.act_position))
    MacGyver.print_mg((MacGyver.pix_position))

    if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) != 0:
        if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) == 1:
            WINDOW.blit(YOUWIN, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.display.quit()
            pygame.quit()
        if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) == 2:
            WINDOW.blit(YOULOST, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.display.quit()
            pygame.quit()

    MacGyver.movements((MacGyver.act_position))
    MacGyver.print_mg((MacGyver.pix_position))

pygame.quit()
