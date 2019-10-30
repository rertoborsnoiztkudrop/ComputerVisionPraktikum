'''
Aufgabe 3.1.3
'''

import numpy as np


def ConfusionMatrix(prediction, validation, labelCount):
    '''

    :param prediction: the 1-Dimensional Array of predicted Labels
    :param validation: the 1-Dimensional Array of actual Labels
    :param labelCount: the numer of labels
    :return: a labelCount x labelCount ConfusionMatrix
    '''

    matrix = np.zeros((labelCount, labelCount), dtype=int)

    for i in range(len(prediction)):
        matrix[validation[i], prediction[i]] += 1

    return matrix

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

print(ConfusionMatrix(trMatch, vdLabels, 9))
