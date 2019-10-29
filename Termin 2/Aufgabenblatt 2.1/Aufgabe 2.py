"""
Aufgabe 2 von Blatt 2.2
"""
from skimage.io import imread

def CountPixelsForTone(img):
    '''
    Gibt eine Map aus, die jeder Graustufe zuweist, wie oft sie in einem Bild vorkommt.
    :param img: Das Bild welches analysiert wird.
    :return: Die Map die sagt, welche Graustufe wie oft im Bild vorkommt.
    '''

    result = {}
    for x in range(256):
       result[x] = sum(sum(x == y for y in img))

    return result



img = imread("./catG.png")
print("Schwarze Pixel:", sum(sum(x == 0 for x in img)))  #Anzahl schwarzer Pixel
print("Weiße Pixel:", sum(sum(x == 255 for x in img)))   #Anzahl weißer Pixel
print(CountPixelsForTone(img))                           #Wie viele Pixel von jeder Graustufe