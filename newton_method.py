import numpy as np


##

def measure(x):
    # returns 1st norm of a vector (avg)
    sum = 0
    for _ in x:
        sum += abs(_)
    return sum / len(x)


def newton_method(f1, f2, df1_dx1, df1_dx2, df2_dx1, df2_dx2, x1_init, x2_init):
    x = np.array([x1_init, x2_init])

    eps = 0.01
    ms = eps
    while ms >= eps:
        # A - Jacobian matrix of f1, f2
        # f(x) + A(x)*dx = 0 <=> A(x)*dx = -f(x)
        A = np.array([[df1_dx1(x[0]), df1_dx2(x[1])],
                      [df2_dx1(x[0]), df2_dx2(x[1])]])
        dx = np.linalg.solve(A, np.array([-f1(x[0], x[1]),
                                          -f2(x[0], x[1])]))
        x = x + dx
        ms = measure(dx)

    return x
