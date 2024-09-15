import numpy as np

def calculate(x, y):
    n = len(x)
    array = []
    solved_arr = {}
    array.append([np.sum(x), n])
    array.append([np.sum(x**2), np.sum(x)])

    solved_arr['n'] = n
    solved_arr['Σx'] = array[0]
    solved_arr['Σ^2'] = array[1]
    
    ind = []
    y_prima = np.log(y)
    ind.append(np.sum(y_prima))
    ind.append(np.sum(x*y_prima))

    solved_arr["Σy'"] = ind[0]
    solved_arr["Σxy'"] = ind[1]

    ab = np.linalg.solve(array, ind)
    ans = {}
    ans["A'"] = ab[0]
    ans["B'"]= ab[1]
    ans["B"] = f"A' => B = {ab[0]}"
    ans["Ln(A)"] = "B'"
    ans["e^Ln(A)"] = "e^B'"
    ans["A"] = "e^B'" 
    ans["e^B'"] = f"e^{ab[1]}"
    ans["A"] = np.exp(ab[1])
    return array, ind, ans, solved_arr


def r_nonlinear_exponential(data: dict):
    x = data['x']
    y = data['y']
    
    x = np.array(x)
    y = np.array(y)
    
    
    g_array, indep, answer, solved_arr = calculate(x, y)
    return {
            'general formula': "y' = A'x + B'; y' = Ln(y); A' = B; B' = Ln(A)",
            'n': solved_arr['n'],
            'array scheme': "[[Σx, n], [Σx^2, Σx]] [A', B'] = [Σy', Σxy']",
            'general array': g_array,
            'Independe': indep,
            'answer': answer
            }
