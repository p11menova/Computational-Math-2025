from integral_methods import *
from storage import *

functions_dict = {
    "1": (f1, integral1),
    "2": (f2, integral2),
    "3": (f3, integral3)
}

methods_dict = {
    "1": left_rectangles,
    "2": right_rectangles,
    "3": middle_rectangles,
    "4": trapezoid,
    "5": simpson
}


def solve(f, integral, solving_method, A, B, eps):
    print("|".join(i.center(16) for i in '№ n I_0 I_1 |I_1-I_0|/2^k'.split()) + "\n" + "-" * 90)

    ans, msg = solving_method(A, B, 4, f, eps)
    print(msg)
    print(f"\033[1msolved with {solving_method.__name__} method: {round(ans, 4)} \033[0m")
    actual = integral(B) - integral(A)
    print(f"actual answer F(B) - F(A): {integral(B) - integral(A)}")
    print(f"inaccuracy: {round(100*abs((actual - ans)/actual), 5)}%")


if __name__ == "__main__":
    print("\033[1mпривееет это моя лаба 3\033[0m\nвот функции, которые можно проинтегрировать:")
    print("1) 2x^3 - 3x^2 + 5x - 9".center(40))
    print("2) -3x^3 - 5x^2 + 4x + 5".center(40))
    print("3) x^3 - 2x^2 - 5x + 24".center(40))
    function_num = None
    while function_num is None:
        function_num = input("введите \033[1mномер функции\033[0m, которую хотите проинтегрировать:").strip()
        if "1" <= function_num <= "3":
            break
        function_num = None
        print("\033[1m error: неет такой функции нет( попробуйте еще раз \033[0m")

    function = functions_dict[function_num]

    A, B = None, None
    while A is None or B is None:
        try:
            A, B = map(float, input("введите \033[1mграницы интегрирования\033[0m через пробел:").split())
            if A > B:
                raise ValueError
            break
        except ValueError:
            print("\033[1m error: неет это должны быть числа + идти по возрастанию \033[0m")
            A, B = None, None

    print("вот такие есть методы интегрирования:")
    print("\n".join(f"\t{k}) {v.__name__}_method" for k, v in methods_dict.items()))

    method_num = None
    while method_num is None:
        method_num = input("введите \033[1mномер метода\033[0m, которым хотите решить:").strip()
        if "1" <= method_num <= "5":
            break
        method_num = None
        print("\033[1m error: неет такого метода нет( попробуйте еще раз \033[0m")

    method = methods_dict[method_num]
    eps = None
    while eps is None:
        try:
            eps = float(input("введите \033[1mточность:\033[0m"))
            if eps <= 0:
                raise ValueError

        except ValueError:
            print("\033[1m error: нееет точность это положительное число \033[0m")
            eps = None

    solve(functions_dict[function_num][0], functions_dict[function_num][1], method, A, B, eps)
