import numpy as np
import sympy as sp
def pick(n):
    values = {
        2: ([-0.57735, 0.57735], [1, 1]),
        3: ([-0.77459, 0, 0.77459], [0.55555, 0.88888, 0.55555]),
        4: ([-0.86113, -0.33998, 0.33998, 0.86113], [0.34785, 0.65214, 0.65214, 0.34785]),
        5: ([-0.90617, -0.53846, 0, 0.53846, 0.90617], [0.23692, 0.47862, 0.56888, 0.47862, 0.23692]),
        6: ([-0.93246, -0.66120, -0.23861, 0.23861, 0.66120, 0.93246], [0.17132, 0.36076, 0.46791, 0.46791, 0.36076, 0.17132]),
        7: ([-0.94910, -0.74153, -0.40484, 0, 0.40484, 0.74153, 0.94910], [0.12948, 0.27970, 0.38183, 0.41795, 0.38183, 0.27970, 0.12948]),
        8: ([-0.96028, -0.79666, -0.52553, -0.18343, 0.18343, 0.52553, 0.79666, 0.96028], [0.10122, 0.22238, 0.31370, 0.36268, 0.36268, 0.31370, 0.22238, 0.10122])
    }
    return values.get(n, ([], []))

def calculate(a, b, r):
    form = []
    form.append('x_i = \\frac{{1}}{{2}} [(b - a) \\cdot ri + (b + a)]')
    xi = []
    for i in range(len(r)):
        xi.append(1/2 * ((b - a) * (r[i]) + (b + a)))
        form.append(f'\\frac{{1}}{{2}} [({b} - {a}) \\cdot {r[i]} + ({b} + {a})] = {xi[i]}')
    return xi, form

def func(c, xi, a, b, func_expr):
    procedure = []

    x = sp.symbols('x')
    expr = sp.sympify(func_expr)
    f_values = []

    f = np.array([])

    for xi_value in xi:
        f_value = float(expr.subs(x, xi_value))
        f_values.append(f_value)

    f_values = np.array(f_values)


    procedure.append("\\frac{b - a}{2} \\cdot \\sum f(xi) \\cdot ci")

    formula = f"\\frac{{{b} - {a}}}{{2}} \\cdot ("
    for i in range(len(xi)):
        if i == 0:
            formula = formula + f" ({f_values[i]} \\cdot {c[i]})"
            procedure.append(formula)
            continue
        elif i == len(xi)-1:
            formula = formula + f" + ({f_values[i]} \\cdot {c[i]}) )"
            procedure.append(formula)
            break
        formula = formula + f" + ({f_values[i]} \\cdot {c[i]})"
        procedure.append(formula)

    result = (b-a)/2 * np.sum(f_values*np.array(c))
    return procedure, result


def m_gauss(data: dict):
    a = data['a']
    b = data['b']
    n = data['n']
    func_expr = data['func_expr']

    r, c = pick(n)

    xi, form = calculate(a, b, r)
    procedure, result = func(c, xi, a, b, func_expr)


    return {
        'form': form,
        'procedure': procedure,
        'result': result,
    }
