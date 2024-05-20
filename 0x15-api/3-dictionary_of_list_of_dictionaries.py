#!/usr/bin/python3
"""
This module retrieves and exports the TODO list progress for all employees
using the JSONPlaceholder REST API and exports the data to a JSON file.
"""

import json
import requests

def fetch_all_employees_todo_progress():
    """
    Fetch and export the TODO list progress for all employees
    to a JSON file.

    The JSON file is named 'todo_all_employees.json' and contains
    the TODO list data for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    # Fetch all users
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error: Unable to fetch users data")
        return

    users_data = users_response.json()

    # Fetch all todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch todos data")
        return

    todos_data = todos_response.json()

    # Construct the JSON data
    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = [task for task in todos_data if task.get('userId') == user_id]
        all_tasks[user_id] = [
            {"username": username, "task": task.get('title'), "completed": task.get('completed')}
            for task in user_tasks
        ]

    # Write to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)

if __name__ == "__main__":
    fetch_all_employees_todo_progress()

