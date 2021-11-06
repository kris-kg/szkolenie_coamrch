import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)
    print(root[0][2])

except:
    print("element nie istnieje!")