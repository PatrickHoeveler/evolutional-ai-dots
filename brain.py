import numpy as np

class Brain:

    def __init__(self, size: int):
        self.directions = self.get_random_vectors(size)
        # print('brain initialized with', size, 'directions')
        
    def get_random_vectors(self, size: int):
        # (additive direction between -1 and 1)
        # (90, 80.77)
        vectors  = [((np.random.random()*2)-1, (np.random.random()*2)-1) for _ in range(size)]
        return vectors

    def mutate(self):
        # mutate the directions
        for i in range(len(self.directions)):
            if(np.random.random() < 0.1):
                self.directions[i] = ((np.random.random()*2)-1, (np.random.random()*2)-1)

    def clone(self):
        clone = Brain(size=len(self.directions))
        clone.directions = self.directions.copy()
        return clone
