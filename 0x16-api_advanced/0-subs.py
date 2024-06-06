#!/usr/bin/python3
"""Module that queries the Reddit API and returns the number of subs"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subs for a given subreddit.

    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subs
    """
    base_url = 'https://www.reddit.com/r/'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        data = response.json().get('get',{})
        return data.get('subscribers',0)
    return 0
    except requests.RequestException:
        return 0

