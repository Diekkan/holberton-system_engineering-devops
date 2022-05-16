#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys

if __name__ == "__main__":
    filename = "{}.json".format(sys.argv[1])
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = todos.json()
    users = users.json()
    username = ''
    tasklist = []
    diction = {}
    eachtask = {}
    for user in users:
        if user.get('id') == int(sys.argv[1]):
            username = user.get('username')
            break
    for task in todos:
        if task.get('userId') == int(sys.argv[1]):
            eachtask.update({'task': task.get('title')})
            eachtask.update({'completed': task.get('completed')})
            eachtask.update({'username': username})
            tasklist.append(eachtask.copy())
    diction["{}".format(sys.argv[1])] = tasklist
    with open(filename, 'w', newline='') as jsonfile:
        json.dump(diction, jsonfile)
