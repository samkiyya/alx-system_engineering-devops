#!/usr/bin/python3
"""Module for counting words in hot posts of a subreddit."""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts of the subreddit."""
    
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        return None

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0)
            word_count[word_lower] += title.split().count(word_lower)

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, word_count, after)
    
    if word_count:
        sorted_words = sorted(word_count.items(), key=lambda kv: ( - kv[1], kv[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")

    return word_count
