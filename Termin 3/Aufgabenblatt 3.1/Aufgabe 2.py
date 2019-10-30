'''
Aufgabe 3.1.2
'''

import numpy as np

#1.1
td = np.load('./trainingsDaten.npz')
trImgs = td['data']
trLabels = td['labels']

vd = np.load('./validierungsDaten.npz')
vdImgs = vd['data']
vdLabels = vd['labels']

#1.2
trDesk = [0] * trImgs.shape[0]
vdDesk = [0] * vdImgs.shape[0]

for i in range(trImgs.shape[0]):
    trDesk[i] = np.histogram(trImgs[i, :, :], bins= 15, range=(0, 256))[0]

for i in range(vdImgs.shape[0]):
    vdDesk[i] = np.histogram(vdImgs[i, :, :], bins= 15, range=(0, 256))[0]

#1.3 + 1.4
trMatch = [0] * vdImgs.shape[0]
deltaDesk = [0] * trImgs.shape[0]

for i in range(vdImgs.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trImgs.shape[0]):
        deltaDesk[j] = np.sqrt(np.sum((x[j, :])**2))
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = trLabels[n]

#1.5
tp = 0
for i in range(vdImgs.shape[0]):
    if(vdLabels[i] == trMatch[i]):
        tp += 1

print("Trefferquote:", tp / vdImgs.shape[0] * 100, "%")
