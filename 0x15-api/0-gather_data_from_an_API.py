#!/usr/bin/python3
"""
Gather data from an API
"""
from sys import argv
import requests

try:
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    todos = todos.json()
    tasks = 0
    done = 0
    tasktitle = """"""
    for user in users:
        if user.get('id') == int(argv[1]):
            username = user.get('name')
            break
    for todo in todos:
        if todo.get('userId') == int(argv[1]):
            tasks += 1
            tasktitle += '\t' + todo.get('title') + " \n"
            if todo.get('completed') is True:
                done += 1
    txtformat = f"Employee {username} is done with tasks"
    txtformat += f"({done}/{tasks}):\n"
    txtformat += tasktitle
    print(txtformat)
except Exception:
    pass
