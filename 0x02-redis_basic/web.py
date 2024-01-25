#!/usr/bin/env python3
"""uses the requests module to obtain the HTML content
of a particular URL and returns it."""


import requests
import redis


def get_page(url: str) -> str:
    """ tracks how many times a particular URL was accessed
    in the key "count:{url}" and cache the result
    with an expiration time of 10 seconds"""
    link = requests.get(url)
    connection = redis.Redis()
    connection.incr("count:{}".format(url))
    connection.setex("result:{}".format(url), 10, link.text)
    return link.text
