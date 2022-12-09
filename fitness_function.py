class Fitness:
    def _init_ (self, clauses, cat):
        self.clauses = clauses
        self.cat = cat

    def get_fitness(self):
        values = []
        count = 0
        for clause in self.clauses:
            for index, value in enumerate(clause):
                if value != None:
                    if self.cat[index] == value:
                        count += 1
            if count == len(clause) - clause.count(None):
                values.append(True)
            else:
                values.append(False)

        return values.count(True)