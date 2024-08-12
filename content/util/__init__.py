
import random as rnd

def bernoulli(p):
    assert p >= 0 and p <= 1, \
        f'{p} is not a valid parameter for the bernoulli distribution.'
    
    return 1 if rnd.random() <= p else 0