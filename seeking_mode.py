import random
import copy


class SeekingMode:
    def __init__(self, can_stay, num_of_looks, num_of_dimensions_to_change, distance, fitness_eval):
        self.spc = can_stay  # self position considering
        self.num_of_looks = num_of_looks  # seeking memory pool
        self.cdc = num_of_dimensions_to_change  # count of dimensions to change
        self.distance = distance  # seeking range of dimension
        self.fitness_eval = fitness_eval  # fitness function

    def begin_strategy(self, cat):
        candidates = []

        seeking_memory_pool = self.num_of_looks

        for i in range(seeking_memory_pool):
            candidates.append(copy.copy(cat))

        if self.spc:
            seeking_memory_pool -= 1

        for index, cat_child in enumerate(candidates[0:seeking_memory_pool]):
            dimension_indexes = random.sample(range(len(cat_child.position)), self.cdc)

            for idx in dimension_indexes:
                probability = random.random()
                move = 1 if (probability > 0.5) else 0

                cat_child.change_position_at_index(idx, move*self.distance)

            cat_child.evaluate_fitness(self.fitness_eval)
            candidates[index] = cat_child

        same = True

        fitness_values = [cat.fitness for cat in candidates]
        for value in fitness_values:
            if value != fitness_values[0]:
                same = False
                break

        if same:
            return random.choice(candidates)
        else:
            return sorted(candidates, key=lambda cat: cat.fitness)[-1]
