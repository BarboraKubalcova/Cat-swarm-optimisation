import numpy as np


class TracingMode:
    def __init__(self):
        pass

    def begin_strategy(self, cat, best_cat):
        probability = (best_cat.fitness - cat.fitness)/ cat.position.count
        for i in range(cat.position.count):
            if np.random.random() < probability:
                cat.position[i] = best_cat.position[i]
            else:
                cat.position[i] = not best_cat.position[i]

        return cat
