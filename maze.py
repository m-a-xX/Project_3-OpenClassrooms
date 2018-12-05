"""This file concern the interpretaion of the
txt file and the generation of the map"""

from constants import WALL, GUARDIAN, WINDOW, LEN_SPR


class Maze:

    """Generate the maze"""
    def __init__(self, file):
        self.structure = 0
        self.file = file

    def read(self):
        """Convert the txt file to a double list"""
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
        """Print the games's map"""
        for line in range(0, 15):
            for column in range(0, 15):
                if Maze.struct[line][column] == '0':
                    WINDOW.blit(WALL, (column * LEN_SPR, line * LEN_SPR))
                if Maze.struct[line][column] == '9':
                    WINDOW.blit(GUARDIAN, (column * LEN_SPR, line * LEN_SPR))

    @staticmethod
    def is_wall(position):
        """Boolean returns 1 if the movement is possible"""
        pos_x, pos_y = position
        if Maze.struct[pos_x][pos_y] == '0':
            return 1
