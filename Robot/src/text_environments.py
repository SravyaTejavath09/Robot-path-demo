from src.robot import Robot
from src.environments import envs

text_environments = {env_name: Robot(*args) for env_name, args in envs.items() }

