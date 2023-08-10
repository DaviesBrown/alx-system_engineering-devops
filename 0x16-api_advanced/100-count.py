#!/usr/bin/python3
"""count number of words that are in word list"""
import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively counts occurrences of specified keywords in the titles of hot posts from a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to fetch hot posts from.
    word_list (list): A list of keywords to count occurrences of in the titles.
    after (str, optional): The post ID to start fetching from in the next page. Default is None.
    word_counts (dict, optional): A dictionary to store the counts of keywords. Default is None.

    Returns:
    None"""
    if not subreddit or not word_list:
        return
    
    # Initialize word_counts dictionary if not provided
    if word_counts is None:
        word_counts = {}
    
    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        "User-Agent": "YourUserAgentHere"
    }
    
    # Parameters for pagination
    params = {
        "limit": 100,  # Number of posts per request
        "after": after  # After which post to continue fetching
    }
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        # Process titles and update word counts
        for post in posts:
            title = post["data"]["title"]
            lowercase_title = title.lower()
            
            # Iterate through the word list and update word counts
            for word in word_list:
                lowercase_word = word.lower()
                if f" {lowercase_word} " in f" {lowercase_title} ":
                    word_counts[lowercase_word] = word_counts.get(lowercase_word, 0) + 1
        
        # Recursive call with the next page's "after" parameter
        if data["data"]["after"]:
            count_words(subreddit, word_list, after=data["data"]["after"], word_counts=word_counts)
        else:
            # Print sorted word counts
            sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return
