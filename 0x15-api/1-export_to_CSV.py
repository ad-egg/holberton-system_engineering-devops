#!/usr/bin/python3
"""
uses REST API to get information on an employee's TODO list progress and
exports the information in CSV format
"""

if __name__ == "__main__":
    import csv
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

    with open("{}.csv".format(employee_id), mode='w') as csv_file:
        writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in total_tasks:
            writer.writerow(["{}".format(employee_id), "{}".format(
                        employee_name), "{}".format(task.get(
                                'completed')), "{}".format(task.get('title'))])
