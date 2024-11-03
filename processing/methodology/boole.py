import numpy as np
import sympy as sp

def calculate(func_expr, a, b, n):
    x = sp.symbols('x')
    expr = sp.sympify(func_expr)
    f = sp.lambdify(x, expr, 'numpy')

    form = []
    form.append('I = \\frac{{2 \\cdot \\Deltax x}}{{45}} \\cdot (7 \\cdot y0 + 32 \\cdot y1 + 12 \\cdot y2 + 32 \\cdot y3 + 7 \\cdot y4)')
    form.append('\\cdot x = \\frac{{b - a}}{{4}}')
    form.append('\\int x^n dx = \\frac{{x^{n+1}}}{{n + 1}}')

    h = (b - a) / 4
    print(f'Δx = ({b} - {a}) / 4')
    print(f'Δx = {h}')

    x_values = [a + i * h for i in range(5)]
    y_values = [round(f(x_val), 4) for x_val in x_values]

    for i, (x_val, y_val) in enumerate(zip(x_values, y_values)):
        print(f"x{i} = {x_val}, y{i} = {y_val}")

    integral = ((2 * h) / 45) * (7 * y_values[0] + 32 * y_values[1] + 12 * y_values[2] + 32 * y_values[3] + 7 * y_values[4])
    print(f'\nI = (2*{h})/45 * (7*{y_values[0]} + 32*{y_values[1]} + 12*{y_values[2]} + 32*{y_values[3]} + 7*{y_values[4]})')
    print(f'I = {integral}\n')


    return form, integral

def m_boole(data: dict):
    a = data['a']
    b = data['b']
    n = data['n']
    func_expr = data['func_expr']
    form, integral = calculate(func_expr, a, b, n)
    return {
        'form': form,
        'procedure': integral
    }
