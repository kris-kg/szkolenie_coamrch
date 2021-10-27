#słownik - dictionary => (klucz,wartość)

auto = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1972
}

print(auto)

m = auto["rocznik"]
print(m)

m = auto.get("rocznik")
print(m)

auto["rocznik"] = 2018

print(auto)

print(auto.items())
print(auto.keys())
print(auto.values())
print("__________________________________")
for x in auto:
    print(x)

print("__________________________________")

for y in auto:
    print(auto[y])

print("__________________________________")

for x,y in auto.items():
    print(f"{x}:{y}")

print("__________________________________")

auta = {
    "auto1":{
        "marka": "Ford",
        "model": "Mustang",
        "rocznik": 1972
    },
    "auto2":{
        "marka": "Opel",
        "model": "Insignia",
        "rocznik": 2017
    },
    "auto3":{
        "marka": "Jeep",
        "model": "Cherokee",
        "rocznik": 2020
    }
}

print(auta)
print(auta["auto1"]["marka"])