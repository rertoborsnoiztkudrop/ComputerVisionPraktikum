'''
Präsentation
'''

import numpy as np

td = np.load('./trainingsDaten.npz')
vd = np.load('./validierungsDaten.npz')
trDesk = np.mean(td['data'], axis=(1, 2))
vdDesk = np.mean(vd['data'], axis=(1, 2))
trDesk = np.tile(trDesk, (vdDesk.size, 1))
deltDesk = np.abs(trDesk - vdDesk[:, None])
index = np.argmin(deltDesk, axis=1)
predicitions = np.take(td['labels'], index)
correctPrediction = predicitions == vd['labels']
tp = sum(correctPrediction)
print("Trefferquote:", tp / len(vdDesk) * 100, "%")
