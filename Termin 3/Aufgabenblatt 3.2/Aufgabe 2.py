"""
Aufgabe 3.2.2
"""

import numpy as np

# 1.1
td = np.load('./trainingsDatenFarbe2.npz')
vd = np.load('./validierungsDatenFarbe2.npz')

# 1.2
trDesk = np.mean(td['data'], axis=(1, 2))
vdDesk = np.mean(vd['data'], axis=(1, 2))

# 1.3 + 1.4
trMatch = [0] * vdDesk.shape[0]
deltaDesk = [0] * trDesk.shape[0]

for i in range(vdDesk.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trDesk.shape[0]):
        deltaDesk[j] = np.sqrt(np.sum((x[j, :])**2))
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = td["labels"][n]

# 1.5
tp = sum(list(map(lambda x, y: x == y, trMatch, vd['labels'])))

print("Trefferquote:", tp / len(vdDesk) * 100, "%")
