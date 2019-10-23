from skimage.io import imread, imsave
import matplotlib.pyplot as plt

def NumberOfPixels(img):
    '''

    :param img:
    :return:
    '''
    return img.shape[0] * img.shape[1]

def MaxValImg(img):
    '''

    :param img:
    :return:
    '''
    n = -1
    for x in range(img.shape[0]):
        n = max([n, max(img[x, : ])])

    return n

def MinValImg(img):
    '''

    :param img:
    :return:
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

    :param img:
    :return:
    '''
    n = 0
    for x in range(img.shape[0]):
        n += mean(img[x, :])

    return n / img.shape[0]

def mean(collection):
    '''

    :param collection:
    :return:
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