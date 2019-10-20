#!/usr/bin/python3
def postRequest(session, url, payload, header):
    return session.post(url, data=payload, headers=header)
