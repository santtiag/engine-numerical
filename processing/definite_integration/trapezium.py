import numpy as np

def calculate(x, y):
    procedure = []
    forms = [
        'A = ( ( f(x1) + f(x2) ) / 2) \\cdot Δx',
        'AreaTrapecio = \\frac{{(y_1 + y_2) \\cdot \\Delta x)}}{{2}}',
        'ATotal = \\int_{a}^{b} dx ≈ ΣATrapecio'
    ]

    x_ = np.array([])
    y_ = np.array([])

    for i in range(len(x) - 1):
        x_ = np.append(x_, x[i + 1] - x[i])
        y_ = np.append(y_, y[i] + y[i + 1])

    delta = {
        'Δx': str(x_),
        'Δy': str(y_),

    }
    an = []

    for i in range(len(x)-1):
        an.append(f'A{i+1} = \\frac{{1}}{{2}} \\cdot ({y[i]} + {y[i+1]}) = {1/2 * (y[i] + y[i+1])}')

    text = 'A = A1'
    for i in range(len(x)-2):
        text = text + f" + A{i+2}"
    area = np.sum((y_ * x_) / 2)


    procedure = [
        an,
        text,
        f'Area = {area}',
    ]
    return forms, delta, procedure

def di_trapezium(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    forms, delta, procedure = calculate(x, y)
    return {
        'forms': forms,
        'deltas': delta,
        'procedure': procedure,
    }
