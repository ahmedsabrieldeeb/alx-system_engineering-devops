#!/usr/bin/python3
""" This module contains a function that queries the Reddit API """


def count_words(subreddit, word_list, after=None, count_dict={}):
    """
    This function queries the Reddit API, parses the titles of all
    hot articles, and prints a sorted count of given keywords

    Args:
        subreddit (str): The subreddit to query
        word_list (list): The list of words to count
        after (str): The 'after' parameter for pagination
        count_dict (dict): The dictionary of word counts
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                if word in count_dict:
                    count_dict[word] += count
                else:
                    count_dict[word] = count

    after = data['data']['after']

    if after is None:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))
    else:
        count_words(subreddit, word_list, after, count_dict)


count_words('programming', ['react', 'python', 'java', 'javascript', 'scala'])
