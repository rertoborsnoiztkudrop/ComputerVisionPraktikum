"""
Aufgabe 3.2.3
"""


import numpy as np

# 1.1
td = np.load('./trainingsDatenFarbe2.npz')
vd = np.load('./validierungsDatenFarbe2.npz')

# 1.2
trDesk = np.zeros((td['data'].shape[0],15,3))
vdDesk = np.zeros((vd['data'].shape[0],15,3))

for i in range(trDesk.shape[0]):
    histR = np.histogram(td['data'][i,:,:,0],bins = 15, range = (0, 256))[0]
    histG = np.histogram(td['data'][i,:,:,1],bins = 15, range = (0, 256))[0]
    histB = np.histogram(td['data'][i,:,:,2],bins = 15, range = (0, 256))[0]
    trDesk[i] = np.dstack((histR,histG,histB))                               #dstack benutzt statt hstack...

for i in range(vdDesk.shape[0]):
    histR = np.histogram(vd['data'][i,:,:,0],bins = 15, range = (0, 256))[0]
    histG = np.histogram(vd['data'][i,:,:,1],bins = 15, range = (0, 256))[0]
    histB = np.histogram(vd['data'][i,:,:,2],bins = 15, range = (0, 256))[0]
    vdDesk[i] = np.dstack((histR,histG,histB))

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
