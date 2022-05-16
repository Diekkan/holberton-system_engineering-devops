#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys

if __name__ == "__main__":
    filename = f'{sys.argv[1]}.json'
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = todos.json()
    users = users.json()
    username = ''
    tasklist = []
    eachtask = {}
    for user in users:
        if user.get('id') == int(sys.argv[1]):
            username = user.get('username')
            break
        for task in todos:
            if task.get('userId') == int(sys.argv[1]):
                eachtask['task'] = task.get('title')
                eachtask['completed'] = task.get('completed')
                eachtask['username'] = username
                tasklist.append(eachtask)

#    with open(filename, 'w', newline='') as jsonfile:
        #json.dump()


