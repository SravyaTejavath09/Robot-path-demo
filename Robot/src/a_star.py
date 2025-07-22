from queue import PriorityQueue
from src.direction import Direction
from src.cell import Cell

class AStar:
    def __init__(self, robot):
        self.open_set = PriorityQueue() 
        self.open_set.put((0, robot.position))
        self.came_from = {}
        self.goal = robot.goal_cell
        self.graph = robot.graph
        self.g_score = {robot.position: 0}
        self.f_score = {robot.position: self.heuristic(robot.position)}

    def heuristic(self, node):
        return ((node.row - self.goal.row) ** 2 + (node.column - self.goal.column) ** 2) ** 0.5

    def reconstruct_path(self, current):
        path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            path.insert(0, current)
        return path

    def search_ongoing(self):
        return not self.open_set.empty()

    def get_current_node(self):
        return self.open_set.get()[1]
    
    def get_path(self, current):
        return self.reconstruct_path(current)

    def get_tentative_score(self, current):
        return self.g_score[current] + 1

    def get_neighbour_score(self, neighbour):
        return self.g_score.get(neighbour, float('inf'))

    def update_neighbour_score(self, current, neighbour, tentative_score):
        self.came_from[neighbour] = current
        self.g_score[neighbour] = tentative_score
        self.f_score[neighbour] = tentative_score + self.heuristic(neighbour)

    def neighbour_not_in_queue(self, neighbour):
        return neighbour not in [node[1] for node in self.open_set.queue]

    def add_neighbout_in_queue(self, neighbour):
        self.open_set.put((self.f_score[neighbour], neighbour))

    def get_next_cell(self, cell, direction):
        if direction == Direction.Up:
            return Cell(cell.row - 1, cell.column)
        elif direction == Direction.Down:
            return Cell(cell.row + 1, cell.column)
        elif direction == Direction.Left:
            return Cell(cell.row, cell.column - 1)
        elif direction == Direction.Right:
            return Cell(cell.row, cell.column + 1)

    def get_neighbours(self, cell):
        neighbours = []
        graph = self.graph
        actions = graph[cell]

        for action in actions:
            neighbours.append(self.get_next_cell(cell, action))

        return neighbours

