"""Jeu de labyrinthe
Python3
UTF-8"""

import random
import pygame
from pygame.locals import *

from constants import *
from classes import *
from display import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))
pygame.display.set_icon(title)

"""Principal loop"""
game = 1
while game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = 0

	"""Generate and print the maze"""
	Maze.(grid)
	print.Maze()

	"""Generate and print items"""
	item1_pos = randomPosition.Items(struct)
	window.blit(item_1, (item1_pos))
	item2_pos = randomPosition.Items(struct)
	window.blit(item_2, (item2_pos))
	item3_pos = randomPosition.Items(struct)
	window.blit(item_3, (item3_pos))
	pygame.display.flip()

	"""Core of the game"""
	win = 0
	while not win:
		act_position = first_position
		movements.MacGyver(firstPosition.Characters(act_position))
		printMg.MacGyver(act_position)
		checkItems.Items(item1_pos, item2_pos, item3_pos, act_position)
		if asleepGuardian.MacGyver(guardian_position, act_position):
			win = 1



"""
	def create_grid(nb_lines, nb_colums):
	grid = [[]] * nb_lines
	for line in range(nb_lines):
		grid[line] = [0] * nb_colums
	return grid

	grid = create_grid(15, 15)"""