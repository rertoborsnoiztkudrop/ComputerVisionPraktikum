"""
Aufgabe 5 von Blatt 1.2
"""

def findSmallestDivisor(n):
    """
    Findet den kleinsten echten Teiler einer Ganzzahl.
    :param n: Die Zahl für die der kleinste echte Teiler gesuchte wird
    :return: Den kleinsten geminsamen Teiler und den Quotienten
    """
    if n % 2 == 0:
        return 2, n // 2

    for i in range(3, int(n**0.5 + 1), 2):
        if(n % i == 0):
            return i, n // i

    return n, 1

def primeFactors(n):
    """
    Gibt die Primfaktorzerlegung einer Zahl als Liste aus.
    :param n: die Zahl des Primfaktorzerlegung gesucht wird
    :return: die Primfaktorzerlegung als Liste
    """
    primFaktoren =[]
    while n > 1:
        i, n = findSmallestDivisor(n)
        primFaktoren.append(i)

    return primFaktoren

def zerlegungToString(zerlegung):
    """
    Verwandelt eine Primfaktorzerlegung in einen String der Form 2*3*3
    :param zerlegung: die Zerlegung die ausgegebnen werden soll
    :return: String der Form 2*3*5*7
    """
    s = str(zerlegung[0])
    for i in range(1,len(zerlegung)):
        s = s +"*" + str(zerlegung[i])
    return s


zahl = int(input("Welche Zahl?: "))
zerlegung = primeFactors(zahl)
print(f"{zahl} = " + zerlegungToString(zerlegung))

#  600851475147 = 3*7*7*11*163*2279657
