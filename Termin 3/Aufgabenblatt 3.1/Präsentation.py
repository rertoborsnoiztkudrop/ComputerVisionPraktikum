'''
Präsentation
'''

import numpy as np

trainingsData = np.load('./trainingsDaten.npz')
validationData = np.load('./validierungsDaten.npz')

trainingsImages = trainingsData['data']
trainingsLabels = trainingsData['labels']

validationImages = validationData['data']
validationLabels = validationData['labels']

trainingsDescriptors = np.mean(trainingsImages, axis=(1, 2))
validationDescriptors = np.mean(validationImages, axis=(1, 2))

trDesc = np.tile(trainingsDescriptors, (len(validationDescriptors), 1))

deltaDescriptors = np.abs(trDesc - validationDescriptors[:, None])

index = np.argmin(deltaDescriptors, axis=1)
predictions = trainingsLabels[index]

evaluatedPredictions = predictions == validationLabels
correctPredictions = sum(evaluatedPredictions)
print("Trefferquote:", correctPredictions / len(validationLabels) * 100, "%")
