def createGrid(nbLines, nbColumns):
	grid = [[]] * nbLines
	for line in range(nbLines):
		grid[line] = [0] * nbColumns
	return grid

grid = createGrid(15, 15)

grid[1][1] = 15

print(grid[1][1])