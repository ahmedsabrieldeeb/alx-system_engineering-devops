#!/usr/bin/python3
"""
This module retrieves and prints the completed tasks
and exports the data into JSON file
"""
import json
import requests
import sys


def get_todo_all_employees():
    """
    Retrieves and prints the completed tasks of all employees.

    Returns:
        None
    """
    # Construct the URL to retrieve the tasks of all employees
    url = f'https://jsonplaceholder.typicode.com/todos'
    # Send a GET request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        # Print an error message if the request failed
        print("Error: status_code: {}".format(response.status_code))
        return
    else:
        # Create the file and filling it with the data
        file_name = "todo_all_employees.json"
        # The main dictonary
        tasks_dict = {}
        with open(file_name, 'w') as f:
            # Parse the response as JSON
            data = response.json()
            for task in data:
                # Extract the user ID from the task
                employee_id = task.get('userId')
                # Retrieve the employee information
                user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
                    .format(employee_id)
                username = requests.get(user_url)
                username = username.json().get('username')
                # Add the user to the dictionary if it doesn't exist
                if str(employee_id) not in tasks_dict:
                    tasks_dict[str(employee_id)] = []
                # Add the task to the user
                tasks_dict[str(employee_id)].append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })
            # Write the dictionary to the file
            json.dump(tasks_dict, f)


if __name__ == "__main__":
    get_todo_all_employees()
