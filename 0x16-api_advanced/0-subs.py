#!/usr/bin/python3
"""
This module get the all subscribers on reddit
"""
import requests


def number_of_subscribers(subreddit):
    """This method get all the subreddit subcriber"""
    if subreddit is None:
        return 0

    get_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'NaziffAgent', 'from': 'bellnas09@gmail.com'}

    response = requests.get(get_url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
