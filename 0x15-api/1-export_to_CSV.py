#!/usr/bin/python3
"""Returns information from TODO list, filtered by employee ID."""
import csv
import requests
import sys


if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    ind_user = [i for i in user if i.get('id') == int(sys.argv[1])][0]
    tasks = [i for i in todos if i.get('userId') == int(sys.argv[1])]
    with open(sys.argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for task in tasks:
            writer.writerow([str(sys.argv[1]), ind_user.get('username'),
                             str(task.get('completed')), task.get('title')])
        f.close()
