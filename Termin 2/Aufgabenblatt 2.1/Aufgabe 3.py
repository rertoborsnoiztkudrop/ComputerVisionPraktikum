"""
Aufgabe 3 von Blatt 2.1
"""
from skimage.io import imread

img = imread("./catG.png")

print("n:", img.size)
print("max:", img.max())
print("min:", img.min())
print("avg:", img.mean())

