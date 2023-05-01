#!/usr/bin/python3
"""
Exports data in csv format
"""

import csv
import requests
from sys import argv

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def employee_tasks_csv():
    """
    This function exports the data in csv format
    """
    users_response = requests.get(USERS_URL)
    users = users_response.json()

    tasks_response = requests.get(TODOS_URL)
    tasks = tasks_response.json()

    # Check args
    if (len(argv) < 2):
        print("Usage: {} <employee_id".format(argv[0]))
        exit(1)
    else:
        employee_id = int(argv[1])
        # Open file for writing
        with open("USER_ID.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for user in users:
                id = user.get("id", 1001)
                if (employee_id == id):
                    employee_username = user.get("username", "NO USERNAME")

                    for task in tasks:
                        user_id = task.get("userId", 2002)
                        if (employee_id == user_id):
                            status = task.get("completed", False)
                            task_title = task.get("title", "NO TITLE")
                            writer.writerow(
                                [employee_id,
                                 employee_username,
                                 status,
                                 task_title])
                        else:
                            continue
                else:
                    continue


if __name__ == "__main__":
    employee_tasks_csv()
