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
        # Preserve values as strings; XML elements do not retain Python types.
        # If an element has no text, store None to reflect empty nodes.
        text = child.text
        if text is None:
            result[child.tag] = None
        else:
            result[child.tag] = text
    return result
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml


def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}\n")

    deserialized_data = deserialize_from_xml(xml_file)
    print("Deserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
