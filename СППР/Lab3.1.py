from scipy.optimize import minimize

# Целевая функция
def objective(x):
    return ((x[0]-4)**2 + (x[1]-3)**2)  # Например, минимизируем - (x1^2 + x2^2)

# Определяем ограничения
constraints = [
    {'type': 'ineq', 'fun': lambda x: (2*x[0] + 3*x[1])-6},  # 2x1 + 3x2 >= 6
    {'type': 'ineq', 'fun': lambda x: x[0]},               # x1 >= 0
    {'type': 'ineq', 'fun': lambda x: x[1]},               # x2 >= 0
    {'type': 'ineq', 'fun': lambda x: 18 -(3*x[0] - 2*x[1])},  # 3x1 - 2x2 <= 18
    {'type': 'ineq', 'fun': lambda x: 8 -(-x[0] + 2*x[1])},  # -x1 + 2x2 <= 8
]

# Начальное приближение
initial_guess = [1, 1]

# Решение задачи оптимизации
solution = minimize(objective, initial_guess, constraints=constraints)

# Вывод результата
if solution.success:
    print("Оптимальное значение функции:", -solution.fun)  # Для максимума берем отрицательное значение
    print("Значения переменных:", solution.x)
else:
    print("Решение не найдено")
