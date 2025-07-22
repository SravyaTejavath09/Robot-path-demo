import sys
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_directory)
from robot import Robot
from direction import Direction
import pygame
import os


class RobotGUI(Robot):
    def __init__(self, board_size, obstacles, start_cell, goal_cell):
        super().__init__(board_size, obstacles, start_cell, goal_cell)

        self.width, self.height = 800, 800
        self.rows, self.cols = board_size, board_size
        self.cell_size = self.width // self.cols

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.robot_img = pygame.image.load(os.path.join(script_directory, 'assets', 'robot.png'))
        self.robot = pygame.transform.scale(self.robot_img, (self.cell_size, self.cell_size))
        self.__pygame_initialised = False

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.window, self.black, rect, 1)

    def draw_robot(self, x, y):
        x, y = x - 1, y - 1
        self.window.blit(self.robot, (x * self.cell_size, y * self.cell_size))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            x, y = obstacle.column - 1, obstacle.row - 1
            rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.window, self.red, rect)

    def draw_goal(self):
        x, y = self.goal_cell.column - 1, self.goal_cell.row - 1
        rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.window, self.green, rect)

    def move(self, direction: Direction):
        super().move(direction)
        self.draw()

    def print_board(self):
        pass

    def init_pygame(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Robot Path Finding")
        self.__pygame_initialised = True

    def draw(self):
        if not self.__pygame_initialised:
            self.init_pygame()

        self.window.fill(self.white)
        self.draw_grid()
        self.draw_obstacles()
        self.draw_goal()
        self.draw_robot(self.position.column, self.position.row)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


