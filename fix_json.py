import json
import math
import os

# Создаём папку results
os.makedirs("results", exist_ok=True)

def f(x):
    """Функция из варианта 3"""
    return 100 * math.sqrt(1 - 0.01 * x**2) + 0.01 * abs(x + 10)

# Генерируем данные в правильном формате
x_vals = []
y_vals = []

x = -15.0
step = 0.01

while x <= 5.0:
    try:
        y = f(x)
        x_vals.append(round(x, 4))
        y_vals.append(round(y, 6))
    except:
        pass
    x += step

# Формат 4: два массива
data = {
    "x": x_vals,
    "y": y_vals
}

# Сохраняем
with open("results/result_variant_3.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Создано точек: {len(x_vals)}")
print("Файл сохранён: results/result_variant_3.json")
print("\nПервые 5 точек:")
for i in range(5):
    print(f"x = {x_vals[i]}, y = {y_vals[i]}")
