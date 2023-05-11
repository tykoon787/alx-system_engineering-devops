#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit.

Functions:
    recurse(subreddit, hot_list=[])
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return List of all host articles"""

    # Variables
    headers = {'User-agent': 'my agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
        subreddit, after)
    posts = requests.get(url, headers=headers, allow_redirects=False)

    # if success
    if posts.status_code == 200:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        # Check for specific post
        for post in posts:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
