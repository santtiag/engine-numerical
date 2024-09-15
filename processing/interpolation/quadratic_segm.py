import numpy as np
import pandas as pd
from fastapi import HTTPException

def first_func(x_values, y_values):
    if len(x_values) != len(y_values):
        raise HTTPException(status_code=404, detail='The number of values of x and y are not equal')

    j = 1
    count = 0
    pasa = False
    equations = []
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        equation = f"{y} = A{j} \cdot {x}^2 + B{j} \cdot {x} + C{j}"
        simplified = f"{y} = {x**2}A{j} + {x}B{j} + C{j}"
        equations.append((equation, simplified))

        if i != 0 and i != len(x_values)-1:
            pasa = True
            if pasa:
                j = j + 1
            equation = f"{y} = A{j} \cdot {x}^2 + B{j} \cdot {x} + C{j}"
            # Simplificar la ecuación asumiendo que A, B y C son las incógnitas para el i-ésimo punto
            simplified = f"{y} = {x**2}A{j} + {x}B{j} + C{j}"
            # Añadir la ecuación y la versión simplificada a la lista de ecuaciones
            equations.append((equation, simplified))
            i = i-1
        else:
            pasa = False
        count = count + 1
    return equations

def seconds_func(x_values):
    equations = []
    for i in range(len(x_values)):
        i = i + 1
        x = x_values[i]
        equation = f"2A{i} \cdot X{i+1} + B{i} = 2A{i+1} \cdot X{i+1} + B{i+1}"
        simplified = f"2A{i} \cdot {x} + B{i} = 2A{i+1} \cdot {x} + B{i+1}"
        equations.append((equation, simplified))
        if i+2 == len(x_values):
            i = i + 1
            x = x_values[i]
            equation = f"2A{i} \cdot X{i+1} + B{i} = 0"
            simplified = f"2A{i} \cdot {x} + B{i} = 0"
            equations.append((equation, simplified))
            break
    return equations

def main():
    # NOTE: Camibar datos
    # x_values = np.array([3, 4.5, 7, 9])
    # y_values = np.array([2.5, 1, 2.5, 0.5])

    x_values = np.array([1, 1.8, 2.5, 3.5])
    y_values = np.array([3, 5, 4, 5])

    equations = first_func(x_values, y_values)

    df_ecuaciones = pd.DataFrame(equations, columns=['Ecuación Original', 'Ecuación Simplificada'])
    print(df_ecuaciones)

    equations = seconds_func(x_values)

    df_ecuaciones = pd.DataFrame(equations, columns=['Ecuación Original', 'Ecuación Simplificada'])
    print(df_ecuaciones)

def i_quadratic_segm(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)
    first_equations = first_func(x_values, y_values)
    second_equations = seconds_func(x_values)
    return {'First Equations': first_equations, 'Second Equations': second_equations}
