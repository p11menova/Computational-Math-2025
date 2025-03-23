from nonlinear_system import solve_nonlinear_system, draw_system_graphics
from nonlinear_equation import simple_iteration, chord_method, newton_method
import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return -1.8 * x ** 3 - 2.94 * x ** 2 + 10.37 * x + 5.38


def phi1(x):
    return 0.174 * x ** 3 + 0.284 * x ** 2 - 0.519


def dphi1_dx(x):
    return 0.174 * 3 * x + 0.284 * 2 * x


def df1_dx(x):
    return -1.8 * 3 * x ** 2 - 2.94 * 2 * x + 10.37


def df1_dx2(x):
    return -1.8 * 6 * x - 2.94 * 2


def f2(x):
    return 2 * x ** 3 + 3.41 * x ** 2 - 23.74 * x + 2.95


def phi2(x):
    return -2 * x ** 3 / 23.74 - 3.41 * x ** 2 / 23.74 - 2.95 / 23.74


def dphi2_dx(x):
    return -2 * 3 / 23.74 * x ** 2 - 3.41 * 2 / 23.74 * x


def df2_dx(x):
    return 6 * x ** 2 + 3.41 * 2 * x - 23.74


def df2_dx2(x):
    return 12 * x + 3.41 * 2


def f3(x):
    return x ** 3 - 3.78 * x ** 2 + 1.25 * x + 3.49


def df3_dx(x):
    return 3 * x ** 2 - 3.78 * 2 * x + 1.25


def df3_dx2(x):
    return 8 * x - 3.78 * 2


def phi3(x):
    return (-x ** 3 + 3.78 * x ** 2 - 3.49) / 1.25


def dphi3_dx(x):
    return -3 / 1.25 * x ** 2 + 3.78 / 1.25 * x


def draw_graphics(num, root_x=None):
    X = np.linspace(-5, 5, 400)

    if num == 1:
        Y = f1(X)
        if root_x: root_y = f1(root_x)
    elif num == 2:
        Y = f2(X)
        if root_x: root_y = f2(root_x)

    else:
        Y = f3(X)
        if root_x: root_y = f3(root_x)

    plt.figure(figsize=(8, 8))

    plt.plot(X, Y, color='cyan')
    if root_x:
        plt.scatter(root_x, root_y, color='hotpink')
        plt.text(root_x + 0.1, root_y + 0.1, f'({round(root_x, 3)}, {round(root_y, 3)})', color='hotpink')

    plt.title('график функции')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.legend(['f(x)', 'root'] if root else ['f(x)'])

    plt.grid(True)
    plt.show()


def solve_with_simple_iteration_method(eq_num):
    correct = False
    while not correct:
        try:
            a0, b0 = map(float, input("введите через пробел границы интервала начального приближения корня:").split())
            correct = a0 < b0

        except Exception:
            print("неет еще раз")
            continue

    if eq_num == 1:
        return simple_iteration(a0, b0, f1, phi1, dphi1_dx)
    elif eq_num == 2:
        return simple_iteration(a0, b0, f2, phi2, dphi2_dx)
    elif eq_num == 3:
        return simple_iteration(a0, b0, f3, phi3, dphi3_dx)


def solve_with_chord_method(eq_num):
    correct = False
    while not correct:
        try:
            a0, b0 = map(float, input("введите через пробел границы интервала начального приближения корня:").split())
            correct = a0 < b0

        except Exception:
            print("неет еще раз")
            continue

    if eq_num == 1:
        return chord_method(a0, b0, f1, df1_dx2)
    elif eq_num == 2:
        return chord_method(a0, b0, f2, df2_dx2)
    elif eq_num == 3:
        return chord_method(a0, b0, f3, df3_dx2)


def solve_with_newton_method(eq_num):
    correct = False
    while not correct:
        try:
            x0 = float(input("введите x0 - начальное приближение:"))
            correct = True

        except Exception:
            print("неет еще раз")
            continue
    if eq_num == 1:
        return newton_method(x0, f1, df1_dx)
    elif eq_num == 2:
        return newton_method(x0, f2, df2_dx)
    elif eq_num == 3:
        return newton_method(x0, f3, df3_dx)


if __name__ == "__main__":
    eq_or_system = input(
        "приви! введите 1, если хотите решить нелинейное уравнение и любой другой символ, если систему:")
    if eq_or_system == '1':
        print("1)\t-1.8x^3 - 2.94x^2 + 10.37x + 5.38 = 0\n")
        print("2)\t2x^3 + 3.41x^2 - 23.74x + 2.95 = 0\n")
        print("3)\tx^3 - 3.78x^2 + 1.25x + 3.49")

        eq_num = int(input("введите номер уравнения, которое хотите решить:"))
        print('1) метод хорд\n2) метод Ньютона\n3) метод простой итерации')
        method_number = int(input("введите номер метода, которым хотите решить уравнение:"))

        root, msg = -1, ''
        if method_number == 1:
            pass
            root, msg = solve_with_chord_method(eq_num)
        elif method_number == 2:
            root, msg = solve_with_newton_method(eq_num)
        else:
            root, msg = solve_with_simple_iteration_method(eq_num)

        if not root:
            print("ERROR:", msg)
            draw_graphics(eq_num)
        else:
            print(msg)
            print(f"SUCCESS: найденный корень уравнения = {round(root, 3)}")

            draw_graphics(eq_num, root)

    else:
        print("1){sin(x+y) = 1.5x - 0.1")
        print("  {x^2+2y^2 =1\n")
        print("2){tg(x+y+0.3) = x^2")
        print("   {0.9x^2+2y^2 = 1\n")

        syst_num = int(input("введите номер системы:"))

        correct = False
        while not correct:
            try:
                a0, b0 = map(float, input("введите начальные приближения a0 b0 через пробел:").split())
                correct = True

            except Exception:
                print("неет еще раз")
                continue

        x_root, y_root, msg = solve_nonlinear_system(a0, b0, syst_num)
        if x_root is None or y_root is None:
            print(msg)
        else:
            print(msg)
            print(f"SUCCESS: найденный корень уравнения = ({round(x_root, 3)}, {round(y_root, 3)})")
            draw_system_graphics(x_root, y_root, syst_num)
