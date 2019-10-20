#!/usr/bin/python3
import requests
import sys


def getProxies(session):
    proxiesList = []
    try:
        r = session.get('http://spys.me/proxy.txt', timeout=3)
        ls = r.text.split()

        for i in range(len(ls)):
            if ":" in ls[i] and i > 25:  # skiping unesesary text
                proxiesList.append(ls[i])
        return proxiesList
    except requests.exceptions.RequestException as e:
        print("Get Proxies Error: {}".format(str(e)))
        sys.exit(98)
