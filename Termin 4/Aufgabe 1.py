"""
Aufgabe 4.1
"""
import glob
import numpy as np
from skimage.io import imread

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


#Aus der vorherigen Aufgabe übernommen
trDesk = np.mean(trImgs, axis=(1, 2))
vdDesk = np.mean(vdImgs, axis=(1, 2))

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