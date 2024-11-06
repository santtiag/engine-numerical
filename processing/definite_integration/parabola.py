import numpy as np

def calculate(x, y):
    procedure = []
    x_ = []
    for i in range(len(x)-1):
        x_.append(x[i+1] - x[i])
    a: list = []
    for i in range(len(x)-2):
        procedure.append(f"A{i+1} =\\frac{{\\Delta x}}{{3}} \\cdot [f(x_{i+1} + 4 \\cdot f(x_{i+2} + f(x_{i+3})")
        procedure.append(f"A{i+1} =\\frac{{{x_[i]}}}{{3}} \\cdot [{y[i]} + 4 \\cdot {y[i+1]} + {y[i+2]}]")
        procedure.append(f"A{i+1} = {x_[i]/3 * (y[i] + 4 * y[i+1] + y[i+2])}")
        a.append(x_[i]/3 * (y[i] + 4 * y[i+1] + y[i+2]))
    result = []
    result = [
        f'A1 = {a[0]}',
        f'A2 = {a[-1]}',
        'Atotal = A1 + A2',
        f'Atotal = {a[0]} + {a[-1]}',
        f'Atotal = {a[0] + a[-1]}'
    ]
    return x_, procedure, result

def di_parabola(data: dict):
    x = data['x']
    y = data['y']
    # x_values = np.array(x)
    # y_values = np.array(y)

    x_, procedure, result = calculate(x, y)
    return {
        'form': 'A = \\frac{{\\Delta x}}{{3}} \\cdot [f(x_1) + 4 \\cdot f(x_2) + f(x_3)]',
        '\\Delta x': x_,
        'procedure': procedure,
        'result': result
    }
