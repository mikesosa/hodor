#!/usr/bin/python3
import requests
import sys
postRequest = __import__('postRequest').postRequest
getValue = __import__('getValue').getValue
getCurrentVotes = __import__('getCurrentVotes').getCurrentVotes
getRequest = __import__('getRequest').getRequest


id_number = 833
required_votes = 4096
myUrl = 'http://158.69.76.135/level1.php'
current_votes = 0
n_votes = required_votes
session = requests.Session()

for count in range(n_votes):

    r = getRequest(session, myUrl)

    urlTextList = r.text.split()

    current_votes = getCurrentVotes(urlTextList, id_number)

    if current_votes is None:
        current_votes = 0
    elif current_votes >= required_votes:
        print("Contratulations id {} has {} votes!"
              .format(id_number, required_votes))
        sys.exit()

    n_votes = required_votes - current_votes

    my_key = getValue(urlTextList)

    payload = {
        'id': id_number,
        'holdthedoor': 'Submit',
        'key': my_key
    }

    p = postRequest(session, myUrl, payload)

    if p.ok:  # ok catches all the status_code under 400 so return True
        print("Required: {} | Voting--> {}\
              ".format(required_votes, count), end="\r")
        p.connection.close()
    else:
        print("POST Error: {}".format(p.status_code))
        sys.exit(98)

print("\nDone. You have voted {} times for the id {}."
      .format(count + 1, id_number))
