#!/usr/bin/python3
import requests
import sys

postRequest = __import__('postRequest').postRequest
getValue = __import__('getValue').getValue
getCurrentVotes = __import__('getCurrentVotes').getCurrentVotes
getRequest = __import__('getRequest').getRequest
getProxies = __import__('getProxies').getProxies


def main():
    """Main function"""

    id_number = 8
    required_votes = 98
    myUrl = 'http://158.69.76.135/level4.php'
    session = requests.Session()
    current_votes = 0
    n_votes = required_votes
    count = 0
    badProxyErrors = 0
    alreadyUsedErrors = 0
    voted = 0

    proxiesList = getProxies(session)

    while required_votes != current_votes:

        print("> Required: {} | Tries {} | Bad Proxy {} | Proxy Already\
 used {} | Voted --> {}".format(required_votes, count, badProxyErrors,
                                alreadyUsedErrors, voted), end="\r",
              flush=True)
        proxies = {
            "https": proxiesList[count],
            "http": proxiesList[count]
        }

        r = getRequest(session, myUrl, proxies)
        if r == 98:
            count += 1
            badProxyErrors += 1
            continue

        myReferer = r.url

        urlTextList = r.text.split()

        current_votes = getCurrentVotes(urlTextList, id_number)

        if current_votes is None:
            current_votes = 0
        elif current_votes >= required_votes:
            print("\nContratulations id {} has {} votes!"
                  .format(id_number, required_votes))
            sys.exit()

        n_votes = required_votes - current_votes

        my_key = getValue(urlTextList)

        payload = {
            'id': id_number,
            'holdthedoor': 'Submit',
            'key': my_key
        }

        myHeader = {
            'Referer': myReferer
        }

        p = postRequest(session, myUrl, payload, myHeader, proxies)
        if p == 98:
            badProxyErrors += 1
            count += 1
            continue

        if "hacker" in p.text:
            badProxyErrors += 1
            count += 1
            continue

        if "already" in p.text:
            alreadyUsedErrors += 1
            count += 1
            continue

        if p.ok:  # ok catches all the status_code under 400 so return True
            count += 1
            voted += 1
            p.connection.close()
        else:
            print("POST Error: {}".format(p.status_code))
            sys.exit(98)

    print("\nDone. You have voted {} times\
 for the id {}.".format(count + 1, id_number))

if __name__ == '__main__':
    main()
