'''
Aufgabe 4 von Blatt 2.1
'''

import numpy as np
from skimage.io import imread, imsave

img = imread("./catG.png")

# inverse image
img_inverse = np.zeros(img.shape, dtype=np.uint8)
for x in range(img_inverse.shape[0]):
    for y in range(img_inverse.shape[1]):
        img_inverse[x, y] = 255 - img[x, y]
imsave("./catG_inversed.png", img_inverse)

# mirror image along the vertical axis
img_mirrored = np.zeros(img.shape, dtype=np.uint8)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        img_mirrored[x, y] = img[x, img.shape[1] - y - 1]
imsave("./catG_mirrored.png", img_mirrored)

# Cut out head
img_head = img[17:260, 260:495]
imsave("./catG_head.png", img_head)
