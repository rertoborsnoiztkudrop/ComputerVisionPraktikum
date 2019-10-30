'''
Aufgabe 3.1.1
'''

import numpy as np


def find_nearest_index(array, target):
    '''
    Find the index of the value closest to target.
    :param array: The array to search in.
    :param target: The target value to find the closest value to.
    :return: The index of the closest value in the array.
    '''
    array = np.asarray(array)
    return (np.abs(array - target)).argmin()


# 1.1
td = np.load('./trainingsDaten.npz')
vd = np.load('./validierungsDaten.npz')

# 1.2
trDesk = list(map(lambda x: np.mean(x) + np.std(x), td['data']))
vdDesk = list(map(lambda x: np.mean(x) + np.std(x), vd['data']))

# 1.3 + 1.4
trMatch = list(map(lambda vd: td['labels'][find_nearest_index(trDesk, vd)], vdDesk))

# 1.5
tp = sum(list(map(lambda x, y: x == y, trMatch, vd['labels'])))

print("Trefferquote:", tp / len(vdDesk) * 100, "%")
