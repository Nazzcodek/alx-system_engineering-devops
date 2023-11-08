#!/usr/bin/python3
"""
This module get the all subscribers on reddit
"""
import requests


def top_ten(subreddit):
    """This method get the title of top ten post"""
    if subreddit is None:
        return 0

    get_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'NaziffAgent', 'from': 'bellnas09@gmail.com'}
    params = {'limit': 10}

    response = requests.get(get_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        top_posts = data.get('data', {}).get('children', None)

        for post in top_posts:
            title = post.get('data', {}).get('title', '')
            print(title)
    else:
        print(None)
