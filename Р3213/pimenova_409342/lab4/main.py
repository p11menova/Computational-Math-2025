from approximation_methods import *
from graphics_drawer import *
from table_printer import *

# мапа полученных значений коэфф
results = {"linear": [None, None],
           "quadratic": [None] * 3,
           "cubic": [None] * 4,
           "exp": [None] * 4,
           "log": [None] * 4,
           "pow": [None] * 4
           }


def validate_data(n, x_line, y_line):
    if n < 8 or n > 12:
        raise ValueError
    X = [float(x) for x in x_line.split()]
    if len(X) != n:
        raise ValueError
    Y = [float(y) for y in y_line.split()]
    if len(Y) != n:
        raise ValueError
    return n, X, Y


def read_data():
    while True:
        try:
            key = input("введите f если хотите прочитать из файла и любой другой символ в ином случае:")
            if key.strip() == "f":
                with open(input("введите название файла:")) as f:
                    n = int(f.readline())
                    x_line = f.readline().replace(",", ".")
                    y_line = f.readline().replace(",", ".")
            else:
                n = int(input("введите количество узлов функции:"))
                x_line = input("введите через пробел значения x_i:")
                y_line = input("введите через пробел значения y_i:")
            n, X, Y = validate_data(n, x_line, y_line)
            return n, X, Y

        except ValueError:
            print("error: некорректный ввод :( попробуйте еще раз!")
            continue


def print_data():
    key = input("введите f, если хотите записать результаты в файл и любой другой символ, если в консоль):")
    if key.strip() == "f":
        with open("output.txt", mode="w") as f:
            print("МЕТОД ЛИНЕЙНОЙ АППРОКСИМАЦИИ:".center(90), file=f)
            print_table(n, X, Y, lambda x: results["linear"][0] * x + results["linear"][1], f)

            print("МЕТОД КВАДРАТИЧНОЙ АППРОКСИМАЦИИ:".center(90), file=f)
            print_table(n, X, Y,
                        lambda x: results["quadratic"][0] * x ** 2 + results["quadratic"][1] * x + results["quadratic"][
                            2], f)

            print("МЕТОД КУБИЧЕСКОЙ АППРОКСИМАЦИИ:".center(90), file=f)
            print_table(n, X, Y, lambda x:
            results["cubic"][0] * x ** 3 + results["cubic"][1] * x ** 2 + results["cubic"][2] * x + results["cubic"][3],
                        f)

            if all(x is not None for x in results["exp"]):
                print("МЕТОД ЭКСПОНЕНЦИАЛЬНОЙ АППРОКСИМАЦИИ".center(90), file=f)
                print_table(len(results["exp"][2]), results["exp"][2], results["exp"][3],
                            lambda x: results["exp"][0] * math.exp(results["exp"][1] * x), f)

            if all(x is not None for x in results["log"]):
                print("МЕТОД ЛОГАРИФМИЧЕСКОЙ АППРОКСИМАЦИИ".center(90), file=f)
                print_table(len(results["log"][2]), results["log"][2], results["log"][3],
                            lambda x: results["log"][0] * math.log(x) + results["log"][1], f)

            if all(x is not None for x in results["pow"]):
                print("МЕТОД СТЕПЕННОЙ АППРОКСИМАЦИИ".center(90), file=f)
                print_table(len(results["pow"][2]), results["pow"][2], results["pow"][3],
                            lambda x: results["log"][0] * x ** results["log"][1], f)

            return

    print("МЕТОД ЛИНЕЙНОЙ АППРОКСИМАЦИИ:".center(90))
    print_table(n, X, Y, lambda x: results["linear"][0] * x + results["linear"][1], None)

    print("МЕТОД КВАДРАТИЧНОЙ АППРОКСИМАЦИИ:".center(90))
    print_table(n, X, Y,
                lambda x: results["quadratic"][0] * x ** 2 + results["quadratic"][1] * x + results["quadratic"][2],
                None)
    print("МЕТОД КУБИЧЕСКОЙ АППРОКСИМАЦИИ:".center(90))
    print_table(n, X, Y, lambda x:
    results["cubic"][0] * x ** 3 + results["cubic"][1] * x ** 2 + results["cubic"][2] * x + results["cubic"][3], None)

    if all(x is not None for x in results["exp"]):
        print("МЕТОД ЭКСПОНЕНЦИАЛЬНОЙ АППРОКСИМАЦИИ".center(90))
        print_table(len(results["exp"][2]), results["exp"][2], results["exp"][3],
                    lambda x: results["exp"][0] * math.exp(results["exp"][1] * x),
                    None)

    if all(x is not None for x in results["log"]):
        print("МЕТОД ЛОГАРИФМИЧЕСКОЙ АППРОКСИМАЦИИ".center(90))
        print_table(len(results["log"][2]), results["log"][2], results["log"][3],
                    lambda x: results["log"][0] * math.log(x) + results["log"][1], None)

    if all(x is not None for x in results["pow"]):
        print("МЕТОД СТЕПЕННОЙ АППРОКСИМАЦИИ".center(90))
        print_table(len(results["pow"][2]), results["pow"][2], results["pow"][3],
                    lambda x: results["log"][0] * x ** results["log"][1], None)


if __name__ == "__main__":
    n, X, Y = read_data()

    a, b = linear_approximation(n, X, Y)
    results["linear"] = a, b
    draw_linear_graph(X, Y, a, b)

    a, b, c = quadratic_approximation(n, X, Y)
    results["quadratic"] = float(a), float(b), float(c)
    draw_quadratic_graph(X, Y, a, b, c)

    a, b, c, d = cubic_approximation(n, X, Y)
    results["cubic"] = float(a), float(b), float(c), float(d)
    draw_cubic_approximation(X, Y, a, b, c, d)

    try:
        a, b, accepted_X, accepted_Y = exponential_approximation(n, X, Y)
        results["exp"] = float(a), float(b), accepted_X, accepted_Y
        draw_exp_approximation(X, Y, accepted_X, a, b)
    except TypeError:
        print(
            "error: ОДЗ логарифма x>0 -> недостаточно точек с положительными значениями функции для аппроксимации данным методом")

    try:
        a, b, accepted_X, accepted_Y = logarithm_approximation(n, X, Y)
        results["log"] = float(a), float(b), accepted_X, accepted_Y
        draw_log_approximation(X, Y, accepted_X, a, b)

    except TypeError:
        print(
            "error: ОДЗ логарифма x>0 -> недостаточно точек с положительными значениями функции для аппроксимации данным методом")

    try:
        a, b, accepted_X, accepted_Y = pow_approximation(n, X, Y)
        results["pow"] = float(a), float(b), accepted_X, accepted_Y
        draw_pow_approximation(X, Y, accepted_X, a, b)

    except TypeError:
        print(
            "error: ОДЗ логарифма x>0 -> недостаточно точек с положительными значениями функции для аппроксимации данным методом")

    print_data()
    draw_all_approximations(X, Y, results)
