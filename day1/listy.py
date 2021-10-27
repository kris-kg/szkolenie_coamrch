lista = ["Polak","Rosjanin","Niemiec"]
print(lista)
lista.append("Turek")
print(lista)
lista.sort()
#print(sorted(lista))
print(lista)
lista.reverse()
print(lista)

liczby = [2,56,112,99,-99,23345,12,1,112,0,112,0,-6,45]

liczby.sort()
print(liczby)
liczby.sort(reverse=True)
print(liczby)

liczby.remove(112)
print(liczby)
print(liczby[5])
print(liczby[2:6])
print(liczby[-1])

sklepzoo = [["pies","kot","papuga"],[5400,1200,6700]]

print(sklepzoo[0])
print(sklepzoo[0][1])
print(f"zwierzę: {sklepzoo[0][0]} kosztuje {sklepzoo[1][0]} zł")

nb = [1,5,2,4,2,3,2,4,2,4,1,1,1,3]

liczby = liczby + nb
print(liczby)

liczby.sort()
print(liczby)

liczby = liczby *4
print(liczby)
liczby.sort()
print(liczby)

litery = ['a','b','c','d','e','f','g','h']

litery[2:7] = [99,112,1005]
print(litery)
litery_m = litery
litery_p = list(litery)
print(f"litery przed: {litery}")
print(f"litery_m przed: {litery_m}")
print(f"litery_p przed: {litery_p}")
litery[:] = [1009,1001,1101,1110]
assert litery is litery_m

print(f"litery po: {litery}")
print(f"litery_m po: {litery_m}")
print(f"litery_p po: {litery_p}")

kolor = ['czerwony','niebieski','żółty','złoty','czarny','biały']
odds = kolor[::2]
evens = kolor[1::2]

print(odds)
print(evens)

w = "lajkonik"
print(w[:4])

s1 = "kajak"
s2 = "pomarańcza"

y1 = s1[::-1]
y2 = s2[::-1]

print(y1)
print(y2)