#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == "__main__":
    try:
        todos = requests.get('https://jsonplaceholder.typicode.com/todos')
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        users = users.json()
        todos = todos.json()
        tasks = 0
        done = 0
        tasktitle = """"""
        for user in users:
            if user.get('id') == int(sys.argv[1]):
                username = user.get('name')
                break
        for todo in todos:
            if todo.get('userId') == int(sys.argv[1]):
                tasks += 1
                if todo.get('completed') is True:
                    done += 1
                    tasktitle += '\t ' + todo.get('title') + "\n"
        txtformat = f"Employee {username} is done with tasks"
        txtformat += f"({done}/{tasks}):\n"
        txtformat += tasktitle
        sys.stdout.write(txtformat)
    except Exception:
        pass
