#!/usr/bin/python3
"""This module uses a GET request to pull JSON formatted data from an API."""
import csv
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = sys.argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    user_data = users.json()
    t_list = []
    user_name = ''
    for user in user_data:
        if int(user_id) == user['id']:
            user_name = user['username']
    users.close()
    r = requests.get(url)
    data = r.json()
    for item in data:
        if item['userId'] == int(user_id):
            format_str = [int(user_id), user_name,
                          str(item['completed']), item['title']]
            t_list.append(format_str)

    with open('{}.csv'.format(int(user_id)), mode='w') as user_file:
        user_writer = csv.writer(user_file, delimiter=',',
                                 quotechar='"', quoting=csv.QUOTE_ALL)
        for task in t_list:
            user_writer.writerow(task)
