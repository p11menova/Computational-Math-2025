import numpy as np
import matplotlib.pyplot as plt
from math import exp

def draw_linear_graph(X, Y, a, b):
    plt.figure(figsize=(10, 6))

    # Рисуем точки
    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)

    # Рисуем линейную функцию
    x_line = np.linspace(min(X) - 0.1, max(X) + 0.1, 100)
    y_line = a * x_line + b
    plt.plot(x_line, y_line, label=f'аппроксимирующая функция: y = {round(a,3)}x + {round(b,3)}', color='darkcyan')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    plt.savefig('graphics/linear_approximation.png')
    plt.close()



def draw_quadratic_graph(X, Y, a, b, c):
    plt.figure(figsize=(10, 6))

    # Рисуем точки
    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)
    x_line = np.linspace(min(X) - 0.1, max(X) + 0.1, 100)
    y_line = a * x_line**2 + b*x_line + c
    plt.plot(x_line, y_line, label=f'аппроксимирующая функция: y = {round(a,3)}x^2 + {round(b,3)}x + {round(c, 3)}', color='lightseagreen')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/quadratic_approximation.png')
    plt.close()


def draw_cubic_approximation(X, Y, a, b, c, d):
    plt.figure(figsize=(10, 6))

    # Рисуем точки
    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)
    x_line = np.linspace(min(X) - 0.1, max(X) + 0.1, 100)
    y_line = a * x_line ** 3 +  + b * x_line**2 + c*x_line + d
    plt.plot(x_line, y_line, label=f'аппроксимирующая функция: y = {round(a, 3)}x^3 + {round(b, 3)}x^2 + {round(c, 3)}x + {round(d, 3)}',
             color='lightseagreen')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/cubic_approximation.png')
    plt.close()

def draw_exp_approximation(X, Y, acc_X, a, b):
    plt.figure(figsize=(10, 6))

    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)
    x_line = np.linspace(min(acc_X) - 0.1, max(acc_X) + 0.1, 100)
    y_line = a * np.exp(b*x_line)
    plt.plot(x_line, y_line,
             label=f'аппроксимирующая функция: y = {round(a, 3)}* e^{round(b, 3)}x',
             color='lightseagreen')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/exp_approximation.png')
    plt.close()



def draw_log_approximation(X, Y, acc_x, a, b):
    plt.figure(figsize=(10, 6))

    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)
    x_line = np.linspace(min(acc_x) - 0.1, max(acc_x) + 0.1, 100)
    y_line = a * np.log(x_line)+ b
    plt.plot(x_line, y_line,
             label=f'аппроксимирующая функция: y = {round(a, 3)}*ln(x) + {round(b, 3)}',
             color='lightseagreen')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/log_approximation.png')
    plt.close()


def draw_pow_approximation(X, Y, acc_x, a, b):
    plt.figure(figsize=(10, 6))

    plt.scatter(X, Y, color='pink', label='исходные точки (X, Y)', zorder=5)
    x_line = np.linspace(min(acc_x) - 0.1, max(acc_x) + 0.1, 100)
    y_line = a * x_line**b
    plt.plot(x_line, y_line,
             label=f'аппроксимирующая функция: y = {round(a, 3)}x^{round(b, 3)}',
             color='lightseagreen')

    plt.title('')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphics/pow_approximation.png')
    plt.close()


def draw_all_approximations(X, Y,results):
    linear_coeffs = results["linear"]
    quadratic_coeffs = results["quadratic"]
    cubic_coeffs = results["cubic"]
    exp_coeffs = results["exp"][0:2]
    log_coeffs = results["log"][0:2]
    pow_coeffs = results["pow"][0:2]
    acc_X = results["exp"][2]
    plt.figure(figsize=(12, 8))

    plt.scatter(X, Y, color='cyan', label='исходные точки (X, Y)', zorder=10)

    x_min = min(X) - 0.5
    x_max = max(X) + 0.5
    x_line = np.linspace(x_min, x_max, 500)

    if linear_coeffs and linear_coeffs[0] is not None:
        a, b = linear_coeffs
        y_linear = a * x_line + b
        plt.plot(x_line, y_linear, label=f'линейн: y = {round(a, 3)}x + {round(b, 3)}',
                 color='pink', linestyle='-')

    if quadratic_coeffs and all(c is not None for c in quadratic_coeffs):
        a, b, c = quadratic_coeffs
        y_quad = a * x_line ** 2 + b * x_line + c
        plt.plot(x_line, y_quad, label=f'квадр: y = {round(a, 3)}x² + {round(b, 3)}x + {round(c, 3)}',
                 color='hotpink', linestyle='-')

    if cubic_coeffs and all(c is not None for c in cubic_coeffs):
        a, b, c, d = cubic_coeffs
        y_cubic = a * x_line ** 3 + b * x_line ** 2 + c * x_line + d
        plt.plot(x_line, y_cubic,
                 label=f'кубич: y = {round(a, 3)}x³ + {round(b, 3)}x² + {round(c, 3)}x + {round(d, 3)}',
                 color='Violet', linestyle='-')

    if exp_coeffs and all(c is not None for c in exp_coeffs[:2]):
        a, b = exp_coeffs[:2]
        y_exp = a * np.exp(b * x_line)
        plt.plot(x_line, y_exp, label=f'экспонец: y = {round(a, 3)}e^{round(b, 3)}x',
                 color='grey', linestyle='--')

    if log_coeffs and all(c is not None for c in log_coeffs[:2]):
        a, b = log_coeffs[:2]
        x_log = x_line[x_line > 0.01]  # Избегаем log(0)
        y_log = a * np.log(x_log) + b
        plt.plot(x_log, y_log, label=f'лог: y = {round(a, 3)}ln(x) + {round(b, 3)}',
                 color='lightgrey', linestyle='--')

    if pow_coeffs and all(c is not None for c in pow_coeffs[:2]):
        a, b = pow_coeffs[:2]
        x_pow = x_line[x_line > 0.01]  # Избегаем 0^b
        y_pow = a * x_pow ** b
        plt.plot(x_pow, y_pow, label=f'степен: y = {round(a, 3)}x^{round(b, 3)}',
                 color='DarkSlateGrey', linestyle='--')

    plt.title('сравнение методов аппроксимации')
    plt.xlabel('Ox')
    plt.ylabel('Oy')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper right')
    plt.tight_layout()

    plt.savefig('graphics/all_approximations.png', bbox_inches='tight', dpi=300)
    plt.show()
