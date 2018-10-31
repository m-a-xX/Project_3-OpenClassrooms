"""Jeu de lalyribthe
Python3
Uft8"""

import pygame
from pygame.locals import *

from constants import *

pygame.init()

window = pygame.display.set_mode((side_window, side_window))

icon = pygame.image.load(title)
pygame.display.set_icon(icone)

game = 1
while game == 1:
	



	def create_grid(nb_lines, nb_colums):
	grid = [[]] * nb_lines
	for line in range(nb_lines):
		grid[line] = [0] * nb_colums
	return grid

	grid = create_grid(15, 15)

