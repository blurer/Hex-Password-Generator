#!/usr/bin/env python3
import string
import random
import tweepy

CONSUMER_KEY = 'twitter api key'
CONSUMER_SECRET = 'twitter api key'
ACCESS_KEY = 'twitter api key'
ACCESS_SECRET = 'twitter api key'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

pwLength = 'password length'
pwQty = 'password quantity'

while True:
    for y in range(pwQty):
        password = ''
    for c in range(pwLength):
        password += random.choice(string.hexdigits)
    api.update_status(password)
    time.sleep(3600)