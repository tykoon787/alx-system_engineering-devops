#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.

Functions:
    top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    """Get the 10 hot topics"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If success
    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
