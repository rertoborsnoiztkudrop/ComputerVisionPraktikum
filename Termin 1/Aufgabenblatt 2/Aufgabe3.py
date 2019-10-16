myList = [0] * 5

for i, n in enumerate(myList):
    myList[i] = float(input(f"Die {i+1}. Zahl bitte: "))

print(myList)
print(f"min: {min(myList)} at {myList.index(min(myList))}")
print(f"max: {max(myList)} at {myList.index(max(myList))}")
myList.sort()
print("median", myList[2])
print("ungrade", sum(x % 2 != 0 for x in myList))
print("grade", sum(x % 2 == 0 for x in myList))
print("unterschiedlich", len(set(myList)))
print("ganze Zahlen", sum(x % 1 == 0 for x in myList))
print("reele Zahlen ohne ganze Zahlen", sum(x % 1 != 0 for x in myList))
