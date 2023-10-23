#!/usr/bin/python3
"""
This module returns information about all Employees TODO list progress.
storing the data in a json file
"""
import json
import requests as r
import sys


def todo_tracker(filename):
    """
    Script to track user todo completed ratio
    Params:
        filename: name of the JSON file to export data
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users_data = r.get(url).json()

    all_employees_data = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = f"{url}/{user_id}/todos"
        todos_data = r.get(todos_url).json()

        user_tasks = []
        for task in todos_data:
            title = task["title"]
            completed = task["completed"]
            user_tasks.append({"username": username,
                               "task": title,
                               "completed": completed
                               }
                              )

        all_employees_data[user_id] = user_tasks

    with open(filename, 'w') as f:
        json.dump(all_employees_data, f)


if __name__ == "__main__":
    filename = 'todo_all_employees.json'
    todo_tracker(filename)
