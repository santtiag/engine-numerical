from fastapi import HTTPException
import numpy as np
import pandas as pd

# INFO: delta to get xy delta values
def get_delta(x_values, y_values):
    if len(x_values) != len(y_values):
        raise HTTPException(status_code=404, detail='The number of values of x and y are not equal')
    x_delta = []
    y_delta = []
    for i in range(len(x_values)-1):
        if i+1 in np.where(x_values)[0]:
        # if i+1 == np.where(len(x_values)):
            break
        x_delta.append(x_values[i+1] - x_values[i])
        y_delta.append(y_values[i+1] - y_values[i])
    return x_delta, y_delta

# INFO: B Value
def calculate_B_values(x, y):
    aux = []
    indep = []
    equations = []
    equation_B = []
    b_answer = {}

    print(f"Bi • Δxi/3 + Bi+1 • 2/3 • (Δxi + Δxi+1) + Bi+2 • (Δxi+1/3) =  (Δyi+1/Δxi+1) - (Δyi/Δxi)")
    j = 0
    i = 1
    for _ in range(len(x)):
        if i == 1:
            equation1 = f"B_{i} \\cdot \\frac{{\\Delta x_{i}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot (\\Delta x_{i} + \\Delta x_{{i+1}}) + B_{{i+2}} \\cdot \\frac{{\\Delta x_{{i+1}}}}{{3}} = \\frac{{\\Delta y_{{i+1}}}}{{\\Delta x_{{i+1}}}} - \\frac{{\\Delta y_{i}}}{{\\Delta x_{i}}}"
            equation2 = f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]}) + B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}} = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
            equation3 = "\\cancel{" + f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}}" + "}" + f"B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]})  + B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}} = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
            equations.append((equation1, equation2, equation3))
            aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
            equation_B.append(aux)
            indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
            i = i + 1
            j = j + 1
            continue
        elif i == len(x)-1:
            equation1 = f"B_{i} \\cdot \\frac{{\\Delta x_{i}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot (\\Delta x_{i} + \\Delta x_{{i+1}}) + B_{{i+2}} \\cdot \\frac{{\\Delta x_{{i+1}}}}{{3}} = \\frac{{\\Delta y_{{i+1}}}}{{\\Delta x_{{i+1}}}} - \\frac{{\\Delta y_{i}}}{{\\Delta x_{i}}}"
            equation2 = f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]}) + B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}} = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
            equation3 = f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]})  +" + "\\cancel{" + f"B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}}" + "}" + f" = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
            equations.append((equation1, equation2, equation3))
            aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
            equation_B.append(aux)
            indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
            i = i + 1
            j = j + 1
            break

        equation1 = f"B_{i} \\cdot \\frac{{\\Delta x_{i}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot (\\Delta x_{i} + \\Delta x_{{i+1}}) + B_{{i+2}} \\cdot \\frac{{\\Delta x_{{i+1}}}}{{3}} = \\frac{{\\Delta y_{{i+1}}}}{{\\Delta x_{{i+1}}}} - \\frac{{\\Delta y_{i}}}{{\\Delta x_{i}}}"
        equation2 = f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]}) + B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}} = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
        equation3 = f"B_{i} \\cdot \\frac{{{x[j]}}}{{3}} + B_{{i+1}} \\cdot \\frac{{2}}{{3}} \\cdot ({x[j]} + {x[j+1]})  + B_{{i+2}} \\cdot \\frac{{{x[j+1]}}}{{3}} = \\frac{{{y[j+1]}}}{{{x[j+1]}}} - \\frac{{{y[j]}}}{{{x[j]}}}"
        equations.append((equation1, equation2, equation3))
        aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
        equation_B.append(aux)
        indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
        i = i + 1
        j = j + 1
    # print(f"Bi • Δxi/3 + Bi+1 • 2/3 • (Δxi + Δxi+1) + Bi+2 • (Δxi+1/3) =  (Δyi+1/Δxi+1) - (Δyi/Δxi)")
    # j = 0
    # i = 1
    # for _ in range(len(x)):
    #     if i == 1:
    #         equation1 = f"B{i} • Δx{i}/3 + B{i+1} • 2/3 (Δx{i} + Δx{i+1}) + B{i+2} • (Δx{i+1}/3) = (Δy{i+1}/Δx{i+1} - (Δy{i}/Δx{i}))"
    #         equation2 = f"B{i} • {x[j]}/3 + B{i+1} • 2/3 • ({x[j]} + {x[j+1]}) + B{i+2} • ({x[j+1]}/3) = ({y[j+1]}/{x[j+1]}) - ({y[j]}/{x[j]}))"
    #         # equation3 = f"///B{i} • {x[j]/3}/// + B{i+1} • {2/3 * (x[j] + x[j+1])}  + B{i+2} • {x[j+1]/3} = {(y[j+1]/x[j+1]) - (y[j]/x[j])}"
    #         equation3 = "\\cancel{" + f"B{i} • {x[j]/3}" + "}" + f"B{i+1} • {2/3 * (x[j] + x[j+1])}  + B{i+2} • {x[j+1]/3} = {(y[j+1]/x[j+1]) - (y[j]/x[j])}"
    #         equations.append((equation1, equation2, equation3))
    #         aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
    #         equation_B.append(aux)
    #         indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
    #         i = i + 1
    #         j = j + 1
    #         continue
    #     elif i == len(x)-1:
    #         equation1 = f"B{i} • Δx{i}/3 + B{i+1} • 2/3 (Δx{i} + Δx{i+1}) + B{i+2} • (Δx{i+1}/3) = (Δy{i+1}/Δx{i+1} - (Δy{i}/Δx{i}))"
    #         equation2 = f"B{i} • {x[j]}/3 + B{i+1} • 2/3 • ({x[j]} + {x[j+1]}) + B{i+2} • ({x[j+1]}/3) = ({y[j+1]}/{x[j+1]}) - ({y[j]}/{x[j]}))"
    #         equation3 = f"B{i} • {x[j]/3} + B{i+1} • {2/3 * (x[j] + x[j+1])}  +" + "\\cancel{" + f"B{i+2} • {x[j+1]/3}" + "}" + f" = {(y[j+1]/x[j+1]) - (y[j]/x[j])}"
    #         equations.append((equation1, equation2, equation3))
    #         aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
    #         equation_B.append(aux)
    #         indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
    #         i = i + 1
    #         j = j + 1
    #         break

    #     equation1 = f"B{i} • Δx{i}/3 + B{i+1} • 2/3 (Δx{i} + Δx{i+1}) + B{i+2} • (Δx{i+1}/3) = (Δy{i+1}/Δx{i+1} - (Δy{i}/Δx{i}))"
    #     equation2 = f"B{i} • {x[j]}/3 + B{i+1} • 2/3 • ({x[j]} + {x[j+1]}) + B{i+2} • ({x[j+1]}/3) = ({y[j+1]}/{x[j+1]}) - ({y[j]}/{x[j]}))"
    #     equation3 = f"B{i} • {x[j]/3} + B{i+1} • {2/3 * (x[j] + x[j+1])}  + B{i+2} • {x[j+1]/3} = {(y[j+1]/x[j+1]) - (y[j]/x[j])}"
    #     equations.append((equation1, equation2, equation3))
    #     aux = [(x[j]/3), (2/3*(x[j]+x[j+1])), (x[j+1]/3)]
    #     equation_B.append(aux)
    #     indep.append((y[j+1]/x[j+1]) - (y[j]/x[j]))
    #     i = i + 1
    #     j = j + 1

    # INFO: Round two

    b_matriz = np.array(get_zero_array(equation_B))

    b_inv = np.linalg.inv(b_matriz)

    b_mmult = np.dot(b_inv, np.array(indep))
    b = np.pad(b_mmult,(1,1), 'constant', constant_values=(0, 0))
    j = 1
    for i in b:
        b_answer[f'B{j}'] = i
        j=j+1
    return equations, b_answer, b

# PERF: Zero Array
def get_zero_array(e):
    n = len(e)

    # Eliminar el primer elemento de la primera sublista
    e[1].pop(0)

    # Eliminar el último elemento de la última sublista
    e[-1].pop(-1)


    # Crear una matriz de nxn inicializada con ceros
    final_matrix = [[0] * n for _ in range(n)]

    changed = True
    aux = 0
    for i in range(len(e)):
        if changed and i == 1:
            aux = aux - 1
            changed = False
        for j in range(len(e[i])):
            if i + j < n+2:
                final_matrix[i][aux + j] = e[i][j]
        aux = aux + 1
    return final_matrix


# INFO: A Value
def calculate_A_values(b, x_delta):
    a = {}
    a_answer = []
    print('\nAi = (Bi+1 - Bi) / 3Δxi')

    for i in range(len(x_delta)):
        a[f'A{i+1}-1'] = f'(B{i+2} - B{i+1}) / 3 • Δx{i+1}'
        a[f'A{i+1}-2'] = f'({b[i+1]} - {b[i]}) / 3 • {x_delta[i]}'
        a[f'A{i+1}-3'] = f'{(b[i+1] - b[i])/(3*x_delta[i])}'
        a_answer.append((b[i+1] - b[i])/(3*x_delta[i]))
    return a, a_answer


# INFO: C Value
def calculate_C_values(b, x_delta, y_delta):
    c = {}
    c_answer = []
    print('\nCi = (Δyi/Δxi) - (Δxi/3) • (2Bi + Bi+1)')

    for i in range(len(x_delta)):
        if x_delta[i] == 0:
            raise HTTPException(status_code=404, detail='A value of x cannot be equal to the consecutive one')
        c[f'C{i+1}-1'] = f'(Δy{i+1}/Δx{i+1}) - (Δx{i+1}/3) • (2B{i+1} + B{i+2})'
        c[f'C{i+1}-2'] = f'{y_delta[i]}/{x_delta[i]}) - ({x_delta[i]}/3) • (2 • {b[i]} + {b[i+1]})'
        c[f'C{i+1}-3'] = f'{(y_delta[i] / x_delta[i]) - (x_delta[i]/3) * (2 * b[i] + b[i+1])}\n'
        c_answer.append((y_delta[i] / x_delta[i]) - (x_delta[i]/3) * (2 * b[i] + b[i+1]))
    return c, c_answer

# INFO: D Value
def calculate_D_values(y_values):
    d = {}
    d_answer = []
    j = 0
    for i in y_values:
        if j == len(y_values)-1:
            break
        d[f'D{j+1}'] = i
        d_answer.append(i)
        j=j+1
    return d, d_answer

# INFO: P Value
def calculate_P_values(a, b, c, d, x_values):
    p = {}
    print('\nP = A(x-xi)^3 + B(x-xi)^2 + C(x-xi) + D')
    for i in range(len(x_values)-1):
        p[f'P{i+1}'] = f'{a[i]}(x-{x_values[i]})^3 + {b[i]}(x-{x_values[i]})^2 + {c[i]}(x-{x_values[i]}) + {d[i]} [{x_values[i]}, {x_values[i+1]}]'
    return p

def main(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    # NOTE: Cambio de datos
    # Pruba
    # x_values = np.array([1, 1.8, 3.8, 4.5, 6])
    # y_values = np.array([0, 2.4, 4.2, 5, 6.5])

    x_delta, y_delta = get_delta(x_values, y_values)
    delta_values = {'x delta': x_delta, 'y delta': y_delta}
    print(pd.DataFrame({'Δx':x_delta, 'Δy':y_delta}))

    equation_1, equation_B, indep = calculate_B_values(x_delta, y_delta)

    b_matriz_zero = get_zero_array(equation_B)

    for i in equation_1:
        print(f'Ecuación #')
        for j in i: print(j)
        print('\n')

    print(f'Independientes:\n {indep}\n')

    b_matriz = np.array(b_matriz_zero)

    print(f'B: \n{b_matriz}\n')

    b_inv = np.linalg.inv(b_matriz)
    print(f'Ecuaciones MINVERSA:\n{b_inv}\n')

    indep_ = np.array(indep)
    b_mmult = np.dot(b_inv, indep_)
    print(f'MMULT:\n{b_mmult}\n')

    b = np.pad(b_mmult,(1,1), 'constant', constant_values=(0, 0))
    j = 1
    for i in b:
        print(f'B{j}: {i}')
        j=j+1

    a = calculate_A_values(b, x_delta)
    c = fifth_func(b, x_delta, y_delta)
    d = sixth_func(y_values)

    seventh_func(a, b, c, d, x_values)

def i_cubic_segm(data: dict):
    x = data['x']
    y = data['y']
    x_values = np.array(x)
    y_values = np.array(y)

    x_delta, y_delta = get_delta(x_values, y_values)
    delta_values = {'x delta': x_delta, 'y delta': y_delta}
    equation, b_answer, b = calculate_B_values(x_delta, y_delta)
    b_values = {'Equations': equation, 'Independs': b_answer}
    a_values, a_answer = calculate_A_values(b, x_delta)
    c_values, c_answer = calculate_C_values(b, x_delta, y_delta)
    d_values, d_answer = calculate_D_values(y_values)
    p_values = calculate_P_values(a_answer, b, c_answer, d_answer, x_values)

    return {'deltas': delta_values, 'B values': b_values, 'A values': a_values, 'C values': c_values, 'D values': d_values, 'P values': p_values}
