"""Maze game
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

ITEM1_POS = Items.random_position()
ITEM2_POS = Items.random_position()
ITEM3_POS = Items.random_position()

MacGyver.act_position = (MacGyver.find_macgyver())
GUARDIAN_POS = (Characters.find_guardian())

"""Principal loop"""
GAME = 1
while GAME:
    MAZE.display()
    pygame.display.flip()

    Items.check_items(ITEM1_POS, ITEM2_POS, ITEM3_POS, MacGyver.act_position)

    MacGyver.movements_and_quit((MacGyver.act_position))
    MacGyver.print_mg((MacGyver.pix_position))

    if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) != 0:
        if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) == 1:
            print("You win")
            WINDOW.blit(YOUWIN, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            GAME = 0

        if MacGyver.asleep_guardian(GUARDIAN_POS, MacGyver.act_position) == 2:
            print("You lost")
            WINDOW.blit(YOULOST, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            GAME = 0

pygame.display.quit()
pygame.quit()
exit()
