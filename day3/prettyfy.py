from xml.etree import ElementTree
from xml.dom import minidom

def pretty(element):
    xml_string = ElementTree.tostring(element,'utf-8')
    reparsed = minidom.parseString(xml_string)
    return reparsed.toprettyxml(indent = "  ")