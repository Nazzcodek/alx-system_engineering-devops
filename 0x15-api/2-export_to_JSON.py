#!/usr/bin/python3
"""
This module returns information about Employee TODO list progress.
using Employee ID
storing the data in a json file
"""
import json
import requests as r
import sys


def todo_tracker(e_id, filename):
    """
    Script to track user todo completed ratio
    Params:
        e_id: employee id
        filename: name of the JSON file to export data
    """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{e_id}"
    todos_url = f"{user_url}/todos"

    todos_data = r.get(todos_url).json()
    user_data = r.get(user_url).json()
    username = user_data.get("username")

    user_json_data = {
        f"{e_id}": [
            {"task": task['title'],
             "completed": task['completed'],
             "username": username
             }
            for task in todos_data
        ]
    }

    with open(filename, 'w') as f:
        json.dump(user_json_data, f)


if __name__ == "__main__":
    e_id = sys.argv[1]
    filename = f'{e_id}.json'
    todo_tracker(e_id, filename)
