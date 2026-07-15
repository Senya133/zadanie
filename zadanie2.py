import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===============================
# Вариант 15: f(x1, x2) = 0.5 * sum_{i=1}^{D} (x_i^4 - 16*x_i^2 + 5*x_i), D = 2
# ===============================

def f(x1, x2):
    D = 2
    # Суммируем по i=1..2
    sum_val = (x1**4 - 16*x1**2 + 5*x1) + (x2**4 - 16*x2**2 + 5*x2)
    return 0.5 * sum_val

# Параметры
x1_min, x1_max = -5.0, 5.0
x2_min, x2_max = -5.0, 5.0
x10, x20 = -2.903534, -2.903534  # тестовая точка

# Шаг дискретизации для гладкости
step = 0.05
x1_vals = np.arange(x1_min, x1_max + step, step)
x2_vals = np.arange(x2_min, x2_max + step, step)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Y = f(X1, X2)

# Значение функции в тестовой точке
y0 = f(x10, x20)

# ===============================
# Построение 4-х графиков
# ===============================
fig = plt.figure(figsize=(14, 10))

# 1. 3D поверхность (изометрический вид)
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
surf = ax1.plot_surface(X1, X2, Y, cmap='viridis', edgecolor='none', alpha=0.9)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y=f(x1, x2)')
ax1.set_title('Изометрический вид')
ax1.view_init(elev=30, azim=-60)

# 2. "Вид сверху" (контурный график)
ax2 = fig.add_subplot(2, 2, 2)
contour = ax2.contourf(X1, X2, Y, levels=50, cmap='viridis')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_title('Вид сверху (контуры)')
plt.colorbar(contour, ax=ax2, label='y=f(x1, x2)')

# 3. График y = f(x1) при x2 = x20
ax3 = fig.add_subplot(2, 2, 3)
y_x1 = f(x1_vals, x20)
ax3.plot(x1_vals, y_x1, 'b-', linewidth=2)
ax3.axvline(x=x10, color='r', linestyle='--', linewidth=1, label=f'x10 = {x10:.4f}')
ax3.axhline(y=y0, color='g', linestyle='--', linewidth=1, label=f'y0 = {y0:.4f}')
ax3.set_xlabel('x1')
ax3.set_ylabel('y = f(x1, x2=' + f'{x20:.4f})')
ax3.set_title(f'Сечение при x2 = {x20:.4f}')
ax3.grid(True)
ax3.legend()

# 4. График y = f(x2) при x1 = x10
ax4 = fig.add_subplot(2, 2, 4)
y_x2 = f(x10, x2_vals)
ax4.plot(x2_vals, y_x2, 'b-', linewidth=2)
ax4.axvline(x=x20, color='r', linestyle='--', linewidth=1, label=f'x20 = {x20:.4f}')
ax4.axhline(y=y0, color='g', linestyle='--', linewidth=1, label=f'y0 = {y0:.4f}')
ax4.set_xlabel('x2')
ax4.set_ylabel('y = f(x1=' + f'{x10:.4f}' + ', x2)')
ax4.set_title(f'Сечение при x1 = {x10:.4f}')
ax4.grid(True)
ax4.legend()

# ===============================
# Вывод координат тестовой точки и значения функции
# ===============================
info_text = f'Тестовая точка: (x10, x20) = ({x10:.4f}, {x20:.4f})\nf(x10, x20) = {y0:.6f}'
fig.suptitle(info_text, fontsize=14, color='darkblue')

plt.tight_layout()
plt.show()
