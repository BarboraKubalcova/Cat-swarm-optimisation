class FitnessEvaluator:
    def __init__(self, problem):
        self.problem = problem

    def get_fitness(self, cat):
        count = self.problem["count"]
        size = self.problem["size"]
        result_count = 0
        for i in range(1, count+1):
            for j in range(size):
                if self.problem[i][j] == cat.position[j]:
                    result_count += 1
                    break

        return result_count
