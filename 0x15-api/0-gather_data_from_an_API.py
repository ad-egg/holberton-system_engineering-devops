#!/usr/bin/python3
"""
uses REST API to get information on an employee's TODO list progress
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = argv[1]

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    r_todos = requests.get(todos_url, params={'userId': employee_id})
    r_users = requests.get(users_url, params={'id': employee_id})

    total_tasks = r_todos.json()
    done_tasks = []
    for task in total_tasks:
        if task.get('completed') is True:
            done_tasks.append(task)

    user_info = r_users.json()
    employee_name = user_info[0].get('name')

    print("Employee {} is done with tasks({:d}/{:d}):".format(
                employee_name, len(done_tasks), len(total_tasks)))
    for task in done_tasks:
        print("\t{}".format(task.get('title')))
