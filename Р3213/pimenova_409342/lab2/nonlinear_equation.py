EPS = 0.001
MAX_ITER = 1000


def simple_iteration(a0, b0, f, phi, dphi_dx):
    if dphi_dx(a0) >= 1 or dphi_dx(b0) >= 1:
        return None, "условие сходимости метода простой итерации не выполняется"

    x0 = a0
    x1 = phi(x0)
    result_text = ''
    iter_count = 0
    try:
        while abs(x0 - x1) >= EPS:
            if iter_count == MAX_ITER:
                return None, "уравнение не имеет корней на данном промежутке"

            result_text += ''.join([i.center(20) for i in
                                    f"№={iter_count} x_k={round(x0, 3)} x_k1={round(x1, 3)} f(x_k1)={round(f(x1), 3)} |x0-x1|={round(abs(x0 - x1), 3)}".split()]) + '\n'
            x0 = x1
            x1 = phi(x0)
            iter_count += 1

        result_text += ''.join([i.center(20) for i in
                                f"№={iter_count} x_k={round(x0, 3)} x_k1={round(x1, 3)} f(x_k1)={round(f(x1), 3)} |x0-x1|={round(abs(x0 - x1), 3)}".split()])

        return x1, result_text

    except Exception:
        return None, "уравнение не решится данным методом("


def newton_method(x0, f, df):
    x1 = None
    result_msg = ''
    iter_count = 0
    while x1 is None or abs(x0 - x1) >= EPS and abs(f(x1)) >= EPS:
        if iter_count == MAX_ITER:
            return None, "превышено максимальное количество итераций"

        x0 = x1 if x1 is not None else x0
        x1 = x0 - f(x0) / df(x0)
        result_msg += ''.join([i.center(16) for i in
                               f"№={iter_count} x_i={round(x0, 3)} x_i+1={round(x1, 3)} f(x_i+1)={round(f(x1), 3)} f'(x_i)={round(df(x0), 3)} |x0-x1|={round(abs(x0 - x1), 3)}".split()]) + '\n'
        iter_count += 1

    return x1, result_msg


def chord_method(a, b, f, df_dx2):
    if f(a) * f(b) > 0:
        return None, "уравнение не имеет корней на данном промежутке"

    x0 = None
    x = None
    iter_count = 0
    result_msg = ''
    if not (f(a) * df_dx2(a) > 0 or f(b) * df_dx2(b) > 0):
        return None, f"уравнение не сойдется данным методом, " \
                     f"поскольку не выполняется условие совпадения знака функции на конце отрезка и знака второй производной\n" \
                     f"f(a)={round(f(a), 3)} df_dx2(a)={round(df_dx2(a), 3)} f(b)={round(f(b), 3)} df_dx2(b)={round(df_dx2(b), 3)}"
    if f(a) * df_dx2(a) > 0:  # b - fixed_end

        while iter_count == 0 or abs(x0 - x) >= EPS:

            if iter_count == MAX_ITER:
                return None, "превышено максимальное количество итераций"

            x0 = x if x != None else a
            x = (a * f(b) - b * f(a)) / (f(b) - f(a))

            result_msg += ''.join(
                [i.center(14) for i in f"№={iter_count} a={round(a, 3)} b={round(b, 3)} x={round(x, 3)} "
                                       f"f(a)={round(f(a), 3)} f(b)={round(f(b), 3)} f(x)={round(f(x), 3)} "
                                       f"|x_i+1-x_i|={round(abs(x - x0), 3)}".split()]) + '\n'
            b = x
            iter_count += 1

    if f(b) * df_dx2(b) > 0:
        while iter_count == 0 or abs(x0 - x) >= EPS:

            if iter_count == MAX_ITER:
                return None, "превышено максимальное количество итераций"
            x0 = x if x is not None else b
            x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            result_msg += ''.join(
                [i.center(14) for i in f"№={iter_count} a={round(a, 3)} b={round(b, 3)} x={round(x, 3)} "
                                       f"f(a)={round(f(a), 3)} f(b)={round(f(b), 3)} f(x)={round(f(x), 3)} "
                                       f"|x_i+1-x_i|={round(abs(x - x0), 3)}".split()]) + '\n'
            a = x
            iter_count += 1

    result_msg += ''.join([i.center(14) for i in f"№={iter_count} a={round(a, 3)} b={round(b, 3)} x={round(x, 3)} "
                                                 f"f(a)={round(f(a), 3)} f(b)={round(f(b), 3)} f(x)={round(f(x), 3)} "
                                                 f"|x_i+1-x_i|={round(abs(x - x0), 3)}".split()])
    return x, result_msg
