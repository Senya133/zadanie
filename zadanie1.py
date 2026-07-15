import os
import json
import numpy as np
import matplotlib.pyplot as plt

# Функция для варианта 3 (с защитой от отрицательных значений под корнем)
def f(x):
    # Используем np.abs для защиты, чтобы функция была определена везде
    return 100 * np.sqrt(np.abs(1 - 0.01 * x**2)) + 0.01 * np.abs(x + 10)

# Интервал из задания
x_min, x_max = -15, 5
x_vals = np.linspace(x_min, x_max, 1000)
y_vals = f(x_vals)

# Создание папки results
os.makedirs("results", exist_ok=True)

# Сохранение в JSON
data = [{"x": round(x, 4), "y": round(y, 4)} for x, y in zip(x_vals, y_vals)]
with open("results/result_variant_3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Сохранено {len(x_vals)} точек")

# График
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, linewidth=2, color='blue')
plt.title(r'$f(x)=100\sqrt{|1-0.01x^2|}+0.01|x+10|$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(x_min, x_max)
plt.tight_layout()
plt.savefig('plot.png', dpi=300)
plt.show()

# Вывод первых 20 строк
print("\nПервые 20 строк:")
with open("results/result_variant_3.json", "r") as f:
    for i, line in enumerate(f):
        if i >= 20:
            break
        print(line.strip())
