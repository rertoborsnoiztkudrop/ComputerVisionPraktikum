"""
Aufgabe 3 von Blatt 1.1
"""

wechselkurse = {"England": (0.86, "Pfund"),
                "Schweiz": (1.1, "Schweizer Franken"),
                "USA": (1.11, "US-Dollar"),
                "Norwegen": (10.16, "Norwegische Kronen"),
                "Polen": (4.29, "Zloty"),
                "Japan": (120.14, "Yen")}

land = input("Ein land bitte: ")
betrag = float(input("Wie viele Euro hast du?: "))
tupel = wechselkurse.get(land)
if tupel is None:
    print("Land nicht gefunden: " + land)
else:
    print(str(betrag * tupel[0]) + " " + tupel[1])
