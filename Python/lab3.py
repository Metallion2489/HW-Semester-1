import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Определение функции для системы уравнений
def f1(t, y):
    X, Y, Z = y
    return [1.5 * X + Y - X * Z, -X, -0.2 * Z + 0.2 * np.sign(X) * X**2]

# Интервал времени и начальные условия
te = np.linspace(0, 10, 10001)
yi = [3, 3, 0]  # начальные условия для X, Y, Z

# Решение задачи Коши
r1s = solve_ivp(f1, (0, 10), yi, method="RK45", t_eval=te)

# Визуализация траекторий
plt.plot(r1s.y[0], r1s.y[1], label="Траектория")  # X и Y
plt.xlabel('x')
plt.ylabel('y')
plt.title('Визуализация траектории')
plt.legend()
plt.grid()
plt.show()