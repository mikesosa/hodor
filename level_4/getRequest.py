#!/usr/bin/python3
import requests


def getRequest(session, my_url, proxies):

    try:
        r = session.get(my_url, proxies=proxies, timeout=3)
        return r
    except requests.exceptions.RequestException as e:
        # print("GET Error: {}".format(str(e)))
        return (98)
