"""Jeu de labyrinthe
Python3
UTF-8"""

import random
import pygame
from pygame.locals import *

from constants import *
#from classes import *
#from display import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))
pygame.display.set_icon(title)

"""Principal loop"""
game = 1
while game == 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = 0




"""
	def create_grid(nb_lines, nb_colums):
	grid = [[]] * nb_lines
	for line in range(nb_lines):
		grid[line] = [0] * nb_colums
	return grid

	grid = create_grid(15, 15)"""