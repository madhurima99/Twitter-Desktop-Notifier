import urllib.request
import urllib.parse
import urllib.error
import twurl
import ssl
import json


# https://apps.twitter.com/

def tweet():
    print('')
    #acct = input('Enter Twitter Account:')
    acct = "NASA"
    if (len(acct) >= 1):
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '2'})
        #print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        info = connection.read().decode()
        data = json.loads(info)
        print("----------------------")
        print("Tweet:", data[0]["text"])
        print("----------------------")
        headers = dict(connection.getheaders())
        # print headers
        print('Remaining', headers['x-rate-limit-remaining'])

        return acct, data[0]["text"]


TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
