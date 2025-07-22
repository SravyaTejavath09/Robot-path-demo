from src.utils import get_environment, display_grid

env_name = "custom_env"
rows = 8
cols = 8

# 💬 Get custom input
start_row = int(input("Enter Start Row (0-7): "))
start_col = int(input("Enter Start Col (0-7): "))
goal_row = int(input("Enter Goal Row (0-7): "))
goal_col = int(input("Enter Goal Col (0-7): "))

start = (start_row, start_col)
goal = (goal_row, goal_col)

robot = get_environment(env_name, start, goal)

# 🤖 Robot Demo
step = 0
while robot.position != robot.goal:
    display_grid(robot.grid, robot.position, robot.goal, robot.obstacles)
    robot.move()
    step += 1
    input("Press Enter for next move...")

# Final state
display_grid(robot.grid, robot.position, robot.goal, robot.obstacles)
print(f"🎉 Reached goal in {step} steps!")
