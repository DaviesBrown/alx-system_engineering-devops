#!/usr/bin/python3
"""get title of hot of all in a subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively return the titles of hot posts from a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to fetch hot posts from.
    hot_list (list): A list of all occurrences of the titles.
    after (str, optional): The post ID to start fetching from in the next page. Default is None.
    
    Returns:
    None
    """
    if not subreddit:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "YourUserAgentHere"
    }
    params = {
        "limit": 100,  # Number of posts per request
        "after": after  # After which post to continue fetching
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)
        print(hot_list)
        if data["data"]["after"]:
            recurse(subreddit, hot_list, after=data["data"]["after"])
        return hot_list
    else:
        return None
