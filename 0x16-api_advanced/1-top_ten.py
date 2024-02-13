#!/usr/bin/python3
"""
    This module containes a function that queries the Reddit API
    and prints the top ten hot posts titles for a given subreddit
"""


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the top ten
    hot posts titles for a given subreddit

    Args:
        subreddit (str): The subreddit to query
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data').get('children')
    for post in data:
        print(post.get('data').get('title'))
