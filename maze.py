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
			Maze.struct = [] #Creation d'un attribut de classe pour reutiliser la structure
		line = 0
		for lines in range(0, 15):
			column = 0
			for columns in range(0, 15):
				struct[line][column] = char
				if char == 2:
					first_position = (line, column)
				if char == 9:
					guardian_position = (line, column)
				column += 1
			line += 1
		
	def print(self):
		window.blit(background, [0,0])
		pygame.display.flip()
		line = 0
		for lines in range(0, 15):
			column = 0
			for columns in range(0, 15):
				if struct[line][column] == 0:
					window.blit(wall, (line * len_sprites, column * len_sprites))
				if struct[line][column] == 9:
					window.blit(guardian, (line * len_sprites, column * len_sprites))
				if struct[line][column] == 2:
					window.blit(macgyver, (line * len_sprites, column * len_sprites))					
				column += 1
			line += 1
			pygame.display.flip()

	@staticmethod
	def isWall(position):
		x, y = position
		if struct[x][y] == 0:
			return 1
		else:
			return 0