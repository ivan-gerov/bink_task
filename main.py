

import argparse

from common.utils import sort_records, parse_csv_to_dicts


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

def task_controller(task_id, data):
    """ Runs any of the four tasks """
    tasks = {"1": task_1,
             "2": task_2,}
            #  "3": task_3,
            #  "4": task_4}
    if task_id not in tasks.keys():
        raise ValueError("Please provide a valid task id")

    records = parse_csv_to_dicts(data)
    tasks[task_id](records)
    

if __name__ == "__main__":
    DATA = "data/Python Developer Test Dataset.csv"

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--task", required=True,
                    help="Task id")
    ap.description = "Hi! You are required to provide an integer between 1-4 to run any of the four tasks! Thanks! :)"
    args = vars(ap.parse_args())

    task_controller(args["task"], data=DATA)


    
