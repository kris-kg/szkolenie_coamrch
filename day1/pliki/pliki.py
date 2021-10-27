import os

f = open("dane.txt","r")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()
print("********************************")
f = open("dane.txt","r")
print(f.read())
f.close()

print("********************************")
f = open("dane.txt","r")
for x in f:
    print(x)

print("********************************")
f = open("wdane.txt","a",encoding='utf-8')
f.write("to jest ważna informacja \n")
f.close()

print("********************************")
f = open("wdane.txt","r",encoding='utf-8')
print(f.read())
f.close()

if os.path.exists("wdane.txt"):
    os.remove("wdane.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje")

