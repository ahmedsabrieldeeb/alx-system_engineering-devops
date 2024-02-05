#!/usr/bin/python3
"""
This module retrieves and prints the completed tasks
and exports the data into JSON file
"""
import json
import requests
import sys


def get_todo_employee(employee_id):
    """
    Retrieves and prints the completed tasks of a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Construct the URL to retrieve the tasks of the employee
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    # Send a GET request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        # Print an error message if the request failed
        print("Error: status_code: {}".format(response.status_code))
        return
    else:
        # Parse the response as JSON
        data = response.json()
        # Retrieve the employee information
        username = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(employee_id)).json().get('username')
        # Create the file and filling it with the data
        file_name = "{}.json".format(employee_id)
        with open(file_name, 'w') as f:
            user_dict = {}
            user_dict[str(employee_id)] = []
            for task in data:
                user_records = {}
                user_records['task'] = task.get('title')
                user_records['completed'] = task.get('completed')
                user_records['username'] = username
                user_dict[str(employee_id)].append(user_records)
            json.dump(user_dict, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    else:
        employee_id = int(sys.argv[1])
        get_todo_employee(employee_id)
