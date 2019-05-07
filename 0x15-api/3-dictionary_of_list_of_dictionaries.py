#!/usr/bin/python3
"""
uses REST API to get information on all employees' TODO list progress and
exports the data in JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    employee_id = 1

    all_users = requests.get(users_url).json()

    user_tasks = {}

    for employee_id in range(1, len(all_users) + 1):
        r_todos = requests.get(todos_url, params={'userId': employee_id})
        r_users = requests.get(users_url, params={'id': employee_id})

        total_tasks = r_todos.json()
        user_info = r_users.json()
        list_dict = []
        employee_name = user_info[0].get('username')

        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = employee_name
            list_dict.append(task_info)
        user_tasks[employee_id] = list_dict

    with open("todo_all_employees.json", 'w') as json_file:
        info = json.dumps(user_tasks)
        json_file.write(info)
