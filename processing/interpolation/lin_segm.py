import numpy as np

def calculate(x, y):
    procedure = {}
    equations = []

    for i in range(len(x)-1):
        equations.append(f'{y[i]} + \\frac{{{y[i+1]} - {y[i]}}}{{{x[i+1]} - {x[i]}}} \\cdot (x - {x[i]})')
        equations.append(f'{y[i]} + {(y[i+1] - y[i]) / (x[i+1] - x[i])} \\cdot (x - {x[i]})')
        equations.append(f'{(y[i+1] - y[i]) / (x[i+1] - x[i])}x {((y[i+1] - y[i]) / (x[i+1] - x[i]) * -x[i]) + y[i]}')
        procedure[f'P{i+1}(x)'] = equations
        equations = []

    return procedure


def i_linear_segm(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    procedure = calculate(x_values, y_values)

    return {
        'form': 'P(x) = yi + m(x - xi)',
        'Answer': procedure
    }
