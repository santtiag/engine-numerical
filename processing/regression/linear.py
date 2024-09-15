import numpy as np

def calculate(x, y):
    n = len(x)
    array = []
    
    solved_array = {}
    e_1 = {}
    e_2 = {}
    
    print('AΣx + nB = Σy')
    e_1[f'A{np.sum(x)} + B{n}'] = np.sum(y)
    array.append([np.sum(x), n])
    
    solved_array['n'] = n
    solved_array['Σx'] = np.sum(x)
    solved_array['Σy'] = np.sum(y)


    print('AΣx^2 + BΣx = Σxy')
    e_2[f'A{np.sum(x**2)} + B{np.sum(x)}'] = np.sum(x*y)
    array.append([np.sum(x**2), np.sum(x)])
    
    solved_array['Σx^2'] = np.sum(x**2)
    solved_array['Σxy'] = np.sum(x*y)

    ind = [np.sum(y), np.sum(x*y)]
    
    
    ab = np.linalg.solve(array, ind)
    
    solved_array['A'] = ab[0]
    solved_array['B'] = ab[1]

    f_e = f'y = {ab[0]} x + {ab[1]}'
    
    return e_1, e_2, ind, f_e, solved_array
    


def r_linear(data: dict):
    # NOTE: Cambio de datos
    x = data['x']
    y = data['y']
    x = np.array(x)
    y = np.array(y)

    # número de parejas
    equ_1, equ_2, indep, final_equ, solved_arr = calculate(x, y)

    return {
            'general formula':'d/dB (y - (Ax + B))^2',
            'n': solved_arr['n'],
            'AΣx + nB = Σy': equ_1,
            'AΣx^2 + BΣx = Σxy': equ_2,
            'independent': indep,
            'array scheme': '[[Σx, n], [Σx^2, Σx]] [A, B] = [Σy, Σxy]',
            'solved array scheme': f"[[{solved_arr['Σx']}, {solved_arr['n']}], [{solved_arr['Σx^2']}, {solved_arr['Σx']},]] [{solved_arr['A']}, {solved_arr['B']}] = [{solved_arr['Σy']}, {solved_arr['Σxy']}]",
            'final equation': final_equ
            }
