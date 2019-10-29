"""
Aufgabe 1 von Blatt2.2
"""

import numpy as np
from skimage.io import imread

def BildVergleich (img1, img2):
    """
    Vergleicht zwei Bildwerte anhand des Graumittelwertes beider Bilder (gibt die Differenz aus)
    :param img1: das erste Bild
    :param img2: das zweite Bild
    :return: Die Differenz der Graumittelwerte
    """
    return np.abs(img1.mean()-img2.mean())

agri3 = imread("./satBilder/agri3.png")
agri6 = imread("./satBilder/agri6.png")
urban1 = imread("./satBilder/urban1.png")

print("Unterschied zwischen agri3 und agri6:", BildVergleich(agri3,agri6))
print("Unterschied zwischen agri3 und urban1:", BildVergleich(agri3,urban1))
print("Unterschied zwischen agri6 und urban1:", BildVergleich(agri6,urban1))