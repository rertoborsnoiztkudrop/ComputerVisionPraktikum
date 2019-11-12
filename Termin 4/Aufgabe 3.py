"""
Aufgabe 4.3
"""

import glob
import numpy as np
from skimage.io import imread, imsave
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from skimage.transform import rotate

def bestRotationDegree(mask):
    """
    Calculates the best degree of rotation for a binary picture, s.t. the bounding box is minimal
    :param mask: the binary picture
    :return: the best rotation degree
    """
    size = mask.shape[0] * mask.shape[1]
    min = 0
    for deg in range(90):
        rotMask = rotate(mask, deg, order=0)
        rotMask = rotMask.astype(np.int)
        props = regionprops(rotMask)[0]
        rotSize = (props.bbox[2]-props.bbox[0])*(props.bbox[3]-props.bbox[1])
        if rotSize < size:
            size = rotSize
            min = deg
    return min


# Einlesen der Pfadstrings
trStrings = glob.glob("./haribo2/hariboTrain2/*.png")
vdStrings = glob.glob("./haribo2/hariboVal2/*.png")

#3.2
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
    imsave("./haribo2/hariboTrainErgebnisse2/"+trStrings[i].split("/")[-1], trImgs[i])

for i in range(len(vdImgs)):
    vdMasks[i] = vdMasks[i].astype(np.int)
    props = regionprops(vdMasks[i])[0]
    vdImgs[i] = vdImgs[i][props.bbox[0]:props.bbox[2],props.bbox[1]:props.bbox[3],:]
    imsave("./haribo2/hariboValErgebnisse2/"+vdStrings[i].split("/")[-1], vdImgs[i])

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


#3.3
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

# Das Rotieren(!) und Schneiden der Bilder
for i in range(len(trImgs)):
    #!!hier verändert!!
    deg = bestRotationDegree(trMasks[i])
    trMasks[i] = rotate(trMasks[i], deg, order=0)
    trMasks[i] = trMasks[i].astype(np.int)
    props = regionprops(trMasks[i])[0]
    trImgs[i] = rotate(trImgs[i], deg, order = 0)
    #ab hier wieder unverändert
    trImgs[i] = trImgs[i][props.bbox[0]:props.bbox[2],props.bbox[1]:props.bbox[3],:]
    imsave("./haribo2/hariboTrainErgebnisse2/"+trStrings[i].split("/")[-1], trImgs[i])

for i in range(len(vdImgs)):
    #!!hier verändert!!
    deg = bestRotationDegree(vdMasks[i])
    vdMasks[i] = rotate(vdMasks[i], deg, order=0)
    vdMasks[i] = vdMasks[i].astype(np.int)
    props = regionprops(vdMasks[i])[0]
    vdImgs[i] = rotate(vdImgs[i], deg, order = 0)
    #ab hier wieder unverändert
    vdImgs[i] = vdImgs[i][props.bbox[0]:props.bbox[2],props.bbox[1]:props.bbox[3],:]
    imsave("./haribo2/hariboValErgebnisse2/"+vdStrings[i].split("/")[-1], vdImgs[i])

#Deskripor Verhältnis Höhe Breite
trDesk = []
for i in range(len(trImgs)):
    trDesk.append(max(trImgs[i].shape[0]/trImgs[i].shape[1], trImgs[i].shape[1]/trImgs[i].shape[0]))
trDesk = np.asarray(trDesk)

vdDesk = []
for i in range(len(vdImgs)):
    vdDesk.append(max(vdImgs[i].shape[0]/vdImgs[i].shape[1],vdImgs[i].shape[1]/vdImgs[i].shape[0]))
vdDesk = np.asarray(vdDesk)

trMatch = [0] * vdDesk.shape[0]
deltaDesk = [0] * trDesk.shape[0]

for i in range(vdDesk.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trDesk.shape[0]):
        deltaDesk[j] = np.abs(x[j])
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = trLabels[n]

tp = sum(list(map(lambda x, y: x == y, trMatch, vdLabels)))

print("Trefferquote mit Höhe-Breite Verhältnis:", tp / len(vdDesk) * 100, "%")


#3.4
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

# Das Speichern der Deskriptoren mittels Exzentrizität!!!
trDesk = []
for i in range(len(trImgs)):
    trMasks[i] = trMasks[i].astype(np.int)
    props = regionprops(trMasks[i])[0]
    trDesk.append(props.eccentricity)
trDesk = np.asarray(trDesk)

vdDesk = []
for i in range(len(vdImgs)):
    vdMasks[i] = vdMasks[i].astype(np.int)
    props = regionprops(vdMasks[i])[0]
    vdDesk.append(props.eccentricity)
vdDesk = np.asarray(vdDesk)

trMatch = [0] * vdDesk.shape[0]
deltaDesk = [0] * trDesk.shape[0]

for i in range(vdDesk.shape[0]):
    x = (trDesk - vdDesk[i])
    for j in range(trDesk.shape[0]):
        deltaDesk[j] = np.abs(x[j])
    n = deltaDesk.index(min(deltaDesk))
    trMatch[i] = trLabels[n]

tp = sum(list(map(lambda x, y: x == y, trMatch, vdLabels)))

print("Trefferquote mit Exzentrizität:", tp / len(vdDesk) * 100, "%")