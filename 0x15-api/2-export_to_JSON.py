#!/usr/bin/python3
"""
uses REST API to get information on an employee's TODO list progress and
exports the data in JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_id = argv[1]

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    r_todos = requests.get(todos_url, params={'userId': employee_id})
    r_users = requests.get(users_url, params={'id': employee_id})

    total_tasks = r_todos.json()
    user_info = r_users.json()
    employee_name = user_info[0].get('username')
    list_dict = []
    user_tasks = {}

    with open("{}.json".format(employee_id), 'w') as json_file:
        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = employee_name
            list_dict.append(task_info)
        user_tasks[employee_id] = list_dict
        info = json.dumps(user_tasks)
        json_file.write(info)
