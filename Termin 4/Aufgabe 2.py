"""
Aufgabe 4.2
"""

import glob
import numpy as np
from skimage.io import imread, imsave
from skimage.measure import regionprops
from skimage.filters import threshold_otsu

# Einlesen der Pfadstrings
trStrings = glob.glob("./haribo1/hariboTrain/*.png")
vdStrings = glob.glob("./haribo1/hariboVal/*.png")

# Einlesen der Bilder
trImgs = []
for i in range(len(trStrings)):
    trImgs.append(imread(trStrings[i]))

vdImgs = []
for i in range(len(vdStrings)):
    vdImgs.append(imread(vdStrings[i]))

#Einlesen der Labels
trLabels = []
for i in range(len(trStrings)):
    trLabels.append(trStrings[i].split("/")[-1].split("_")[0])

vdLabels = []
for i in range(len(vdStrings)):
    vdLabels.append(vdStrings[i].split("/")[-1].split("_")[0])

# Verwandeln der Bilder in GraustufenBilder
trImgsG =[]
for img in trImgs:
    trImgsG.append(img[:,:,0]/3 +img[:,:,1]/3 +img[:,:,2]/3)

vdImgsG = []
for img in vdImgs:
    vdImgsG.append(img[:,:,0]/3 +img[:,:,1]/3 +img[:,:,2]/3)


# (willkürliche) Setzung des Grenzwertes
grenzwert = 100

# Erstellung der Binärbilder
trMasks = []
for img in trImgsG:
    trMasks.append(img < threshold_otsu(img))  #oder grenzwert

vdMasks = []
for img in vdImgsG:
    vdMasks.append(img < threshold_otsu(img))  #oder grenzwert

# Das Schneiden der Bilder
for i in range(len(trImgs)):
    trMasks[i] = trMasks[i].astype(np.int)
    props = regionprops(trMasks[i])[0]
    trImgs[i] = trImgs[i][props.bbox[0]:props.bbox[2],props.bbox[1]:props.bbox[3],:]
    imsave("./haribo1/hariboTrainErgebnisse/"+trStrings[i].split("/")[-1], trImgs[i])

for i in range(len(vdImgs)):
    vdMasks[i] = vdMasks[i].astype(np.int)
    props = regionprops(vdMasks[i])[0]
    vdImgs[i] = vdImgs[i][props.bbox[0]:props.bbox[2],props.bbox[1]:props.bbox[3],:]
    imsave("./haribo1/hariboValErgebnisse/"+vdStrings[i].split("/")[-1], vdImgs[i])

#Ab hier Aufgabe 1 kopiert:
#den np.mean teil musste ich ändern, komischerweise hat es vorher nicht funktioniert
trDesk = []
for i in range(len(trImgs)):
    trDesk.append(np.mean(trImgs[i], axis=(0, 1)))
trDesk = np.asarray(trDesk)

vdDesk = []
for i in range(len(vdImgs)):
    vdDesk.append(np.mean(vdImgs[i], axis=(0, 1)))
vdDesk = np.asarray(vdDesk)

trMatch = [0] * vdDesk.shape[0]
deltaDesk = [0] * trDesk.shape[0]

for i in range(vdDesk.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trDesk.shape[0]):
        deltaDesk[j] = np.sqrt(np.sum((x[j, :])**2))
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = trLabels[n]

tp = sum(list(map(lambda x, y: x == y, trMatch, vdLabels)))

print("Trefferquote mit Mittelwert:", tp / len(vdDesk) * 100, "%")

#3D Histogramm (Vielleicht durch mehr Variabeln besser lesbar):
trDesk =[]
for i in range(len(trImgs)):
    trDesk.append(np.histogramdd(trImgs[i].reshape((trImgs[i].shape[0]*trImgs[i].shape[1],3)), bins = [8,8,8], range=((0,256),(0,256),(0,256)))[0])
trDesk = np.asarray(trDesk)
vdDesk = []
for i in range(len(vdImgs)):
    vdDesk.append(np.histogramdd(vdImgs[i].reshape((vdImgs[i].shape[0]*vdImgs[i].shape[1],3)), bins = [8,8,8], range=((0,256),(0,256),(0,256)))[0])
vdDesk = np.asarray(vdDesk)



#Ab hier Copy-Paste von oben, ausgelagerte Fktn wären schöner
trMatch = [0] * vdDesk.shape[0]
deltaDesk = [0] * trDesk.shape[0]

for i in range(vdDesk.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trDesk.shape[0]):
        deltaDesk[j] = np.sqrt(np.sum((x[j, :])**2))
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = trLabels[n]

tp = sum(list(map(lambda x, y: x == y, trMatch, vdLabels)))

print("Trefferquote mit 3D-Histogramm:", tp / len(vdDesk) * 100, "%")