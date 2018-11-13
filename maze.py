import random
import pygame
from pygame.locals import *

from constants import wall, guardian, window, len_spr

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
                    window.blit(wall, (column * len_spr, line * len_spr))
                if int(Maze.struct[line][column]) == 9:
                    window.blit(guardian, (column * len_spr, line * len_spr))

    @staticmethod
    def is_wall(position):
        pos_x, pos_y = position
        if int(Maze.struct[pos_x][pos_y]) == 0:
            return 1