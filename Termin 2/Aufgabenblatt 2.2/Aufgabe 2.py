"""
Aufgabe 2 von Blatt 2.2
"""

import numpy as np
from skimage.io import imread


def HistogrammVergleichEuklid(hist1, hist2):
    """
    Vergleicht zwei (gleich lange) Histogramme anhand der euklidischen Differenz
    :param hist1: das erste Histogramm
    :param hist2: das zweite Histogramm
    :return: Die Euklidische Differenz der beiden Histogramme
    """
    distanz = 0
    for i in range(len(hist1)):
        distanz += (hist1[i] - hist2[i]) ** 2
    distanz = np.sqrt(distanz)

    return distanz


def HistogrammVergleichIntersection(hist1, hist2):
    '''
    Vergleicht zwei (gleich lange) Histogramme anhand der Intersection
    :param hist1: das erste Histogramm
    :param hist2: das zweite Histogramm
    :return: Die Gleichheit  der beiden Histogramme zwischen 0 und 1
    '''

    intersection = 0
    total = 0
    for i in range(len(hist1)):
        total += hist1[i]
        intersection += min(hist1[i], hist2[i])
    return intersection / total


agri3 = imread("./satBilder/agri3.png")
agri6 = imread("./satBilder/agri6.png")
urban1 = imread("./satBilder/urban1.png")

agri3Hist = np.histogram(agri3, bins=8, range=(0, 256))
agri6Hist = np.histogram(agri6, bins=8, range=(0, 256))
urban1Hist = np.histogram(urban1, bins=8, range=(0, 256))

print("Unterschied zwischen agri3 und agri6 \n"
      f"\t Euklidisch: {HistogrammVergleichEuklid(agri3Hist[0], agri6Hist[0])}"
      f"\t Intersection: {HistogrammVergleichIntersection(agri3Hist[0], agri6Hist[0])}"
      )
print("Unterschied zwischen agri3 und urban1 \n"
      f"\t Euklidisch: {HistogrammVergleichEuklid(agri3Hist[0], urban1Hist[0])}"
      f"\t Intersection: {HistogrammVergleichIntersection(agri3Hist[0], urban1Hist[0])}"
      )
print("Unterschied zwischen agri6 und urban1 \n"
      f"\t Euklidisch: {HistogrammVergleichEuklid(agri6Hist[0], urban1Hist[0])}"
      f"\t Intersection: {HistogrammVergleichIntersection(agri6Hist[0], urban1Hist[0])}"
      )
