#!/usr/bin/python3
"""Export data to CSV"""
import csv
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    user = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()
    json = []
    filename = f'{sys.argv[1]}.csv'
    for todo in todos:
        csv_format = {
            'userId': f"{todo['userId']}",
            'username': f"{user['username']}",
            'completed': f"{todo['completed']}",
            'title': f"{todo['title']}"
        }
        json.append(csv_format)
    with open(filename, 'w', newline="") as file:
        fieldnames = ['userId', 'username', 'completed', 'title']
        csvwriter = csv.DictWriter(file, fieldnames=fieldnames)
        csvwriter.writerows(json)
