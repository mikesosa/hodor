#!/usr/bin/python3
import requests
import sys


def postRequest(session, url, payload, header, proxies):
    try:
        p = session.post(url, data=payload, headers=header,
                         proxies=proxies, timeout=3)
        return p
    except:
        return (98)
