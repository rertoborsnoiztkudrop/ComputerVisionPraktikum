"""
Aufgabe 1 von Blatt 2.1
"""
from skimage.io import imread
import matplotlib.pyplot as plt

def NumberOfPixels(img):
    '''
    Berechnet die Anzahl Pixel eines Bildes
    :param img: das Bild
    :return: die Anzahl Pixel
    '''
    return img.shape[0] * img.shape[1]

def MaxValImg(img):
    '''
    Gibt den Wert des hellsten Pixels in einem Graustufenbild wieder.
    :param img: das Bild
    :return: der höchste (hellste) Wert
    '''
    n = -1
    for x in range(img.shape[0]):
        n = max([n, max(img[x, : ])])

    return n

def MinValImg(img):
    '''
    Gibt den Wert des dunkelsten Pixels in einem Graustufenbild wieder.
    :param img: das Bild
    :return: der niedrigste (dunkelste) Wert
    '''
    n = 256
    pos = [-1, -1]
    for x in range(img.shape[0]):
        n = min([n, min(img[x, : ])])

    if n == 256:
        return -1
    else:
        return n


def AvgValImg(img):
    '''
    Berechnet den Graumittelwert eines Bildes
    :param img: das Bild
    :return: der Graumittelwert
    '''
    n = 0
    for x in range(img.shape[0]):
        n += mean(img[x, :])

    return n / img.shape[0]

def mean(collection):
    '''
    Gibt den Mittelwert einer Collection
    :param collection: die Collection
    :return: der Mittelwert
    '''
    n = 0
    for x in collection:
        n += x

    return n / len(collection)


img = imread("./catG.png")
plt.imshow(img, cmap="Greys_r")
print(NumberOfPixels(img))
print(MaxValImg(img))
print(MinValImg(img))
print(AvgValImg(img))