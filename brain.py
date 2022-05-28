import numpy as np

class Brain:

    def __init__(self, size: int):
        self.directions = self.get_random_vectors(size)

    def get_random_vectors(self, size: int):
        vectors  = [((np.random.random()*2)-1, (np.random.random()*2)-1) for _ in range(size)]
        return vectors

    def mutate(self, mutation_rate: float):
        for i in range(len(self.directions)):
            if(np.random.random() < mutation_rate):
                self.directions[i] = ((np.random.random()*2)-1, (np.random.random()*2)-1)

    def clone(self):
        clone = Brain(size=len(self.directions))
        clone.directions = self.directions.copy()
        return clone
