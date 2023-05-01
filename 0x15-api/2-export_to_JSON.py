#!/usr/bin/python3
"""
Exports records of all tasks in json format
"""

import json
import requests
from sys import argv

USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def export_json():
    """
    This functions exports the data to a file in json format
    """
    if (len(argv) < 2):
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)
    else:
        users_response = requests.get(USERS_URL)
        users = users_response.json()

        tasks_response = requests.get(TODOS_URL)
        tasks = tasks_response.json()

        employee_id = int(argv[1])
        # {USER_ID: [{DETAILS}]}
        records = {}
        for user in users:
            id = user.get("id", 1001)
            if (employee_id == id):
                employee_username = user.get("username", "NO USERNAME")
                # Generate task list for each employee
                tasks_list = []
                for task in tasks:
                    user_id = task.get("userId", 2002)
                    if (employee_id == user_id):
                        status = task.get("completed", None)
                        task_title = task.get("title", "NO TITLE")
                        tasks_dict = {}
                        tasks_dict["task"] = task_title
                        tasks_dict["completed"] = status
                        tasks_dict["username"] = employee_username
                        tasks_list.append(tasks_dict)
                    else:
                        continue
                records[employee_id] = tasks_list
                with open("{}.json".format(employee_id), "w") as f:
                    json.dump(records, f)
            else:
                continue


if __name__ == "__main__":
    export_json()
