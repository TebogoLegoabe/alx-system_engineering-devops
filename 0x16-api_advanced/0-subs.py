#!/usr/bin/python3
#Get subs
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit"""
    head = {'User-Agent': 'Dan Kazam'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1])
