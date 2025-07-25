#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.
    Returns True if successful, False otherwise.
    """
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
