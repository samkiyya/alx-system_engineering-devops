# 0x16. API advanced

## Description

This project focuses on making recursive requests to an API, how to use an API with pagination and how to read API documentation to find the endpoints we’re looking for.

## Table of contents

| Files                                                             | Description                                                                                                                                                                       |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [0-subs.py](./0-subs.py) <br />[0-main.py](./0-main.py)           | Python function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit                                     |
| [1-top_ten.py](./1-top_ten.py)<br />[1-main.py](./1-main.py)      | Python function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit                                                          |
| [2-recurse.py](./2-recurse.py) <br />[2-main.py](./2-main.py)     | Python recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit                                          |
| [100-count.py](./100-count.py) <br />[100-main.py](./100-main.py) | Python recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces.) |
