import numpy as np

def calculate(x, y):
    procedure = {}
    x_ = []
    a = []
    for i in range(len(x)-1):
        x_.append(x[i+1] - x[i])
    print(f'Δx = {x_}')
    procedure['Δx'] = str(x_)

    for i in range(len(x)-2):
        print(f"\\frac{{{x_[i]}}}{{3}} \\cdot ({y[i]} + 4 \\cdot {y[i+1]} + {y[i+2]})")
        a.append(x_[i]/3 * (y[i] + 4 * y[i+1] + y[i+2]))

    procedure['A'] = a

    procedure['ATotal'] = {
        'A1': a[0],
        'A2': a[-1],
        'ATotal': 'A1 + A2',
        'ATotal' : a[0] + a[-1]
    }
    return procedure

def di_parabola(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    procedure = calculate(x, y)
    return {
        'form': 'Δx/3 \\cdot (f(x_1) + 4 \\cdot f(x_2) + f(x_3))',
        'procedure': procedure
    }
