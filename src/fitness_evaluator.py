class FitnessEvaluator:
    def __init__(self, clauses):
        self.clauses = clauses

    def get_fitness(self, cat):
        count = self.clauses["count"]
        size = self.clauses["size"]
        result_count = 0
        for i in range(1, count+1):
            for j in range(size):
                if self.clauses[i][j] == cat.position[j]:
                    result_count += 1
                    break

        return result_count
