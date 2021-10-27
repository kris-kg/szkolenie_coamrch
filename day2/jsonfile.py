import json

x = '{"name":"Jan","age":31,"city":"Kraków"}'

print(x)

y = json.loads(x)
print(y)
print(y["city"])

auto = {
    "marka":"Opel",
    "model":"Insignia",
    "rok":2019
}
jsonauto = json.dumps(auto, indent=4)
print(jsonauto)

with open("auto.json","w") as outf:
    outf.write(jsonauto)

with open("auto.json","r") as outf:
    auto_dict = json.load(outf)

print(auto_dict)
print(auto_dict["marka"])
print(type(auto_dict))

print("**************************************************")

info ='{"organizacja":"Fundacja BIOTECH",' \
      '"miasto":"Krosno","kraj":"Polska"}'

extra = {
    "id":53454,
    "zakres":"sztuczna inteligencja"
}

z = json.loads(info)
z.update(extra)
info_new = json.dumps(z)
print(info_new)
