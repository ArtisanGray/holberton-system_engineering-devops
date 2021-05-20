#!/usr/bin/python3
"""pulls post data from a subreddit."""
import requests
import sys


def top_ten(subreddit):
    """uses a get request to pull data for the number of subs"""
    rq = requests.get('https://reddit.com/r/{}/hot/.json?limit=10'
                      .format(subreddit),
                      headers={'User-agent': 'ArtisanGray'})
    data = rq.json().get('data')
    if data is None:
        print("None")
        return
    else:
        c = data.get('children')
        for posts in c:
            c_dict = posts['data']
            print(c_dict.get('title'))
