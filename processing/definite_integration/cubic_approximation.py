import numpy as np

def calculate(x, y):
    procedure = {}
    forms =[
        'A = \\frac{{3cΔx}}{{8}} \\cdot [f(x_1) + 3 \\cdot f(x_2) + 3 * f(x_3) + f(x_4)]',
        'Δx = x_4 - x_1',
    ]

    x_ = (x[-1] - x[0])/3
    procedure['Δx'] = str(x_)
    procedure['A'] = [
        f"A = \\frac{{3 \\doct {x_}}}{{8}} \\cdot ({y[0]} + 3 \\cdot {y[1]} + 3 \\cdot {y[2]} + {y[3]})",
        f'A = {(3*x_/8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])}'
       ]
    return forms, procedure


def di_cubic_approximation(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    forms, procedure = calculate(x, y)

    return {
        'form': forms,
        'procedure': procedure
    }
