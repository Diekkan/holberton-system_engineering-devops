#!/usr/bin/python3
"""Gather data from an API and save it to CSV file"""
import csv
import sys
import requests

if __name__ == "__main__":
    filename = f'{sys.argv[1]}.csv'
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = todos.json()
    users = users.json()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for user in users:
            if user.get('id') == int(sys.argv[1]):
                username = user.get('username')
                break
        for task in todos:
            if task.get('userId') == int(sys.argv[1]):
                writer.writerow([int(sys.argv[1]), username,
                                task.get('completed'), task.get('title')])
