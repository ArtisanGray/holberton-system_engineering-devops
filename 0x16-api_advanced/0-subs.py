#!/usr/bin/python3
"""pulls subscriber data from a subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """uses a get request to pull data for the number of subs"""
    rq = requests.get('https://reddit.com/r/{}/about.json'.format(subreddit),
                      headers={'User-agent': 'ArtisanGray'})
    data = rq.json().get('data')
    if data is None:
        return (0)
    else:
        if data.get('subscribers') is None:
            return (0)
        else:
            return data.get('subscribers')
