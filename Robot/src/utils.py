from src.robot import Robot

def get_environment(env_name, start, goal):
    if env_name == "custom_env":
        rows = 8
        # Define obstacles
        obstacles = [(3, 4), (4, 4), (5, 4)]
        return Robot(rows, start, goal, obstacles)
    raise ValueError("Unknown environment")

def display_grid(grid_size, robot_pos, goal_pos, obstacles):
    print("\n📦 GRID:")
    for i in range(grid_size):
        row = ""
        for j in range(grid_size):
            if (i, j) == robot_pos:
                row += " R "
            elif (i, j) == goal_pos:
                row += " G "
            elif (i, j) in obstacles:
                row += " X "
            else:
                row += " . "
        print(row)
