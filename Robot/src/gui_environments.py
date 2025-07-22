from src.gui_robot import RobotGUI
from src.environments import envs

gui_environments = {env_name: RobotGUI(*args) for env_name, args in envs.items() }

