#!/usr/bin/python3
"""Module for counting words in hot posts of a subreddit."""

import requests

def count_words(subreddit, word_list, word_count=None, after=None):
    """Recursively queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts of the subreddit."""

    if word_count is None:
        word_count = {}

    sub_info = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        params={"after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if sub_info.status_code != 200:
        return None

    info = sub_info.json()
    hot_l = [child.get("data").get("title") for child in info.get("data").get("children")]

    word_list = list(dict.fromkeys(word.lower() for word in word_list))

    for title in hot_l:
        split_words = title.split()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + sum(
                1 for s_word in split_words if s_word.lower() == word)

    after = info.get("data").get("after")
    if after is not None:
        return count_words(subreddit, word_list, word_count, after)

    if word_count:
        sorted_counts = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_counts:
            if v > 0:
                print('{}: {}'.format(k, v))

    return word_count
