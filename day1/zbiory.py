drzewa = {"buk","dąb","jesion","baobab","jabłoń","jabłoń"}
print(drzewa)
print(drzewa)
print(drzewa)
for d in drzewa:
    print(d)

print("jesion" in drzewa)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

drzewa.add("osika")
print(drzewa)

drzewa.update(["wierzba","topola","śliwa"])

print(drzewa)
drzewa.remove("osika")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("jesion")
print(drzewa)

drzewa_m = drzewa.pop()
print(drzewa_m)

print(drzewa)