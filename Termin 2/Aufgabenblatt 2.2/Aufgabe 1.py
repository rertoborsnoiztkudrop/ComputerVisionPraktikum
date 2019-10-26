import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

def BildVergleich (img1, img2):
    """

    :param img1:
    :param img2:
    :return:
    """
    return np.abs(AvgValImg(img1)-AvgValImg(img2))

def AvgValImg(img):
    """

    :param img:
    :return:
    """
    n= 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            n += img[x,y]
    n = n/(img.shape[0]*img.shape[1])
    return n

agri3 = imread("./satBilder/agri3.png")
agri6 = imread("./satBilder/agri6.png")
urban1 = imread("./satBilder/urban1.png")

print("Unterschied zwischen agri3 und agri6:", BildVergleich(agri3,agri6))
print("Unterschied zwischen agri3 und urban1:", BildVergleich(agri3,urban1))
print("Unterschied zwischen agri6 und urban1:", BildVergleich(agri6,urban1))