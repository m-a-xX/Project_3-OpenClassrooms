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
			struct = []
		line = 0
		for lines in range(0, 15):
			column = 0
			for columns in range(0, 15):
				struct[line][column] = #char
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

	@property
	def isWall(self, pos_x, pos_y):
		if struct[pos_x][pos_y] == 0:
			return 1
		else:
			return 0

"""Manage characters and moves"""
class Characters:

	def __init__(self, dep_x, dep_y, image):
		self.dep_x = dep_x
		self.dep_y = dep_y
		self.image = image

	def firstPosition(self, (dep_x, dep_y)):
		first position = ((dep_x * len_sprites), (dep_y * len_sprites))
		return first_position


"""Child class of Characters for all specifics things to MacGyver"""
class MacGyver(Characters):

	def printMg(self, position):
		window.blit(macgyver, (position))
		pygame.display.flip()

	def asleepGuardian(self, guardian_position, macgyver_position):
		if guardian_position == macgyver_position and items_count == 3:
			return 1
		else:
			return 0

	@property
	def movements(self, (pos_x, pos_y)):
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				pos_x -= 1
				if isWall.Maze(pos_x, pos_y):
					pos_x += 1
			if event.key == K_RIGHT:
				pos_x += 1
				if isWall.Maze(pos_x, pos_y):
					pos_x -= 1
			if event.key == K_UP:
				pos_y += 1
				if isWall.Maze(pos_x, pos_y):
					pos_y -= 1
			if event.key == K_DOWN:
				pos_y -= 1
				if isWall.Maze(pos_x, pos_y):
					pos_y += 1
		act_position = (pos_x * len_sprites, pos_y * len_sprites)
		return act_position


"""Manage the items"""
class Items:

	def __init__(self, image):
		self.image = image

	@property
	def checkItems(self, position_item1, position_item2, position_item3, position_macgyver):
		if position_macgyver == position_item1:
			items_count += 1
		if position_macgyver == position_item2:
			items_count += 1
		if position_macgyver == position_item3:
			items_count += 1
		return items_count

	@property
	def randomPosition(self, struct):
		x = 0
		y = 0
		while struct[x][y] != 1:
			x = random.randint(0, 14)
			y = random.randint(0, 14)
		struct[x][y] = 3
		x = x * len_sprites
		y = y * len_sprites
		return 	(x, y)