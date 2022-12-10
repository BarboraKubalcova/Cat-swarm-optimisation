class Cat:

    def __init__(self, position, fitness_func):
        self.position = position
        self.fitness = fitness_func.get_fitness()
