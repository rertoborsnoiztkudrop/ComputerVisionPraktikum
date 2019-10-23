import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

def CountPixelsForTone(img):
    '''

    :param img:
    :return:
    '''

    result = {}
    for x in range(256):
       result[x] = sum(sum(x == y for y in img))

    return result



img = imread("./catG.png")
print("Schwarze Pixel:", sum(sum(x == 0 for x in img)))
print("Weiße Pixel:", sum(sum(x == 255 for x in img)))
print(CountPixelsForTone(img))