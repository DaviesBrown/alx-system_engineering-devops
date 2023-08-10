#!/usr/bin/python3
"""Number of subreddit total subscribers"""
import requests

def number_of_subscribers(subreddit):
    """
    number of subredit subscribers
    Parameters:
    subreddit (str): The name of the subreddit to fetch number of post.
    
    Returns:
    Number of subscriber"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
