#!/usr/lib/python3
def getValue(ls):
    for i in ls:
        if i.startswith('value'):
            value = i[7:-1]
    return value
