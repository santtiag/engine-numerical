from fastapi import HTTPException
import numpy as np

def calculate(x, y):
    forms = [
        'Area = Σ Area Rectangulo',
        'Area Rectangulo = Base \\cdot Altura'
        'Area Rectangulo = y \\cdot Δx',
        'Area = Σf(x) \\cdot Δx'
    ]

    procedure = {}

    x_ = []
    for i in range(len(x)-1):
        temp = x[i+1] - x[i]
        x_.append(temp)
    x_ = np.array(x_)
    procedure['Δx'] = str(x_)

    text = 'A = A1'
    number = f"A = {x_[0]} * {y[0]}"
    for i in range(len(x)-2):
        text = text + f"+ A{i+2}"
        number = number + f' + {x_[i+1]} * {y[i+1]}'
    sum_x = np.sum(y*x_)
    procedure['A'] = [
        text,
        number,
        f'A = {sum_x}'
    ]
    return forms, procedure

def di_rectangle(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    procedure = calculate(x_values, y_values)

    forms, procedure = calculate(x, y)

    return {
        'forms': forms,
        'procedure': procedure
    }
