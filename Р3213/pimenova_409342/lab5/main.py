import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from interpolation_methods import *
matplotlib.use('TkAgg')


def main():
    def input_table_manual():
        n = int(input("введите количество точек: "))
        x, y = [], []
        for i in range(n):
            xi = float(input(f"x[{i}]: "))
            yi = float(input(f"y[{i}]: "))
            x.append(xi)
            y.append(yi)
        return x, y

    def input_table_file(path):
        x, y = [], []
        try:
            with open(path, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
            return x, y
        except FileNotFoundError:
            return None, None

    def input_table_function():
        import math
        print("1 - sin(x)\n2 - cos(x)\n3 - ln(1 + x)")
        f_choice = int(input("выберите функцию: "))
        func = {1: math.sin, 2: math.cos, 3: lambda x: math.log(1 + x)}[f_choice]

        while True:
            a = float(input("введите начало интервала: "))
            b = float(input("введите конец интервала: "))
            if a >= b:
                print("нееееет начало интервала должно быть меньше конца")
                continue
            if f_choice == 3 and (a <= -1 or b <= -1):
                print("неееет для ln(1 + x) x должен быть > -1. Попробуйте снова.")
            else:
                break

        n = int(input("введите число точек: "))
        x = np.linspace(a, b, n)
        y = [func(xi) for xi in x]
        return list(x), y

    def menu():
        print("выберите способ ввода:\n1 - вручную\n2 - из файла\n3 - функция")
        ch = int(input("таак: "))
        if ch == 1:
            return input_table_manual()
        elif ch == 2:
            x, y = None, None
            path = input("укажите путь к файлу: ")
            x, y = input_table_file(path)
            while x is None is y is None:

                print("неет такого файла нет")
                path = input("укажите путь к файлу: ")
                x, y = input_table_file(path)
            return x, y
        elif ch == 3:
            return input_table_function()

    x, y = menu()
    x_interp = float(input("введите значение X для интерполяции: "))
    if not (min(x) <= x_interp <= max(x)):
        print("неееет значение X должно быть в интервале интерполяции")
        return

    x_plot = np.linspace(min(x), max(x), 500)

    y_lagr = lagrange(x, y, x_interp)
    f_newton = newton_divided_diff(x, y)
    y_newton = newton_divided_interpolation(x, f_newton, x_interp)
    deltas = finite_diff_table(y)
    table = PrettyTable()
    table.title = "таблица конечных разностей"
    table.add_column("x", [round(i, 4) for i in x])
    table.add_column("y", [round(i, 4) for i in y])
    for i in range(1, len(x)):
        table.add_column(f"∆{i} y", [round(deltas[i][j], 4) if j < len(deltas[i]) else "" for j in range(len(x))])
    print(table)
    y_gauss = gauss_central_even(x, y, x_interp)

    y_l_plot = [lagrange(x, y, xi) for xi in x_plot]
    y_n_plot = [newton_divided_interpolation(x, f_newton, xi) for xi in x_plot]
    y_g_plot = plot_gauss(x, y, x_plot)

    print("\nИТОГО:")
    print(f"интерполяция многочленом Лагранжа: {x_interp}: {y_lagr:.6f}")
    print(f"интерполяция многочленом Ньютона (разделенные разности): {x_interp}: {y_newton:.6f}")
    print(f"интерполяция многочленом Гаусса: {x_interp}: {y_gauss:.6f}")

    plt.plot(x, y, "ro", color="cyan", label='Узлы')
    plt.plot(x_plot, y_l_plot, color="deeppink", linestyle='--', alpha=0.5, label='Лагранж')
    plt.plot(x_plot, y_n_plot, color="purple", linestyle='-.', alpha=0.5, label='Ньютон, разд. разн.')
    plt.plot(x_plot, y_g_plot, color="lime", linestyle=':', alpha=0.8, label='Гаусс')

    plt.axvline(x_interp, color='gray', linestyle=':')
    plt.legend()
    plt.title("интерполяция: Лагранж, Ньютон, Гаусс")
    plt.grid(True, color="lightgray")
    plt.savefig("interpolation.png")
    plt.show()


if __name__ == '__main__':
    main()
