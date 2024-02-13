#!/usr/bin/python3
"""This module queries the Reddit API and returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number
    of subscribers for a given subreddit

    Args:
        subreddit (str): The subreddit to query

    Returns:
        The number of subscribers for the given subreddit,
        0 for invalid subreddit

    """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
