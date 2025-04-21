import math

import numpy as np
from math import exp, log

def count_sums_1(n, X, Y):
    S_X = sum(X)
    S_Y = sum(Y)
    S_XX = sum(map(lambda x: x ** 2, X))
    S_XY = sum([X[i] * Y[i] for i in range(n)])
    return S_X, S_Y, S_XX, S_XY


def count_sums_2(n, X, Y):
    S_X3 = sum(map(lambda x: x ** 3, X))
    S_X2Y = sum([X[i] ** 2 * Y[i] for i in range(n)])
    S_X4 = sum(map(lambda x: x ** 4, X))
    return S_X3, S_X2Y, S_X4


def count_sums_3(n, X, Y):
    S_X5 = sum(map(lambda x: x ** 5, X))
    S_X3Y = sum([X[i] ** 3 * Y[i] for i in range(n)])
    S_X6 = sum(map(lambda x: x ** 6, X))
    return S_X5, S_X6, S_X3Y


def linear_approximation(n, X, Y) -> (float, float):
    """
    :return: коэффиценты a b аппроксимирующей функции ax+b
    """
    S_X, S_Y, S_XX, S_XY = count_sums_1(n, X, Y)

    # получим сист лин уравн и по правилу Крамера посчитаем
    delta = S_XX * n - S_X ** 2
    delta_1 = S_XY * n - S_X * S_Y
    delta_2 = S_XX * S_Y - S_X * S_XY

    return delta_1 / delta, delta_2 / delta


def solve_linear_system(A, B):
    A = np.array(A)
    B = np.array(B)
    try:
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError:
        return None, None


def quadratic_approximation(n, X, Y) -> (float, float, float):
    """
    :return: коэффиценты a b c аппроксимирующей функции ax^2 + bx +c
    """
    S_X, S_Y, S_X2, S_XY = count_sums_1(n, X, Y)
    S_X3, S_X2Y, S_X4 = count_sums_2(n, X, Y)
    A = [[n, S_X, S_X2],
         [S_X, S_X2, S_X3],
         [S_X2, S_X3, S_X4]]
    B = [S_Y, S_XY, S_X2Y]

    a, b, c = solve_linear_system(A, B)[::-1]

    return a, b, c


def cubic_approximation(n, X, Y) -> (float, float, float, float):
    """
    :return: коэффиценты a b c d аппроксимирующей функции ax^3 + bx^2 +cx = d
    """
    S_X, S_Y, S_X2, S_XY = count_sums_1(n, X, Y)
    S_X3, S_X2Y, S_X4 = count_sums_2(n, X, Y)
    S_X5, S_X6, S_X3Y = count_sums_3(n, X, Y)
    A = [
        [S_X6, S_X5, S_X4, S_X3],
        [S_X5, S_X4, S_X3, S_X2],
        [S_X4, S_X3, S_X2, S_X],
        [S_X3, S_X2, S_X, n]
    ]

    B = [S_X3Y, S_X2Y, S_XY, S_Y]
    return solve_linear_system(A, B)


def exponential_approximation(n, X, Y):
    """
    :return: коэфф a, b функции ae^bx
    """
    clean_X = []
    clean_Y = []

    for x, y in zip(X, Y):
        if y is not None and y > 0:  # Явная проверка
            clean_X.append(x)
            clean_Y.append(y)

    if len(clean_Y) < 2:  # Для линейной регрессии нужно минимум 2 точки
        return None, None, None, None

    try:
        lnY = [math.log(y) for y in clean_Y]  # Более питонический способ
        B, A = linear_approximation(len(lnY), clean_X, lnY)
        return math.exp(A), B, clean_X, clean_Y
    except (ValueError, TypeError):
        return None, None, None, None

def logarithm_approximation(n, X, Y):
    clean_X = []
    clean_Y = []

    for x, y in zip(X, Y):
        if x is not None and y is not None and x > 0:  # ln(x) определен только для x > 0
            clean_X.append(x)
            clean_Y.append(y)

    if len(clean_X) < 2:
        return None, None, None, None

    try:
        # линеаризация - заменяем x на ln(x)
        lnX = [math.log(x) for x in clean_X]

        # y = a*lnX + b
        a, b = linear_approximation(len(lnX), lnX, clean_Y)

        return a, b, clean_X, clean_Y

    except (ValueError, TypeError, ZeroDivisionError):
        return None, None, None, None


def pow_approximation(n, X, Y):
    clean_X = []
    clean_Y = []

    for x, y in zip(X, Y):
        if x is not None and y is not None and x > 0 and y > 0:
            clean_X.append(x)
            clean_Y.append(y)

    if len(clean_X) < 2:
        return None, None, None, None

    try:
        # Линеаризация
        lnX = [math.log(x) for x in clean_X]
        lnY = [math.log(y) for y in clean_Y]

        # Линейная регрессия: lnY = ln(a) + b*lnX
        b, ln_a = linear_approximation(len(lnX), lnX, lnY)
        a = math.exp(ln_a)

        return a, b, clean_X, clean_Y

    except (ValueError, TypeError, ZeroDivisionError):
        return None, None, None, None