"""
Aufgabe 3.2.1
"""

import numpy as np
from skimage.io import imread, imsave

img = imread("./cat.png")

rotKanal = img[:,:,0]
gruenKanal = img[:,:,1]
blauKanal = img[:,:,2]

#1.2
grau = (rotKanal/3 + gruenKanal/3 + blauKanal/3)

imsave("./catGrau.png",grau)

#1.3
imsave("./catRot.png",rotKanal)
imsave("./catGruen.png", gruenKanal)
imsave("./catBlau.png", blauKanal)

#1.4
imsave("./catFalsch.png", np.dstack((gruenKanal, blauKanal, rotKanal)))

#1.5
imsave("./catInverse.png",255 - img)

#1.6
print("Mittelwert: ", np.mean(img, axis = (0,1)))
print("Standardabweichung: ", np.std(img, axis =(0,1)))