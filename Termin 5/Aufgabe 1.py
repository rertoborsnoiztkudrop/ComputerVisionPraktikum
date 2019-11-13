"""
Aufgabe 5.1
"""

import numpy as np
from skimage.io import imread, imshow
import time
from scipy.ndimage.filters import convolve

#_____________________Aufgabe 1.1 und 1.2 __________________
img2 = imread("./catGNoisy.png")

entfernungNachbarn = 1  #Bestimmt den Grad an "Weichheit"  -> Aufgabe 1.4 bzw 1.5
                        # 1 bedeutet zb. alle direkten Nachbarn werden berücksichtigt

imgTrauerrand = np.zeros((img2.shape[0] + 2 * entfernungNachbarn, img2.shape[1] + 2 * entfernungNachbarn))
imgTrauerrand[entfernungNachbarn:-entfernungNachbarn, entfernungNachbarn:-entfernungNachbarn] = img2

tic2= time.time()

for x in range(img2.shape[0]):
    for y in range(img2.shape[1]):
        img2[x, y]= np.mean(imgTrauerrand[x:x + 2 * entfernungNachbarn, y:y + 2 * entfernungNachbarn])

toc2 = time.time()

laufzeit2 = toc2-tic2

#imshow(img2, cmap="Greys_r")
print(" Die Laufzeit von  Aufgabe 1.2 : " , laufzeit2)

#___________________ Aufgabe 1.3_____________________________
img3= imread("./catGNoisy.png")
mittelwertFilterShape = entfernungNachbarn*2+1 #Bestimmt den Grad an "Weichheit"   -> Zusatzaufgabe 1.5
mittelwertFilter = (1/(mittelwertFilterShape**2)) * np.ones((mittelwertFilterShape,mittelwertFilterShape))


tic3= time.time()

img3 = convolve(img3,mittelwertFilter)

toc3 = time.time()
laufzeit3 = toc3-tic3

imshow(img3, cmap="Greys_r")
print(" Die Laufzeit von  Aufgabe 1.3 : " , laufzeit3)


#___________________ Aufgabe 1.4_____________________________
# variiere die Variable entfernungNachbarn !:)