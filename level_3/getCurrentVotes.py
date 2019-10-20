#!/usr/lib/python3
def getCurrentVotes(ls, id_number):
    votes = 0
    for j in range(len(ls)):
        if ls[j] == str(id_number):
            if ((ls[j + 3]).isdigit()):
                votes = int(ls[j + 3])
                return votes
