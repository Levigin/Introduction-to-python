import functools
import json
import csv
import random


def generate_csv(string_q: int, left: int, right: int):
    with open('info.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for _ in range(1, string_q + 1):
            row = [random.randint(left, right + 1) for _ in range(3)]
            writer.writerow(row)


def cycle_call_param(string_q: int, left: int, right: int):
    def cycle_call(func):
        roots = {}
        generate_csv(string_q, left, right)

        def wrapper():
            with open('info.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect='excel')
                for i, row in enumerate(reader):
                    if row:
                        a, b, c = row
                        roots[i // 2] = str(func(int(a), int(b), int(c)))

            return roots

        return wrapper

    return cycle_call


def generate_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('info.json', 'w') as f:
            json.dump(result, f, separators=('\n', ' '))

    return wrapper


@generate_json
@cycle_call_param(100, 100, 1000)
def solve_expr(a: int, b: int, c: int):
    d = (b ** 2 - 4 * a * c) ** 0.5
    x1, x2 = (-b + d) / (2 * a), (-b - d) / (2 * a)

    return x1, x2 if x1 != x2 else x1


solve_expr()
solve_expr()
