import numpy as np

def calculate(x, y, n, k):
    formula_general = {}
    coefficients_general = {}
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                A[i][j] = k
            else:
                A[i][j] = np.sum(x ** (i + j))
        B[i] = np.sum(y * (x ** i)) if i != 0 else np.sum(y)
    print(A)

    coefficients = np.linalg.solve(A, B)

    formula = f'{coefficients[0]}'
    for i, coef in enumerate(coefficients):
        coefficients_general[f'a{i}'] = coef
        if coefficients[0] == coef:
            continue
        formula = formula + f' + {coef} x^{i}'
    
    return formula, coefficients_general


def mostrar(n):
    ecuaciones = []
    equations = {}

    for i in range(n):
        coeficientes = []
        for j in range(n):
            coeficiente = f"a{j} Σx^{i+j}"
            if i == 0 and j == 0:
                coeficiente = "a0 /cdot k"
            coeficientes.append(coeficiente)
        
        termino_derecho = f"Σy /cdot x^{i}" if i != 0 else "Σy"
        ecuacion = " + ".join(coeficientes) + f" = {termino_derecho}"
        equations[i] = ecuacion
    
    for i, ecuacion in enumerate(ecuaciones):
        print(f"Ecuación {i+1}: {ecuacion}")



    # for i in range(n):
    #     coeficientes = []
    #     for j in range(n):
    #         coeficiente = f"a{j} Σx^{i+j}"
    #         if i == 0 and j == 0:
    #             coeficiente = "a0 /cdot k"
    #         coeficientes.append(coeficiente)
        
    #     termino_derecho = f"Σy /cdot x^{i}" if i != 0 else "Σy"
    #     ecuacion = " + ".join(coeficientes) + f" = {termino_derecho}"
    #     ecuaciones.append(ecuacion)
    
    # for i, ecuacion in enumerate(ecuaciones):
    #     print(f"Ecuación {i+1}: {ecuacion}")
    return equations


def r_nonlinear_polynomial(data: dict):
    #NOTE: Cambio de datos
    x = data['x']
    y = data['y']
    n = data['n']
    
    x = np.array(x)
    y = np.array(y)

    if len(x) != len(y):
        print(f'x = {len(x)}')
        print(f'y = {len(y)}')
        raise ValueError('Los valores "x" y "y" no son los mismos')

    k = len(x)
    equations = mostrar(n)
    form, coef_solved = calculate(x, y, n, k)


    return {
            'K': k,
            'coefficients': equations,
            'coefficients solved': coef_solved,
            'y': form,
            }
