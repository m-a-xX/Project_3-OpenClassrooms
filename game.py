"""Creation of the games's grid"""
def create_grid(nb_lines, nb_colums):
	grid = [[]] * nb_lines
	for line in range(nb_lines):
		grid[line] = [0] * nb_colums
	return grid

grid = create_grid(15, 15)

