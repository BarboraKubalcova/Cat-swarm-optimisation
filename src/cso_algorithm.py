from random import random
import copy

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
        self.tracing_mode = TracingMode(self.clauses_count)

    def magic(self):
        cats = []
        for i in range(self.population_size):
            if random() < self.mr:
                cats.append(Cat(self.problem_size, False).evaluate_fitness(self.fitness_evaluator))
            else:
                cats.append(Cat(self.problem_size, True).evaluate_fitness(self.fitness_evaluator))
        best_cat = sorted(cats, key=lambda cat: cat.fitness)[-1].copy_self()

        i = 0
        while i < self.num_of_iterations:
            for idx, cat in enumerate(cats):
                if cat.seeking_mode:
                    cats[idx] = self.seeking_mode.begin_strategy(cat)
                else:
                    cats[idx] = self.tracing_mode.begin_strategy(cat, best_cat)

                cats[idx] = cats[idx].evaluate_fitness(self.fitness_evaluator)

            for cat in cats:
                if random() < self.mr:
                    cat.seeking_mode = False
                else:
                    cat.seeking_mode = True

            population_best_cat = sorted(cats, key=lambda cat: cat.fitness)[-1]
            if best_cat.fitness < population_best_cat.fitness:
                best_cat = population_best_cat.copy_self()

            if best_cat.fitness == self.clauses_count:
                break

            i += 1

        print(f"Best cat position: {best_cat.position}\nBest cat fitness: {best_cat.fitness}\n")
        return best_cat.fitness == self.clauses_count, copy.deepcopy(best_cat), i
