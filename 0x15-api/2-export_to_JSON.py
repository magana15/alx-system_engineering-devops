#!/usr/bin/python3
"""
This module retrieves and displays the TODO list progress for a given employee
using the JSONPlaceholder REST API and exports the data to a JSON file.
"""

import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee,
    and export the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')
    employee_username = user_data.get('username')

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")
        return

    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Write to JSON
    json_filename = f"{employee_id}.json"
    tasks_data = [
        {"task": task.get('title'), "completed": task.get('completed'), "username": employee_username}
        for task in todos_data
    ]
    json_data = {str(employee_id): tasks_data}
    with open(json_filename, mode='w') as file:
        json.dump(json_data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

