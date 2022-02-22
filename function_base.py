from matplotlib import pyplot as plt  # 그래프 라이브러리
import numpy  # 수학 관련 라이브러리


def f(x):
    return 2*x+1
def muri(X):
    if x < 0:
        return None
    else:
        return (2*x)**.5


x = []  # 정의역 집합 선언
y = []  # 치역 집합 선언

for i in numpy.arange(-10, 10, 0.001):  # 정의역 : -10~10의 범위
    x.append(i)  # 정의역 집합에 정의역 입력
    y.append(muri(i))  # 치역 집합에 함숫값 입력
    # 그래프 관련 설정
plt.figure(figsize=(7, 7))  # 그래프 창 크기
plt.axis([-5, 5, -0.5, 10])  # 그래프 숫자 범위
plt.grid(True)  # 그래프 격자 그리기
plt.title('jugi hamsu')  # 그래프 위에 제목 쓰기
plt.plot([-50, 50], [0, 0], color='black')  # x축 그리기
plt.plot([0, 0], [-50, 50], color='black')  # y축 그리기
plt.plot(x2, y2, color='red')
plt.plot(x, y, color='blue')  # 입력한 값들 그래프에 표현
plt.show()  # 그래프 실행
