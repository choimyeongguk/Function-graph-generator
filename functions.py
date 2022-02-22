from matplotlib import pyplot as plt
import numpy
import math


def f_linear(x):
    return 2*x+1


def f_quadratic(x):
    return (x-2)**2-1


def f_cubic(x):
    return (x+3)*(x-1)**2


def f_quaternary(x):
    return (x-1)*(x-2)*(x-3)**2+2


def f_abs(x):
    if x <= 0:
        x = -1*x
    return x


def f_M(x):
    if (0 <= x < 0.5):
        return x*4
    elif(0.5 <= x < 1):
        return -x*2+3
    elif(1 <= x < 1.5):
        return None
    elif(1.5 <= x <= 2):
        return -1*x*4+8


def f_G(x):
    if (0 <= x < 2):
        return -x+5
    elif (2 <= x < 3):
        return 3
    elif (3 <= x < 4):
        return -x+6
    else:
        return x-2


def f_H(x):
    if (0 <= x < 1):
        return 3*x+1
    elif(1 <= x < 3):
        return -x+5
    elif(3 <= x < 4):
        return -2*x+8
    else:
        return 3*x-12


def f_gauss(x):
    return math.floor(x)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def jugi(x):
    if (x < -2 or x > 2):
        while (-2 <= x <= 2):
            if (x < -2):
                x += 4
            if (x > 2):
                x -= 4
    else:
        if (0 <= x <= 2):
            return -1*x**2+2*x
        if (-2 <= x < 0):
            return x**2+2*x


x_ori = []
y_ori = []
x_com = []
y_com = []
x = []
y = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

for i in numpy.arange(-10, 10, 0.001):
    x_ori.append(i)
    y_ori.append(f_M(i))
for i in numpy.arange(-10, 10, 0.001):
    x_com.append(i)
    y_com.append(f_M(f_M(i)))

# for i in numpy.arange(-10, 10, 0.001):
#     if 0<=i<=1 or i>=3:
#         x.append(i)
#     else:
#         x.append(None)
#     y.append(f_quadratic(i))
# for i in numpy.arange(-10, 10, 0.001):
#     x2.append(i)
#     if 0<=i <= 1 or i >= 3:
#         y2.append(-1*f_quadratic(i))
#     else:
#         y2.append(None)
# for i in numpy.arange(-10, 10, 0.001):
#     if 0 <= i <= 1 or i >= 3:
#         x3.append(-1*i)
#         y3.append(f_quadratic(i))
#     else:
#         x3.append(None)
#         y3.append(None)
# for i in numpy.arange(-10, 10, 0.001):
#     if 0 <= i <= 1 or i >= 3:
#         x4.append(-1*i)
#         y4.append(-1*f_quadratic(i))
#     else:
#         x4.append(None)
#         y4.append(None)

plt.figure(figsize=(7, 7))
plt.axis([-10, 10, -10, 10])
plt.grid(True)
plt.title('f(x) = (x-2)^2-1')
plt.plot([-50, 50], [0, 0], color='black')
plt.plot([0, 0], [-50, 50], color='black')
plt.plot(x_com, y_com, color='red')
plt.plot(x_ori, y_ori, color='blue')

plt.plot(x, y)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.show()
