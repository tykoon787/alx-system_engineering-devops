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
    users_response = requests.get(USERS_URL)
    users = users_response.json()

    tasks_response = requests.get(TODOS_URL)
    tasks = tasks_response.json()

    # {USER_ID: [{DETAILS}]}
    records = {}
    for user in users:
        employee_id = user.get("id", 1001)
        employee_username = user.get("username", "NO USERNAME")
        # Generate task list for each employee
        tasks_list = []
        for task in tasks:
            user_id = task.get("userId", 2002)
            if (employee_id == user_id):
                status = task.get("completed", None)
                task_title = task.get("title", "NO TITLE")
                tasks_dict = {}
                tasks_dict["username"] = employee_username
                tasks_dict["task"] = task_title
                tasks_dict["completed"] = status
                tasks_list.append(tasks_dict)
        records[employee_id] = tasks_list
        with open("todo_all_employees.json", "w") as f:
            json.dump(records, f)


if __name__ == "__main__":
    export_json()
