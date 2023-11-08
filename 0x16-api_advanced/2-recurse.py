#!/usr/bin/python3
"""
This module recursively get hot-list of post
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This is a recursive method"""
    get_url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'NaziffAgent', 'from': 'bellnas09@gmail.com'}
    params = {'after': after}

    response = requests.get(get_url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        posts = data.get('data', {}).get('children', None)
        for post in posts:
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
