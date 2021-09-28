#!/usr/bin/python3
"""This module pulls subscriber data from Reddit"""
import requests
import sys


def top_ten(subreddit):
    """gets the number of subscribers from a given subreddit."""
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=ua)
    data = res.json()
    i = 0
    try:
        if data is None:
            print('None')
        for item in data['data']['children']:
            if i < 10:
                print(item['data']['title'])
                i += 1
    except KeyError:
        return print('None')
