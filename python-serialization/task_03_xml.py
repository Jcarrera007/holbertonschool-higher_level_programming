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
        # Try to convert to int or float, else leave as string
        if text is not None:
            if text.isdigit():
                result[child.tag] = int(text)
            else:
                try:
                    result[child.tag] = float(text)
                except ValueError:
                    if text.lower() == "true":
                        result[child.tag] = True
                    elif text.lower() == "false":
                        result[child.tag] = False
                    else:
                        result[child.tag] = text
        else:
            result[child.tag] = None
    return result
