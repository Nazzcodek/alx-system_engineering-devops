#!/usr/bin/python3
"""
This module returns information about Employee TODO list progress.
using Employee ID
"""
import requests as r
import sys


def todo_tracker(e_id):
    """
    Script to track user todo completed ratio
    Params:
        e_id: employee id
    """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{e_id}"
    todos_url = f"{user_url}/todos"

    todos_data = r.get(todos_url).json()
    total_todos = len(todos_data)

    user_data = r.get(user_url).json()
    name = user_data.get("name")

    completed = 0
    discription = []
    for todo in todos_data:
        if todo.get("completed"):
            completed += 1
            discription.append(todo['title'])
    print(f"Employee {name} is done with tasks({completed}/{total_todos}):")
    for i in discription:
        print(f"\t {i}")


if __name__ == "__main__":
    e_id = sys.argv[1]
    todo_tracker(e_id)
