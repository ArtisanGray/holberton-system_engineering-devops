#!/usr/bin/python3
"""This module uses a GET request to pull JSON formatted data from an API."""
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = sys.argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    user_data = users.json()
    t_list = []
    user_name = ''
    completed = 0
    count_t = 0
    for user in user_data:
        if int(user_id) == user['id']:
            user_name = user['name']
    users.close()
    r = requests.get(url)
    data = r.json()
    for item in data:
        if item['userId'] == int(user_id):
            count_t += 1
            if item['completed']:
                completed += 1
                t_list.append(item['title'])
    print("Employee {} is done with tasks({}/{}):".format(
                            user_name, completed, count_t))
    for title in t_list:
        print("\t {}".format(title))
