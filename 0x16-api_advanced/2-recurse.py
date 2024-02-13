#!/usr/bin/python3
""" This module contains a function that queries the Reddit API """


def recurse(subreddit, hot_list=[], after=None):
    """
    This function queries the Reddit API and returns a list

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): The list of hot post titles
        after (str): The 'after' parameter for pagination

    Returns:
        The list of hot post titles for the given subreddit,
        None if invalid subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Include 'after' parameter in the request if it's not None
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get("data", {}).get("children")

    for child in children:
        title = child.get("data", {}).get("title")
        hot_list.append(title)

    after = data.get("data", {}).get("after")

    if after:
        # Make a recursive call with the updated 'after' parameter
        return recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return hot_list
