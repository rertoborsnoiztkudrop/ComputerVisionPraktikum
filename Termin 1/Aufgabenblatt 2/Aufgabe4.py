kosten = int(input("Was kostet das Essen?: "))
Münzen = [200, 100, 50, 20, 10, 5, 2, 1]
Lösung = {}

for x in Münzen:
    Lösung[x] = int(kosten / x)
    kosten = kosten % x

for x in Münzen:
    print(f"{x}: {Lösung[x]}")
