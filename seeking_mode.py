import random


class SeekingMode:
    def __init__(self, can_stay, num_of_looks, num_of_dimensions_to_change, distance, fitness_f):
        self.can_stay = can_stay
        self.num_of_looks = num_of_looks
        self.look_variety = num_of_dimensions_to_change
        self.distance = distance
        self.fitness_f = fitness_f

    def find_best_move(self, cat):
        options = []

        cat_length = self.num_of_looks

        for i in range(cat_length):
            options.append(cat.deepcopy())

        if self.can_stay:
            cat_length -= 1

        move_result = []
        for index, cat_look in enumerate(options[0:cat_length]):
            dimension_indexes = random.sample(range(len(cat_look.position)), self.look_variety)

            for idx in dimension_indexes:
                probability = random.random()
                move = 1 if (probability > 0.5) else -1

                cat_look.position[idx] += (move * self.distance)

            options[index] = cat_look
            move_result.append(self.fitness_f(cat_look))

        if self.can_stay:
            move_result.append(self.fitness_f(options[-1]))

        same = True

        for value in move_result:
            if value != move_result[0]:
                same = False
                break

        if same:
            return random.choice(options)
        else:
            return options[move_result.index(max(move_result))]