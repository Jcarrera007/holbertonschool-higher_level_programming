#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to XML and saves it to a file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes XML from a file and returns a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        text = child.text
        if text is None or text == "None":
            result[child.tag] = None
        elif text == "True":
            result[child.tag] = True
        elif text == "False":
            result[child.tag] = False
        else:
            try:
                if "." in text:
                    result[child.tag] = float(text)
                else:
                    result[child.tag] = int(text)
            except ValueError:
                result[child.tag] = text
    return result
