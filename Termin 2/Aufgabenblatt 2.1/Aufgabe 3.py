from skimage.io import imread, imsave

img = imread("./catG.png")

print("n:", img.size)
print("max:", img.max())
print("min:", img.min())
print("avg:", img.mean())

