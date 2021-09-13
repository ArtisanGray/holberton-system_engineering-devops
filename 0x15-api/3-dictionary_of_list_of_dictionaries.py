#!/usr/bin/python3
"""This module uses a GET request to pull JSON formatted data from an API."""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = 0
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    user_data = users.json()
    r = requests.get(url)
    data = r.json()
    t_list = []
    user_dict = {}
    user_name = ''
    for user in user_data:
        user_id = user['id']
        user_name = user['username']
        for item in data:
            if item['userId'] == user_id:
                format_dict = {"task": item['title'],
                               "completed": item['completed'],
                               "username": user_name}
                t_list.append(format_dict)

        user_dict['{}'.format(str(user_id))] = t_list
        t_list = []

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_dict, json_file)
