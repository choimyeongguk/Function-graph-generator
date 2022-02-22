from matplotlib import pyplot as plt
import numpy
import math

global a
a_square = 5.5
a = math.sqrt(a_square)


def f(x):
    if x < -2:
        while x < -2:
            x += 4
    elif x > 2:
        while x > 2:
            x -= 4
    else:
        x

    if 0 <= x <= 2:
        return -1*x**2+2*x
    if -2 <= x < 0:
        return x**2+2*x


def g(x):
    global a
    if x >= 0:
        return (x-a)**2-a**2
    else:
        return a**2-(x+a)**2


x_f = []; y_f = []
x_g = []; y_g = []
x_fus = []; y_fus = []

for i in numpy.arange(-10, 10, 0.0001):
    x_f.append(i)
    y_f.append(f(i))

for i in numpy.arange(-10, 10, 0.0001):
    x_g.append(i)
    y_g.append(g(i))

for i in numpy.arange(-10, 10, 0.0001):
    x_fus.append(i)
    if -a <= i <= 2*a:
        y_fus.append(f(g(i)))
    else:
        y_fus.append(None)

plt.figure(figsize=(14, 7))
plt.axis([-10, 10, -5, 5])
plt.grid(True)
plt.title('a^2=%.2lf' % a_square)
plt.plot([-10, 10], [0, 0], color='black')
plt.plot([0, 0], [-10, 10], color='black')
plt.plot([-10, 10], [1, 1], color='gray')
plt.plot([-a, -a], [-10, 10], color='gray')
plt.plot([2*a, 2*a], [-10, 10], color='gray')
plt.plot(x_f, y_f, color='blue')
plt.plot(x_g, y_g, color="green")
plt.plot(x_fus, y_fus, color='red', linewidth=5)
plt.show()
