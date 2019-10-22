"""
Aufgabe 5 von Blatt 1.2
"""

def isPrime(n):
    """
    Überprüft ob eine Zahl Primzahl ist.

    :param n: die Zahl die geprüft wird
    :return: true, falls primzahl sonst false
    """
    for i in range(2,n):
        if(n/i % 1 == 0):
            return False

    return True

def primeFactors(n):
    """
    Gibt die Primfaktorzerlegung einer Zahl als Liste aus.
    :param n: die Zahl des Primfaktorzerlegung gesucht wird
    :return: die Primfaktorzerlegung als Liste
    """
    primFaktoren =[]
    i = 2
    while n != 1:
        if(isPrime(i) and n/i % 1 ==0):
            primFaktoren.append(i)
            n = n/i
        else:
            i += 1
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