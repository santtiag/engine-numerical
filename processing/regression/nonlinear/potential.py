import numpy as np

def calculate(x, y):
    n = len(x)
    solved_arr = {}
    ans = {}
    
    y_ = np.log(y)
    x_ = np.log(x)
    
    arr  = []
    ind  = []
    
    arr.append([np.sum(x_), n])
    arr.append([np.sum(x_**2), np.sum(x_)])

    solved_arr['n'] = n
    solved_arr["Σx'"] = np.array(x_)
    solved_arr["Σx'^2"] = np.array(x_**2)


    ind = ([np.sum(y_), np.sum(x_*y_)])
    
    ab = np.linalg.solve(arr, ind)
    
    solved_arr["Σy'"] = ind[0]
    solved_arr["Σx'y'"] = ind[1]
    solved_arr["A'"] = ab[0]
    solved_arr["B'"] = ab[1]

    ans["A'"] = ab[0]
    ans["B'"] = ab[1]
    ans["B'"] = "A'"
    ans["B"] = ab[0]
    ans["Ln(A)"] = "B'"
    ans["e^Ln(A)"] = "e^B'"
    ans["A"] = "e^B'"
    ans["'A"]= f"e^{ab[1]}"
    ans["A"] = np.exp(ab[1])
    ans["y"] = f"{np.exp(ab[1])} * x^{ab[0]}"

    ab = np.linalg.solve(arr, ind) 
    return solved_arr, ans

def r_nonlinear_potential(data: dict):
    x = data['x']
    y = data['y']

    x = np.array(x)
    y = np.array(y)

    solved_arr, ans = calculate(x, y)

    return {
            'general formula': 'y = A * x^B',
            'array scheme': "[[Σx', n], [Σx'^2, Σx']] [A', B'] = [Σy', Σx'y']",
            'solved array scheme': f"[[{solved_arr['Σx\'']}, {solved_arr['n']}], [{solved_arr['Σx\'^2']}, {solved_arr['Σx\'']}], [{solved_arr['A\'']}, {solved_arr['B\'']}] = [{solved_arr['Σy\'']}, {solved_arr['Σx\'y\'']}]",

            # f"[[{solved_arr["Σx'"]}, {solved_arr['n']}], [{solved_arr["Σx'^2"]}, {solved_arr["Σx'"]}], [{solved_arr["A'"]}, {solved_arr["B'"]}] = [{solved_arr["Σy'"]}, {solved_arr["Σx'y'"]}]",
            'answer': ans
            }
 

