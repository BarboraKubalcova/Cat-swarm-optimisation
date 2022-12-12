import random


class Testing:
    def __init__(self, problem_size, clauses_count, max_changes_in_clause):
        self.problem_size = problem_size
        self.clauses_count = clauses_count
        self.max_changes = max_changes_in_clause

    def generate_clauses(self):
        problem = {
            "size": self.problem_size,
            "count": self.clauses_count,
        }

        for i in range(1, self.clauses_count + 1):
            changes_count = random.randint(1, self.max_changes)

            change_indexes = random.sample(range(self.problem_size), changes_count)

            clause = [None] * self.problem_size

            for index in change_indexes:
                clause[index] = random.randint(0, 1)

            problem[i] = clause

        return problem

    def test(self, cso, test_sample_size):
        cats = {}
        values = {}
        iterations = {}

        for i in range(test_sample_size):
            value, cat, iteration = cso.magic()

            cats[str(cat.position)] = cats.get(str(cat.position), 0) + 1
            values[value] = values.get(value, 0) + 1
            iterations[iteration] = iterations.get(iteration, 0) + 1

        best_cat = max(cats, key=cats.get)

        print("Statistics")
        print(f"Tested iterations: {test_sample_size}")
        print(f"Inputted problem : {cso.fitness_evaluator.problem}")
        print(f"Most cats ended in this position: {best_cat}")
        print(f"Number of cats in this position {cats[best_cat]}")
        print(f"Statistics for when each simulation ended: {iterations}")
        print(f"Numbers for finding optimal result: {values}")
