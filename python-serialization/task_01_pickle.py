#!/usr/bin/python3
"""Basic serialization module to save and load Python dictionaries as JSON."""

import json
import pickle


class CustomObject:
    def __init__(self, name, age, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'instance courante et la sauvegarde dans un fichier."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Charge une instance sérialisée depuis un fichier et la renvoie."""
        with open(filename, "rb") as file:
            return pickle.load(file)
