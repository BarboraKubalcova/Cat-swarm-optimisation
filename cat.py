import numpy as np


class Cat:

    def __init__(self, problem_size, seeking_mode):
        self.position = np.random.randint(0, 2, problem_size)
        self.velocity = np.random.randint(0, 2, problem_size)
        self.fitness = 0
        self.seeking_mode = seeking_mode

    def change_position_at_index(self, index, value):
        self.position[index] = value

    def evaluate_fitness(self, fitness_func):
        self.fitness = fitness_func.get_fitness(self)
        return self





