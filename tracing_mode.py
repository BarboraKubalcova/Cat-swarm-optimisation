import numpy as np


class TracingMode:
    def __init__(self, clauses_count):
        self.clauses_count = clauses_count

    def begin_strategy(self, cat, best_cat):
        probability = (best_cat.fitness - cat.fitness) / self.clauses_count
        for i in range(len(cat.position)):
            if np.random.random() < probability:
                cat.position[i] = best_cat.position[i]
            else:
                cat.position[i] = int(not best_cat.position[i])

        return cat
