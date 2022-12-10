class Cat:

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.fitness = 0

    def change_position_at_index(self, index, distance):
        self.position[index] += distance

    def evaluate_fitness(self, fitness_func):
        self.fitness = fitness_func.get_fitness()



