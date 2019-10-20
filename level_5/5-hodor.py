#!/usr/bin/python3
import requests
import sys

postRequest = __import__('postRequest').postRequest
getValue = __import__('getValue').getValue
getCurrentVotes = __import__('getCurrentVotes').getCurrentVotes
getRequest = __import__('getRequest').getRequest
getCaptcha = __import__('getCaptcha').getCaptcha


def main():
    """Main function"""

    id_number = 3
    required_votes = 400
    myUrl = 'http://158.69.76.135/level5.php'
    session = requests.Session()
    current_votes = 0
    count = 0
    errors = 0
    voted = 0

    while required_votes != current_votes:

        print("> Required: {} | Tries {} | Errors {} |\
 Voted --> {}".format(required_votes, count, errors,
                     voted), end="\r", flush=True)

        r = getRequest(session, myUrl)
        if r == 98:
            count += 1
            errors += 1
            continue

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
        myCaptcha = getCaptcha(session, 'http://158.69.76.135/tim.php')

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
        if p == 98:
            errors += 1
            count += 1
            continue

        if "hacker" in p.text:
            errors += 1
            count += 1
            continue

        if p.ok:  # ok catches all the status_code under 400 so return True
            count += 1
            voted += 1
            p.connection.close()
        else:
            print("POST Error: {}".format(p.status_code))
            sys.exit(98)
    print("\nDone. You have voted {} times for the id {}."
          .format(count + 1, id_number))

if __name__ == '__main__':
    main()
