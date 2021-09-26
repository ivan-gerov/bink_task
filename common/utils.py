import csv
import datetime
import os


def parse_csv_to_dicts(csv_filepath):
    """Parses csv file to a list of dicts"""
    if not os.path.exists(csv_filepath):
        raise FileNotFoundError

    with open(csv_filepath) as f:
        data = csv.reader(f, delimiter=",")
        header = next(data)
        records = [record for record in data]

    list_of_dicts = []
    for record in records:
        processed_record = {}
        for column, record_element in zip(header, record):

            # Get the proper datatypes
            if column == "Current Rent":
                record_element = float(record_element)
            if column == "Lease Years":
                record_element = int(record_element)
            if "Date" in column:
                record_element = datetime.datetime.strptime(
                    record_element, "%d %b %Y"
                ).date()

            processed_record[column] = record_element
        list_of_dicts.append(processed_record)
    return list_of_dicts


def sort_records(records, by, ascending=True):
    """Sorts a records list inplace by a given field
    and direction (ascending/descending)"""

    def sort_logic(record):
        """Function that passes the sort logic.
        Currently only intended for the "Current Rent" field."""
        return float(record[by])

    sorted_records = sorted(records, key=sort_logic, reverse=not ascending)
    return sorted_records
