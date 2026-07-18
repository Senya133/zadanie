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


