from matplotlib import pyplot as plt
import numpy
import math


def f_gauss_linear(x):
    return math.floor(x)


def f_gauss_linear_abs(x):
    if x < 0:
        return -math.floor(x)
    else:
        return math.floor(x)


def f_gauss_quadratic(x):
    return f_quadratic(x)-math.floor(f_quadratic(x))


def f_gauss_quadratic_2(x):
    return f_quadratic(f_quadratic(x))-math.floor(f_quadratic(f_quadratic(x)))


def f_gauss_cubic(x):
    return x**3-math.floor(x**3)


def f_quadratic(x):
    return 1/2*(x-2)**2-1


def f_abs(x):
    if x < 0:
        return -x
    else:
        return x


x_ori = []
y_ori = []
x_com = []
y_com = []
count = 0
for i in numpy.arange(-10, 10, 0.0001):
    x_ori.append(i)
    y_ori.append(f_quadratic(f_quadratic(i)))
for i in numpy.arange(-10, 10, 0.0001):
    x_com.append(i)
    y_com.append(f_quadratic(f_quadratic(i)) -
                 math.floor(f_quadratic(f_quadratic(i))))
plt.figure(figsize=(7, 7))
plt.axis([-2, 10, -2, 5])
plt.grid(True)
plt.title('f(x) = 1/2(x-2)^2-1')
plt.plot([-50, 50], [0, 0], color='black')
plt.plot([0, 0], [-50, 50], color='black')
plt.scatter(x_ori, y_ori, c='blue', s=1)
plt.scatter(x_com, y_com, c='red', s=1)
plt.show()



