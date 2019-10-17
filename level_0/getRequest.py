#!/usr/bin/python3
def getRequest(session, my_url):
    try:
        r = session.get(my_url, timeout=3)
        return r
    except requests.exceptions.RequestExeption as e:
        print("GET Error: {}".format(str(e)))
