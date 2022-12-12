# main method
from cso_algorithm import CatSwarmOptimization
from testing import *

if __name__ == "__main__":
    testing = True
    test = Testing(80, 10, 4)

    if testing:
        problem = test.generate_clauses()
    else:
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
        "cdc": 2,
        "srd": 1,
        "mr": 0.2,
        "population_size": 3,
    }

    cso = CatSwarmOptimization(problem, setting)

    test.test(cso, 100000)
