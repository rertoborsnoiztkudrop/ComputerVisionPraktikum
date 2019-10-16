l = list(range(1,10))
x = int(input("Gib einen Index ein: "))

a = l[:x]
b = l[x:x+1]
c = l[x+1:]

a.reverse()
c = c[::-1]


print(a + b + c)