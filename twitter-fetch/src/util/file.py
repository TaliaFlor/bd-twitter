import csv
import json
from collections import Iterable


def read_file(filename):
    """Reads and returns a JSON file"""
    json_data = open(filename, encoding="utf-8")
    data = json.load(json_data)
    return data


def write_file(filename, data: Iterable, header: Iterable = None):
    """Writes a CSV file"""
    with open(filename, 'w+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(data)
