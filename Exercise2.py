import numpy as np
import scipy.integrate as spi

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0
b = 2

# Кількість випадкових точок
num_points = 100000

# Генерація випадкових точок в проміжку [a, b]
random_points = np.random.uniform(a, b, num_points)

# Обчислення значення функції в кожній точці
function_values = f(random_points)

# Обчислення середнього значення функції та множимо на ширину інтервалу
monte_carlo_result = np.mean(function_values) * (b - a)

# Використання функції quad для аналітичного розрахунку інтегралу
analytical_result, _ = spi.quad(f, a, b)

print("Значення інтеграла методом Монте-Карло:", monte_carlo_result)
print("Значення інтеграла аналітично:", analytical_result)

# Порівняння результатів
relative_error = abs(monte_carlo_result - analytical_result) / analytical_result * 100
print("Відносна похибка:", relative_error, "%")