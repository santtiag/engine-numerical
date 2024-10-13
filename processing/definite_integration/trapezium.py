import numpy as np

def calculate(x, y):
    procedure = {}
    forms = [
        'A = ( ( f(x1) + f(x2) ) / 2) \\cdot Δx',
        'ATrapecio = ((y_1 + y_2) \\cdot Δ_x) / 2',
        'ATotal = ∫ba(x)dx ≈ ΣATrapecio'
    ]

    x_ = np.array([])
    y_ = np.array([])

    for i in range(len(x) - 1):
        x_ = np.append(x_, x[i + 1] - x[i])
        y_ = np.append(y_, y[i] + y[i + 1])

    procedure['Δx'] = str(x_)
    procedure['Δy'] = str(y_)

    text = 'A = A1'
    number = f"{y[0]} * {x_[0]}"
    for i in range(len(x)-2):
        text = text + f"+ A{i+2}"
        number = number + f' + {y_[i+1]} * {x_[i+1]}'
    area = np.sum((y_ * x_) / 2)
    procedure['A'] = {
        text,
        f'A = Σ \\frac{{{number}}}{{2}}',
        f'Area = {area}'
    }
    return forms, procedure

def di_trapezium(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    forms, procedure = calculate(x, y)
    return {
        'forms': forms,
        'procedure': procedure
    }
