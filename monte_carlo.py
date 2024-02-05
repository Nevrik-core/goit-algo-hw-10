import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def func (x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def monte_carlo_integrate(func, a, b, y_min, y_max, num_points=1000000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(y_min, y_max, num_points)
    under_curve = y_random < func(x_random)
    return np.mean(under_curve) * (b - a) * (y_max - y_min)


result_quad, error_quad = integrate.quad(func, a, b)

y_min = 0
y_max = func(b)
result_monte_carlo = monte_carlo_integrate(func, a, b, y_min, y_max)

# Виведення результатів
print(f"Інтеграл за допомогою quad: {result_quad}")
print(f"Інтеграл методом Монте-Карло: {result_monte_carlo}")


# Візуалізація
# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = func(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = func(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()