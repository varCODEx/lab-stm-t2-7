import numpy as np
import matplotlib.pyplot as plt
from newton_method import newton_method
from simpleiter_method import simpleiter_method


##
# 12

# x1 - cosx2 = 3
# x2 - sinx1 = 3
# <=>
# x1 - cos x2 - 3 = 0
# x2 - sin x1 - 3 = 0

def x1(x2):
    return np.cos(x2) + 3
    # return np.arcsin(x2-3)


def x2(x1):
    return np.sin(x1) + 3
    # return np.arccos(x1-3)


def f1(x1, x2):
    return x1 - np.cos(x2) - 3


def f2(x1, x2):
    return x2 - np.sin(x1) - 3


def df1_dx1(x):
    return 1


def df1_dx2(x):
    return np.sin(x)


def df2_dx2(x):
    return 1


def df2_dx1(x):
    return -np.cos(x)


##
x1_init = 3
x2_init = 4
##

xi = np.arange(-10, 10, 0.1)
xi_ = []
for xx in xi:
    xi_.append(x1(xx))
plt.plot(xi_, xi)
xi_ = []
for xx in xi:
    xi_.append(x2(xx))
plt.plot(xi_, xi)

x = newton_method(f1, f2, df1_dx1, df1_dx2, df2_dx1, df2_dx2, x1_init, x2_init)
print("newton method")
print("x: ", x)
print("f1(x) = ", f1(x[0], x[1]))
print("f2(x) = ", f2(x[0], x[1]))
print()
x = simpleiter_method(x1, x2, x1_init, x2_init)
print("simpleiter method")
print("x: ", x)
print("f1(x) = ", f1(x[0], x[1]))
print("f2(x) = ", f2(x[0], x[1]))
plt.show()
