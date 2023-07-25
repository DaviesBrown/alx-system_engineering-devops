#!/usr/bin/python3
"""Export data to JSON"""
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()
    json_list = []
    for todo in todos:
        json_format = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user['username']
        }
        json_list.append(json_format)
    json_list = {id: json_list}

    filename = f'{id}.json'
    with open(filename, 'w') as file:
        jsonwriter = json.dump(json_list, file)
