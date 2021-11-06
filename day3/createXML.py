from xml.etree.ElementTree import Element,SubElement,Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty

top =  Element("autokomis")
auto = SubElement(top,"samochod")

id = SubElement(auto,"id")
id.text = "sam1"

marka = SubElement(auto,"marka")
marka.text = "Subaru"

model = SubElement(auto,"model")
model.text = "Impreza"

poj = SubElement(auto,"pojemnosc")
poj.text = "2.0"

wyp_dod = SubElement(auto,"wyposazenie_dod")

kolor = SubElement(wyp_dod,"kolor")
kolor.text = "czarna perła"

tap = SubElement(wyp_dod,"tapicerka")
tap.text = "biała skóra"

#drugie auto

auto = SubElement(top,"samochod")

id = SubElement(auto,"id")
id.text = "sam2"

marka = SubElement(auto,"marka")
marka.text = "Subaru"

model = SubElement(auto,"model")
model.text = "Outback"

poj = SubElement(auto,"pojemnosc")
poj.text = "2.2"

wyp_dod = SubElement(auto,"wyposazenie_dod")

kolor = SubElement(wyp_dod,"kolor")
kolor.text = "czerwony metallic"

klima = SubElement(wyp_dod,"klimatyzacja")
klima.text = "GR33554"

print(pretty(top))

zapis = open("subarukomis.xml","w",encoding='utf-8')
zapis.write(pretty(top))
zapis.close()