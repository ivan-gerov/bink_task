import argparse
from datetime import date, datetime

from common.utils import parse_csv_to_dicts, sort_records


def task_1(records):
    """Print top five records by Current Rent"""
    sorted_records = sort_records(records, by="Current Rent")

    print("\nTop five records by Current Rent:\n")
    print([record["Current Rent"] for record in sorted_records[:5]])


def task_2(records):
    """Print all records with Lease Years == 25"""
    lease_25_years = [record for record in records if record["Lease Years"] == 25]

    print("\nAll records with Lease Years of 25:\n")
    for item in lease_25_years:
        print(item)

    print("\nTotal rent of all items in the list:\n")
    print(sum([item["Current Rent"] for item in lease_25_years]))


def task_3(records):
    """Print the count of all masts grouped by tenant"""
    mast_counts = dict()
    for record in records:
        tenant = record["Tenant Name"]
        mast_counts[tenant] = mast_counts.get(tenant, 0) + 1

    for tenant, no_of_masts in mast_counts.items():
        print(f"Tenant: {tenant} --- Number of masts: {no_of_masts}")


def task_4(records):
    """Print the data for rentals with “Lease Start Date”
    between 1st June 1999 and 31st August 2007."""
    result = []
    for record in records:
        if record["Lease Start Date"] < date(day=31, month=8, year=2007) and record[
            "Lease Start Date"
        ] > date(day=1, month=6, year=1999):

            # Format all date fields to the requested format (DD/MM/YYYY)
            for el in record:
                if isinstance(el, datetime):
                    record[el] = record[el].strftime("%d/%m/%Y")

            result.append(record)
    print(result)


def task_selector(task_id, data):
    """Runs any of the four tasks by task_id on the data provided"""
    tasks = {"1": task_1, "2": task_2, "3": task_3, "4": task_4}
    if task_id not in tasks.keys():
        raise ValueError("Please provide a valid task id")

    records = parse_csv_to_dicts(data)
    tasks[task_id](records)


if __name__ == "__main__":
    DATA = "data/Python Developer Test Dataset.csv"

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--task", required=True, help="Task id")
    ap.description = "Hi! You are required to provide an integer between 1-4 to run any of the four tasks! Thanks! :)"
    args = vars(ap.parse_args())
    task_selector(args["task"], data=DATA)
