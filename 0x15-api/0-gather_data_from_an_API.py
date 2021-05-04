#!/usr/bin/python3
"""Returns information from TODO list, filtered by employee ID."""
import requests
import sys


if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    ind_user = [i for i in user if i.get('id') == int(sys.argv[1])][0]
    tasks = [i for i in todos if i.get('userId') == int(sys.argv[1])]
    completed = [i for i in tasks if i.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        ind_user.get('name'), len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task.get('title')))
