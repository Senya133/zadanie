import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    return 0.5 * ((x1**4 - 16*x1**2 + 5*x1) + (x2**4 - 16*x2**2 + 5*x2))

x1 = np.linspace(-5, 5, 200)
x2 = np.linspace(-5, 5, 200)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

x10, x20 = -2.903534, -2.903534
y0 = f(x10, x20)

print("РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ")
print(f"Тестовая точка: x1 = {x10:.6f}, x2 = {x20:.6f}")
print(f"Значение функции: f(x1, x2) = {y0:.10f}")

fig = plt.figure(figsize=(14, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(X1, X2, Y, cmap='viridis')
ax1.set(xlabel='x1', ylabel='x2', zlabel='y', title='3D поверхность')

ax2 = fig.add_subplot(2, 2, 2)
cf = ax2.contourf(X1, X2, Y, 50, cmap='viridis')
ax2.set(xlabel='x1', ylabel='x2', title='Вид сверху')
plt.colorbar(cf, ax=ax2)

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x1, f(x1, x20))
ax3.axvline(x10, color='r', linestyle='--', label=f'x1={x10:.3f}')
ax3.axhline(y0, color='g', linestyle='--', label=f'y={y0:.3f}')
ax3.set(xlabel='x1', ylabel='y', title=f'Сечение при x2={x20:.3f}')
ax3.grid(True)
ax3.legend()

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x2, f(x10, x2))
ax4.axvline(x20, color='r', linestyle='--', label=f'x2={x20:.3f}')
ax4.axhline(y0, color='g', linestyle='--', label=f'y={y0:.3f}')
ax4.set(xlabel='x2', ylabel='y', title=f'Сечение при x1={x10:.3f}')
ax4.grid(True)
ax4.legend()

plt.suptitle(f'Тестовая точка: ({x10:.4f}, {x20:.4f}), f = {y0:.6f}', fontsize=12)
plt.tight_layout()
plt.show()
