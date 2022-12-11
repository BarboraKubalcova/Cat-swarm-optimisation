# main method
from cat import Cat
from cso_algorithm import CatSwarmOptimization
from fitness_evaluator import FitnessEvaluator

if __name__ == "__main__":
    problem = {
        "size": 5,
        "count": 7,
        1:  [0, 0, None, None, None],
        2: [0, None, 0, None, None],
        3: [None, 0, 0, None, None],
        4: [None, None, None, 0, None],
        5: [None, None, None, 0, 0],
        6: [None, 1, 0, 1, None],
        7: [0, None, None, 0, None],
    }

    setting = {
        "iterations": 10,
        "smp": 3,
        "spc": True,
        "cdc": 5,
        "srd": 1,
        "mr": 0.33,
        "population_size": 3,
    }

    cso = CatSwarmOptimization(problem, setting)
    cso.magic()
