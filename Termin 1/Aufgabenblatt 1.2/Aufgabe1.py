"""
Aufgabe 1 von Blatt 1.2
"""

i = int(input("Gib mir eine ungerade Zahl: "))
x = i % 2   #zum Prüfen ob i ungerade ist

while(x != 1):   #in dieser Schleife wird sicher gestellt, dass am Ende eine ungerade Zahl ist
    print("Die Zahl muss ungerade sein!")
    i = int(input("Gib mir eine ungerade Zahl: "))
    x = i % 2

y = 1
for j in range(1,i+1,2):
    y = y * j

print (y)