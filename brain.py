import numpy as np

class Brain:

    def __init__(self, size: int, stepsize: int):
        self.stepsize = stepsize
        self.directions = self.get_random_vectors(size, stepsize)
        print('brain initialized with', size, 'directions and a stepsize of', stepsize)
        
    def get_random_vectors(self, size: int, stepsize: int):
        # (forward step, degree)
        # (90, 80.77)
        vectors  = [(int(np.random.random()*stepsize), np.random.random()*360) for _ in range(size)]
        return vectors


