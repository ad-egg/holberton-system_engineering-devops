#!/usr/bin/python3
"""
this module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns a list that
    contains the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-agent': 'ad-egg'}
    r = requests.get(url, headers=h, allow_redirects=False)

    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        children = data.get('children')
        for post in children:
            post_data = post.get('data')
            title = post_data.get('title')
            hot_list.append(title)
        return hot_list
    else:
        return None
