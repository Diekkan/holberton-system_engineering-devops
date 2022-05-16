#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests

if __name__ == "__main__":
    filename = "todo_all_employees.json"
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = todos.json()
    users = users.json()
    username = ''
    tasklist = []
    diction = {}
    eachtask = {}
    for user in users:
        userid = user.get('id')
        username = user.get('username')
        for task in todos:
            if task.get('userId') == userid:
                eachtask.update({'username': username})
                eachtask.update({'task': task.get('title')})
                eachtask.update({'completed': task.get('completed')})
                tasklist.append(eachtask.copy())
                print(eachtask)
        diction.update({"{}".format(userid): tasklist})

    with open(filename, 'w', newline='') as jsonfile:
        json.dump(diction, jsonfile)
