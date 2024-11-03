import numpy as np
import sympy as sp

def calcular(x_values, y, func_expr):
    form = []
    form.append("\\Delta x \\cdot f(x_i, y_i) + y_i")
    form.append("\\Delta x = x_i+1 - x_i")
    form.append("\\Delta y = y_i + 1 - y_i")

    y_ = y
    delta = x_values[1] - x_values[0]

    x = sp.symbols('x')
    expr = sp.sympify(func_expr)
    f = sp.lambdify(x, expr, 'numpy')

    for i in range(len(x_values)):
        try:
            ecu = round(delta * f(x_values[i]) + y[i], 2)
        except:
            raise Exception(f"ERROR: La ecuación no se pudo resolver para x = {y[i]}")
        y_.append(ecu)

    return y_


def de_linear_approx(data: dict):
    #NOTE: Cambiar los datos
    # x = [0, 0.1, 0.2, 0.3]
    # y = [0]
    x = data['x']
    y = data['y']
    func_expr = data['func_expr']

    #NOTE: Cambiar la formula
    #WARNING: La formula depende del ejercico
    # f = lambda x: 9.8 - 0.15625 * x

    resultado = calcular(x, y, func_expr)

    print(f"La aproximación de la integral de f en el intervalo es: {resultado}")
    return {
    }
