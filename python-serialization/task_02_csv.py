#!/usr/bin/python3
"""
Module to convert CSV data to JSON format using serialization.
"""


import csv
import json


def convert_csv_to_json(csv_filename):

    """Converts a CSV file to a JSON file (data.json).

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """


    try:

        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except (OSError, IOError, csv.Error, json.JSONDecodeError) as e:
        print(f"Error during conversion: {e}")
        return False