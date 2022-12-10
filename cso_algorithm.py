from random import random

from cat import Cat
from fitness_evaluator import FitnessEvaluator
from seeking_mode import SeekingMode
from tracing_mode import TracingMode


class CatSwarmOptimization:

    def __init__(self, maxsat_problem, cso_setting):
        self.fitness_evaluator = FitnessEvaluator(maxsat_problem)
        self.problem_size = maxsat_problem["size"]
        self.clauses_count = maxsat_problem["count"]
        self.num_of_iterations = cso_setting["iterations"]
        self.smp = cso_setting["smp"]
        self.cdc = cso_setting["cdc"]
        self.spc = cso_setting["spc"]
        self.srd = cso_setting["srd"]
        self.mr = cso_setting["mr"]
        self.population_size = cso_setting["population_size"]
        self.seeking_mode = SeekingMode(self.spc, self.smp, self.cdc, self.srd, self.fitness_evaluator)
        self.tracing_mode = TracingMode()

    def magic(self):
        cats = []
        for i in range(self.population_size):
            if random() < self.mr:
                cats.append(Cat(self.problem_size, False).evaluate_fitness(self.fitness_evaluator))
            else:
                cats.append(Cat(self.problem_size, True).evaluate_fitness(self.fitness_evaluator))
        best_cat = sorted(cats, key=lambda cat: cat.fitness)[-1]

        for i in range(self.num_of_iterations):
            for cat in cats:
                if cat.seeking_mode:
                    self.seeking_mode.begin_strategy(cat)
                else:
                    self.tracing_mode.begin_strategy(cat, best_cat)

                # print(cats[j].fitness)
                # print(cats[j].position)
                # print()


