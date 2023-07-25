#!/usr/bin/python3
"""gather data from an API"""
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    user = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user = user.json()
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    todos = todos.json()
    count = 0
    title = []
    for i in todos:
        if i['completed'] is True:
            count += 1
            title.append(i['title'])

    print(f"Employee {user['name']} is done with tasks({count}/{len(todos)}):")
    for i in title:
        print(f"\t {i}")
