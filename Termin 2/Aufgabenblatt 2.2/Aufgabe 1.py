import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

def BildVergleich (img1, img2):
    """

    :param img1:
    :param img2:
    :return:
    """
    unterschied = np.zeros(img1.shape, dtype=np.uint8) #TODO: was tun bei unterschiedlichen Bildgrößen?
    for x in range(img1.shape[0]):
        for y in range(img1.shape[1]):
            unterschied[x,y] = np.sqrt(img1[x,y]**2 + img2[x,y]**2)
    return unterschied

img1 = imread("./satBilder/agri3.png")
img2 = imread("./satBilder/agri6.png")
unterschied = BildVergleich(img1, img2)

plt.imshow(unterschied, cmap="Greys_r")

#Aufgabe voll falsch verstanden, ich mach das noch richtig :D