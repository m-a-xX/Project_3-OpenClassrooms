import random
import pygame
from pygame.locals import *

from constants import *

"""Generate the maze"""
class Maze:

	def __init__(self, file):
		self.structure = 0
		self.file = file
 
	def read(self):
		with open(self.file, 'r') as file:
			Maze.struct = []
			for line in file:
				lines = []
				for char in line:
					if char != '\n':
						lines.append(char)
				Maze.struct.append(lines)
			self.structure = Maze.struct
		
	def display(self):
		for line in range(0, 15):
			for column in range(0, 15):
				if int(Maze.struct[line][column]) == 0:
					window.blit(wall, (column * len_sprites, line * len_sprites))
				if int(Maze.struct[line][column]) == 9:
					window.blit(guardian, (column * len_sprites, line * len_sprites))

	@staticmethod
	def isWall(position):
		x, y = position
		if int(Maze.struct[x][y]) == 0:
			return 1
		else:
			return 0