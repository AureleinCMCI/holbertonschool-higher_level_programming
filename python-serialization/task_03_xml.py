#!/usr/bin/python3
"""
Module to convert CSV data to JSON format using serialization.
"""

import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """
    Sérialise un dictionnaire en XML et l'écrit dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier où écrire le XML.

    Returns:
        None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename: str) -> dict:
    """
    Désérialise un fichier XML en dictionnaire.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for element in root:
        key = element.tag
        value = element.text
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        data[key] = value
    return data

