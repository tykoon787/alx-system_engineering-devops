#!/usr/bin/python3
"""
Retrive Employee's TODO List from REST API

Functions:
    employee_tasks()
"""
import requests
from sys import argv


def employee_tasks():
    """
    This function outputs information about an employee's TODO List
    """
    employee_id = int(argv[1])
    if (len(argv) < 2):
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)
    else:
        # Users
        user_response = requests.get(
            "https://jsonplaceholder.typicode.com/users")
        users = user_response.json()

        # Tasks
        tasks_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos")
        tasks = tasks_response.json()

        for user in users:
            # Variables
            completed = 0
            incomplete = 0
            completed_tasks = []

            # get employee name
            id = user.get("id", 1001)
            if (employee_id == id):
                employee_name = user.get("name", "NO NAME")

                # Asses Tasks
                for task in tasks:
                    user_id = task.get("userId", 2002)
                    if (employee_id == user_id):
                        status = task.get("completed", False)
                        if status:
                            task_title = task.get("title", "NO VALID TITLE")
                            completed_tasks.append(task_title)
                            completed += 1
                        else:
                            incomplete += 1
                total = abs(completed + incomplete)
                print(
                    "Employee {} is done with tasks({}/{}):"
                    .format(employee_name, completed, total))
                for title in completed_tasks:
                    print("    {}".format(title))
                break
            else:
                continue


if __name__ == "__main__":
    employee_tasks()
