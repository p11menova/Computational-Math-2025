from math import sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt

MAX_ITER = 1000


def system1_f(x, y):
    return sin(x + y) - 1.5 * x + 0.1


def system1_g(x, y):
    return x ** 2 + 2 * y ** 2 - 1


def dfdx1(x, y):
    return cos(x + y) - 1.5


def dfdy1(x, y):
    return cos(x + y)


def dgdx1(x, y):
    return 2 * x


def dgdy1(x, y):
    return 4 * y


def system2_f(x, y):
    return tan(x * y + 0.3) - x ** 2


def system2_g(x, y):
    return 0.9 * x ** 2 + 2 * y ** 2 - 1


def dfdx2(x, y):
    return -2 * x + y / (cos((10 * y * x + 3) / 10)) ** 2


def dfdy2(x, y):
    return x / (cos((10 * x * y * 3) / 10)) ** 2


def dgdx2(x, y):
    return 1.8 * x


def dgdy2(x, y):
    return 4 * y


def solve_linear_system(M) -> (float, float):
    A = np.array([[M[0][0], M[0][1]], [M[1][0], M[1][1]]])
    B = np.array([M[0][2], M[1][2]])

    try:
        solution = np.linalg.solve(A, B)
        return solution
    except np.linalg.LinAlgError:
        return None, None


def print_M(M):
    for i in M:
        for j in i:
            print(str(round(j, 4)).center(6), end=" ")
        print()


def draw_system_graphics(root_x, root_y, num):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)

    X, Y = np.meshgrid(x, y)

    if num == 1:
        Z1 = np.sin(X + Y) - (1.5 * X - 0.1)
        Z2 = X ** 2 + 2 * Y ** 2 - 1

    else:
        Z1 = np.tan(X * Y + 0.3) - x ** 2
        Z2 = 0.9 * X ** 2 + 2 * Y ** 2 - 1

    plt.figure(figsize=(8, 8))

    f_label = 'sin(x+y) - 1.5x + 0.1' if num == 1 else 'tg(xy + 0.3) -x^2'
    g_label = 'x^2+2y^2-1' if num == 1 else '0.9x^2 + 2y^2 - 1'

    plt.contour(X, Y, Z1, levels=[0], colors='cyan')
    plt.contour(X, Y, Z2, levels=[0], colors='hotpink')
    plt.scatter(root_x, root_y, color='hotpink')
    plt.text(root_x + 0.1, root_y + 0.1, f'({round(root_x, 3)}, {round(root_y, 3)})', color='hotpink')

    plt.title('графики системы уравнений')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.legend(['root', f_label, g_label])

    plt.grid(True)
    plt.show()


def solve_nonlinear_system(x0, y0, num) -> (float, float, str):
    x, y = x0, y0
    result_msg = ''
    iter_count = 1

    while (x == x0 and y == y0) or (abs(x0 - x) >= 0.01 or abs(y0 - y) >= 0.01):
        if iter_count == MAX_ITER:
            return None, None, "превышено максимальное количество итераций"
        if num == 1:
            M = [
                [dfdx1(x, y), dfdy1(x, y), -1 * system1_f(x, y)],
                [dgdx1(x, y), dgdy1(x, y), -1 * system1_g(x, y)]
            ]  # якобиан системы
        else:
            M = [
                [dfdx2(x, y), dfdy2(x, y), -1 * system2_f(x, y)],
                [dgdx2(x, y), dgdy2(x, y), -1 * system2_g(x, y)]
            ]  # якобиан системы

        delta_x, delta_y = solve_linear_system(M)
        if not delta_x or not delta_x:
            return None, None, "система не имеет решений("

        x0, y0 = x, y
        x = x0 + delta_x
        y = y0 + delta_y

        result_msg += ''.join(
            [i.center(15) for i in f"№={iter_count} delta_x={round(delta_x, 3)} delta_y={round(delta_y, 3)} "
                                   f"x={round(x, 3)} y={round(y, 3)}".split()]) + "\n"
        iter_count += 1
    return x, y, result_msg

# solve_nonlinear_system(1, 0.5, 1)
# solve_nonlinear_system(-1,-1,1)
# solve_nonlinear_system(-1, -1, 2)

# polovina(-3.66, -2.66)
# iteracia(-0.96)

# secant(1.49, 2.49)
