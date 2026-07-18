import argparse
import json
import sys

import matplotlib.pyplot as plt
import numpy as np


def read_json_file(filename):
    """
    Читает данные из JSON-файла формата 4.
    Ожидается структура:
    {
        "x": [x1, x2, ...],
        "y": [y1, y2, ...]
    }
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка: неверный формат JSON-файла: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    if 'x' not in data or 'y' not in data:
        print("Ошибка: файл должен содержать ключи 'x' и 'y'.")
        sys.exit(1)

    x_vals = data['x']
    y_vals = data['y']

    if not x_vals or not y_vals:
        print("Ошибка: массивы x и y не должны быть пустыми.")
        sys.exit(1)

    if len(x_vals) != len(y_vals):
        print("Ошибка: массивы x и y должны иметь одинаковую длину.")
        sys.exit(1)

    return np.array(x_vals), np.array(y_vals)
def apply_thinning(x, y, max_points=1000):
    """
    Применяет прореживание данных (параметр №15).
    Если точек больше max_points, выбираем равномерно каждую N-ю точку.
    """
    if len(x) <= max_points:
        return x, y
    
    step = len(x) // max_points
    if step < 1:
        step = 1
    
    return x[::step], y[::step]
def main():
    parser = argparse.ArgumentParser(
        description="Построение графика функции по данным из JSON-файла. Вариант 14."
    )
    parser.add_argument(
        "input_file",
        help="Имя файла с входными данными в формате JSON"
    )

    # Дополнительный параметр (вариант 14)
    parser.add_argument(
        "--fill",
        action="store_true",
        help="Включить заливку цветом под кривой графика"
    )

    args = parser.parse_args()
# Чтение данных
    x_full, y_full = read_json_file(args.input_file)

    # Применяем прореживание (параметр №15) - автоматически
    x, y = apply_thinning(x_full, y_full)

    print(f"Загружено точек: {len(x_full)}")
    print(f"После прореживания: {len(x)}")

    # Создаём график
    fig, ax = plt.subplots(figsize=(10, 6))

    # Построение с заливкой или без (параметр №14)
    if args.fill:
        ax.fill_between(x, y, color='blue', alpha=0.3, label="Заливка под кривой")
        ax.plot(x, y, color='blue', linewidth=2, label="f(x)")
        title_suffix = " (с заливкой)"
    else:
        ax.plot(x, y, color='blue', linewidth=2, label="f(x)")
        title_suffix = ""

