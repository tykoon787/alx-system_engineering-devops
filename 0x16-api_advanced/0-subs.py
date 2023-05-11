#!/usr/bin/python3
"""
Queries the Reddit API and returns number of
subscribers

Functions:
    number_of_subscribers(subreddit)
"""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If success
    if response.status_code == 200:
        data = response.json()
        return (data.get("data").get("subscribers"))
    else:
        pass
