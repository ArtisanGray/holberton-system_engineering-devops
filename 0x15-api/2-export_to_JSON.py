#!/usr/bin/python3
"""Returns information from TODO list, filtered by employee ID."""
import json
import requests
import sys


if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    ind_user = [i for i in user if i.get('id') == int(sys.argv[1])][0]
    tasks = [i for i in todos if i.get('userId') == int(sys.argv[1])]
    with open(sys.argv[1] + '.json', 'w', newline='') as f:
        expo = {sys.argv[1]: []}
        l = expo.get(sys.argv[1])
        for task in tasks:
            l.append({"task": task.get('title'), "completed": task.
                      get('completed'), "username": ind_user.get('username')})
        f.write(json.dumps(expo))
        f.close()
