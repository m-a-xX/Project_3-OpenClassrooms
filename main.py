"""Jeu de labyrinthe
Python3
UTF-8"""

import random
import pygame
from pygame.locals import *

from constants import *
from maze import *
from characters import *
from items import *

pygame.init()

"""Generate the maze"""
maze = Maze('structure.txt')
maze.read()

"""Generate items positions"""
item1_pos = Items.randomPosition(Maze.struct)
item2_pos = Items.randomPosition(Maze.struct)
item3_pos = Items.randomPosition(Maze.struct)
MacGyver.act_position = (1, 0)

"""Principal loop"""
game = 1
while game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = 0

	"""Print the maze"""
	maze.print()
	pygame.display.flip()


	"""Print items"""
	Items.checkItems(item1_pos, item2_pos, item3_pos, MacGyver.act_position)

	MacGyver.movements((MacGyver.act_position))
	MacGyver.printMg((MacGyver.pix_position))

	"""Core of the game
	win = 0
	while not win:
		MacGyver.movements(Characters.firstPosition(act_position))
		MacGyver.printMg(act_position)
		Items.checkItems(item1_pos, item2_pos, item3_pos, act_position)
		if MacGyver.asleepGuardian(guardian_position, act_position):
			win = 1
"""