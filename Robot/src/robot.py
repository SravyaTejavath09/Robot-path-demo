class Robot:
    def __init__(self, grid_size, start, goal, obstacles):
        self.grid = grid_size
        self.start = start
        self.goal = goal
        self.position = start
        self.obstacles = obstacles

    def move(self):
        row, col = self.position
        goal_row, goal_col = self.goal

        if col < goal_col and (row, col + 1) not in self.obstacles:
            col += 1
        elif row < goal_row and (row + 1, col) not in self.obstacles:
            row += 1
        elif col > goal_col and (row, col - 1) not in self.obstacles:
            col -= 1
        elif row > goal_row and (row - 1, col) not in self.obstacles:
            row -= 1

        self.position = (row, col)
