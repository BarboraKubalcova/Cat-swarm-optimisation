# main method
from cat import Cat
from cso_algorithm import CatSwarmOptimization
from fitness_evaluator import FitnessEvaluator

if __name__ == "__main__":
    problem = {
        "size": 6,
        "count": 7,
        1:  [0, 0, None, None, None, 1],
        2: [0, None, 0, None, None, 0],
        3: [None, 0, 0, None, None, 1],
        4: [None, None, None, 0, None, 0],
        5: [None, None, None, 0, 0, 1],
        6: [None, 1, 0, 1, None, 0],
        7: [0, None, None, 0, None, 1],
    }

    setting = {
        "iterations": 5,
        "smp": 3,
        "spc": True,
        "cdc": 2,
        "srd": 1,
        "mr": 0.33,
        "population_size": 3,
    }

    cso = CatSwarmOptimization(problem, setting)
    cso.magic()
    print(problem)

    cat = Cat(5, False)
    cat.position = [1, 0, 1, 0, 0, 1]
    cat.evaluate_fitness(FitnessEvaluator(problem))

