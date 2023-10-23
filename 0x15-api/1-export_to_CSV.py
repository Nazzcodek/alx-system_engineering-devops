#!/usr/bin/python3
"""
This module returns information about Employee TODO list progress.
using Employee ID
storing the data in a csv file
"""
import csv
import requests as r
import sys


def todo_tracker(e_id, filename):
    """
    Script to track user todo completed ratio
    Params:
        e_id: employee id
        filename: name of the CSV file to export data
    """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{e_id}"
    todos_url = f"{user_url}/todos"

    todos_data = r.get(todos_url).json()
    user_data = r.get(user_url).json()
    username = user_data.get("username")

    with open(filename, 'w', newline="") as f:
        csvwriter = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            task_title = todo['title']
            status = todo['completed']
            csvwriter.writerow([e_id, username, status, task_title])


if __name__ == "__main__":
    e_id = sys.argv[1]
    filename = f'{e_id}.csv'
    todo_tracker(e_id, filename)
