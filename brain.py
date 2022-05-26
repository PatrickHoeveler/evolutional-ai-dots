import numpy as np

class Brain:

    def __init__(self, size: int):
        self.directions = self.get_random_vectors(size, )
        # print('brain initialized with', size, 'directions')
        
    def get_random_vectors(self, size: int):
        # (additive direction between -1 and 1)
        # (90, 80.77)
        vectors  = [((np.random.random()*2)-1, (np.random.random()*2)-1) for _ in range(size)]
        return vectors


