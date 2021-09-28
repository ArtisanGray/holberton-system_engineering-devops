#!/usr/bin/python3
"""This module pulls subscriber data from Reddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """gets the number of subscribers from a given subreddit."""
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=ua)
    data = res.json()
    try:
        if data is None:
            return (0)
        print(data['data']['subscribers'])
    except KeyError:
        return (0)
