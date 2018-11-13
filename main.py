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
item1_pos = Items.random_position(Maze.struct)
item2_pos = Items.random_position(Maze.struct)
item3_pos = Items.random_position(Maze.struct)

MacGyver.act_position = (MacGyver.find_macgyver())
guardian_pos = (Characters.find_guardian())

"""Principal loop"""
game = 1
while game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = 0

	"""Print the maze"""
	maze.display()
	pygame.display.flip()


	"""Print items"""
	Items.check_items(item1_pos, item2_pos, item3_pos, MacGyver.act_position)

	"""Core of the game"""
	MacGyver.movements((MacGyver.act_position))
	MacGyver.print_mg((MacGyver.pix_position))
	if MacGyver.asleep_guardian(guardian_pos, MacGyver.act_position) != 0:
		if MacGyver.asleep_guardian(guardian_pos, MacGyver.act_position) == 1:
			window.blit(youwin, (0, 0))
			pygame.display.flip()
			pygame.time.wait(5000)
			pygame.display.quit()
			pygame.quit()
		if MacGyver.asleep_guardian(guardian_pos, MacGyver.act_position) == 2:
			window.blit(youlost, (0, 0))
			pygame.display.flip()
			pygame.time.wait(5000)
			pygame.display.quit()
			pygame.quit()
	MacGyver.movements((MacGyver.act_position))
	MacGyver.print_mg((MacGyver.pix_position))

pygame.quit()