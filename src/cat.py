import numpy as np


class Cat:

    def __init__(self, problem_size, seeking_mode):
        self.position = np.random.randint(0, 2, problem_size).tolist()
        self.fitness = 0
        self.seeking_mode = seeking_mode

    def change_position_at_index(self, index, value):
        self.position[index] = value

    def evaluate_fitness(self, fitness_eval):
        self.fitness = fitness_eval.get_fitness(self)
        return self

    def copy_self(self):
        copycat = Cat(len(self.position), self.seeking_mode)
        copycat.position = self.position[:]
        copycat.fitness = self.fitness
        return copycat






