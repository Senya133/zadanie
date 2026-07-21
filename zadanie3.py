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
    # Проверяем наличие ключей 'x' и 'y'
    if 'x' not in data or 'y' not in data:
        print("Ошибка: файл должен содержать ключи 'x' и 'y'.")
        print("Текущие ключи:", list(data.keys()))
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


def main():
    parser = argparse.ArgumentParser(
        description="Построение графика функции по данным из JSON-файла. Вариант 14."
    )
    parser.add_argument(
        "input_file",
        help="Имя файла с входными данными в формате JSON"
    )
    parser.add_argument(
        "--fill",
        action="store_true",
        help="Включить заливку цветом под кривой графика"
    )
    args = parser.parse_args()
    x, y = read_json_file(args.input_file)
    print(f"Загружено точек: {len(x)}")
    fig, ax = plt.subplots(figsize=(10, 6))

    if args.fill:
        ax.fill_between(x, y, color='blue', alpha=0.3, label="Заливка под кривой")
        ax.plot(x, y, color='blue', linewidth=2, label="f(x)")
        title_suffix = " (с заливкой)"
    else:
        ax.plot(x, y, color='blue', linewidth=2, label="f(x)")
        title_suffix = ""
    ax.set_title(
        f"График функции f(x) = 100·√(1-0.01·x²) + 0.01·|x+10|\n"
        f"(данные из: {args.input_file}){title_suffix}"
    )
    
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
