# Ваше решение
from typing import Callable

def quadratic_solver(a: float, b: float, c: float) -> Callable[[float], str]:
    """
    Возвращает замыкание для решения квадратного уравнения a*x^2 + b*x + c = 0.

    Параметры:
        a (float): Коэффициент при x^2.
        b (float): Коэффициент при x.
        c (float): Свободный член.

    Возвращает:
        Callable[[float], str]: Функция, принимающая значение x и вычисляющая значение уравнения.
    """
    def solve(x: float) -> str:
        D = b**2 - 4*a*c
        if D <= 0:
            return f"Результата не будет, потому что D = {D}"
        return f"Для x = {x}, значение уравнения: {a * x**2 + b * x + c}"

    return solve

# Пример использования
a, b, c = 1, -3, 2
solver = quadratic_solver(a, b, c)
print(solver(1))  # Для примера с x = 1
print(solver(2))  # Для примера с x = 2
