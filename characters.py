import pygame
from pygame.locals import *

from constants import *

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

	act_position = (0, 0)

	def printMg(self, position):
		window.blit(macgyver, (position))
		pygame.display.flip()

	@staticmethod
	def asleepGuardian(guardian_position, macgyver_position):
		if guardian_position == macgyver_position and items_count == 3:
			return 1
		else:
			return 0

	@staticmethod
	def movements((pos_x, pos_y)):
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
		MacGyver.act_position = (pos_x * len_sprites, pos_y * len_sprites) #Attribut de classe pour pouvoir reutiliser la position
		return act_position