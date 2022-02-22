from matplotlib import pyplot as plt
import numpy


def E(x):
    if -2.5 <= x <= 2.5:
        return 0.64*x**2-7.5
    else:
        return None


def D(x):
    if -2.5 <= x <= 2.5:
        return -0.64*x**2+7.5
    else:
        return None


def N(x):
    if -2.5 <= x <= 2.5:
        return -x


x = []
y = []
x2 = []
y2 = []
x3 = []
y3 = []
for i in numpy.arange(-10, 10, 0.001):
    x.append(i)
    y.append(N(i))

for i in numpy.arange(-10, 10, 0.001):
    x2.append(i)
    if -2.5 <= i <= 2.5:
        y2.append(E(i))
    else:
        y2.append(None)
for i in numpy.arange(-10, 10, 0.001):
    x3.append(i)
    if -2.5 <= i <= 2.5:
        y3.append(D(i))
    else:
        y3.append(None)


plt.figure(figsize=(7, 7))  # 그래프 창 크기
plt.axis([-8, 8, -8, 8])  # 그래프 숫자 범위
plt.grid(True)  # 그래프 격자 그리기
plt.title('THANK YOU')  # 그래프 위에 제목 쓰기

plt.plot(x, y, color='blue', linewidth=5)
plt.plot([-7.5, -3.5], [0, 0], color='red', linewidth=5)
plt.plot(y2, x2, color='red', linewidth=5)
plt.plot([-2.5, -2.5], [-2.5, 2.5], color='blue', linewidth=5)
plt.plot([2.5, 2.5], [-2.5, 2.5], color='blue', linewidth=5)
plt.plot(y3, x3, color='yellow', linewidth=5)
plt.plot([3.5, 3.5], [-2.5, 2.5], color='yellow', linewidth=5)
plt.show()  # 그래프 실행
