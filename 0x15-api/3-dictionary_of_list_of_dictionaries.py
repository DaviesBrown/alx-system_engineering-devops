#!/usr/bin/python3
"""Export data to JSON dictionary of dictionary"""
import json
import requests

if __name__ == '__main__':
    users = requests.get(f'https://jsonplaceholder.typicode.com/users').json()
    json_dict = {}
    for user in users:
        user_id = user['id']
        todo_list = []
        todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos').json()
        for todo in todos:
            json_format = {
            'username': user['username'],
            'task': todo['title'],
            'completed': todo['completed']
            }
            todo_list.append(json_format)
        json_dict[user_id] = todo_list

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        jsonwriter = json.dump(json_dict, file)
