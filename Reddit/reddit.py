#!/usr/bin/env python3
"""
HW 3: Scripting - Reddit

Name: Jana Hayaly

PennKey: jhayaly

Number of hours spent on homework: 4

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.

This assignment template was adapted from Peter Bui's Python scripting
assignment (c) 2020: https://gitlab.com/nd-cse-20289-sp20/cse-20289-sp20-assignments/
which is licensed under the MIT license agreement.
"""

import argparse # for parsing arguments
import json # for formatting and printing json
import requests # for making HTTP requests

def build_parser():
    """
    Builds an ArgumentParser with the specified parameters.

    Args:
        None

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Pulls top posts from subreddit and displays them in terminal")
    parser.add_argument('url', help="the URL or subreddit to visit")

    # TODO implement the -n, -o, and -t flags
    parser.add_argument('-n', metavar= 'N', default= 10, help= 'number of posts to display (default: 10)')
    parser.add_argument('-o', choices= {'score','title'}, default= 'score', help='field to sort posts by (default: score)')
    parser.add_argument('-t', metavar='T', default = 60, help='truncate title to specified length (default: 60)')

    return parser


def load_reddit_data(url):
    """
    Load reddit data from the specified url into a list of dicts.

    You'll need to verify the url parameter. If it starts with http, then
    use it, otherwise assume it is a subreddit.

    Make sure to use the headers specified in the homework description when
    making your get requests!

    After correctly retrieving the response JSON dict from reddit, you'll want
    the list of posts. It's up to you how you'd like to return the list of
    dict, so you need to think carefully about what portion of the JSON you
    need in order to implement format_reddit_data() and print_reddit_data().

    Hint: Use json.dumps(response.json(), indent=4) to print the response
    into a more readable format.

    We don't require any error handling for non-existent subreddits or malformed
    URLs, but you are welcome to optionally do so.

    Args:
        url (str): the url (or subreddit)

    Returns:
        list: a list of dicts containing post information for the subreddit.
    """
    if 'http' not in url:
        url = "https://www.reddit.com/r/" + url + ".json"
    final_list = []
    headers = {
        "user-agent": "CIS 1920 Spring 2023 HW3 by jhayaly@sas.upenn.edu"
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    data = response_json['data']
    children = data['children']
    for subpost in children:
        post_data = subpost['data']
        title = post_data['title']
        score = post_data['score']
        url = post_data['url']
        mapping = {'score': score, 'title': title, 'url': url}
        final_list.append(mapping)
    return final_list


def format_reddit_data(data, limit=10, order_by="score", title_len=60):
    """
    Sorts and formats the given reddit data. If ordered by "score",
    make sure to sort in descending order, otherwise sort in ascending order.

    Hint: use an anonymous function to provide a key to list.sort()

    Args:
        data (list): a list of dicts containing the raw reddit post data from
            load_reddit_data
        limit (int): the number of posts to return, default 10
        order_by (str): the attribute in the raw reddit post data to sort by,
            default "score"
        title_len (int): the length of the title to show, default 60

    Returns:
        list: a list of dicts with with the following attributes in each dict:
            title (str): the possibly shortened post title
            score (str): the score of the post
            url (str): the url to the post
    """

    if order_by == "title":
        data.sort(key = lambda elt: elt['title'], reverse = False)
    else:
        data.sort(key = lambda elt: elt['score'], reverse = True)

    for elt in data:
        elt['title'] = elt['title'][0:int(title_len)]
    
    print(data[: int(limit)])
    return data[: int(limit)]


def print_reddit_data(formatted_data):
    """
    Print reddit data based on specified attributes using the following format:

      print("{index}.\t{title} (Score: {score})\n\t{url}".format(...))

    Note: you don't have to write unit tests for this function, and it will be
    ignored by the code coverage checker. We will be checking the output of
    your script against the solution however, so please follow the print format
    given above exactly!

    Args:
        formatted_data (list): a formatted list of posts returned from
            format_reddit_data()

    Returns:
        None
    """
    idx = 0
    for elt in formatted_data:
        print("{index}.\t{title} (score: {score})\n\t{url}".format(index = idx, 
        title=elt['title'], score=elt['score'], url=elt['url']))
        idx += 1


def main():
    """
    Builds an ArgumentParser object by calling build_parser(),
    loads the data from the given URL by calling load_reddit_data(),
    and then prints the data using print_reddit_data().
    """
    parser = build_parser()
    # Parse command line arguments
    args = parser.parse_args()

    url = args.url
    limit     = args.n
    orderby   = args.o
    titlelen  = args.t

    # Load data from url and then print the data
    data = load_reddit_data(url)
    formatted_data = format_reddit_data(data, limit, orderby, titlelen)
    print_reddit_data(formatted_data)


if __name__ == '__main__':
    """
    example code for getting headers, also in the hw description
    headers = {
    "user-agent": "CIS 1920 Spring 2023 HW3 by [insert your email here]"
    }
    response = requests.get("https://www.reddit.com/r/python/.json", headers=headers)
    print(json.dumps(response.json(), indent=4))
    """
    main()