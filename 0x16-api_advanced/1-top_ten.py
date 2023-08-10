#!/usr/bin/python3
"""Subreddit TOP 10 hot posts"""
import requests

def top_ten(subreddit):
    """
    subreddit top 10 post
    Parameters:
    subreddit (str): The name of the subreddit to fetch hot posts from.

    Returns:
    None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "YourUserAgentHere"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(title)
    else:
        print("None")
