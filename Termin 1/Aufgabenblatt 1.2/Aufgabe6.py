"""
Aufgabe 6 von Blatt1.2
"""
wanze = "Wanze"
tanzen = "tanzen"

for i in range(6):
    for j in range(2):
        print("Auf der Mauer, auf der Lauer sitzt 'ne kleine " + wanze + ".")
    print("Seht euch nur die " + wanze + " an, wie die " + wanze + " " + tanzen + " kann!" )
    print("Auf der Mauer, auf der Lauer sitzt 'ne kleine " + wanze + ".")
    print("")

    if i == 0:
        tanzen = tanzen[:-2]

    else:
        tanzen = tanzen[: -1]

    wanze = wanze[:-1]