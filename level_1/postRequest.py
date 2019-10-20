#!/usr/bin/python3
def postRequest(session, url, payload):
    return session.post(url, data=payload)
