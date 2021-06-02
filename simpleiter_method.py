import numpy as np

def simpleiter_method(x1f, x2f, x1_init, x2_init):

    x = np.array([x1_init, x2_init])

    eps = 0.00001
    ms = eps
    while ms >= eps:
        [x1_, x2_] = x
        x = [x1f(x2_), x2f(x1_)]
        ms = max(abs(x[0]-x1_), abs(x[1]-x2_))

    return x

