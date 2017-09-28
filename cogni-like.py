#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import sleep
import sys
import re
import tweepy


target = 'cognitiva_la'
num_tweets = 10
include_rts = True
min_likes = 10
wait = 10
patterns = (r'\.cl\b', r'chile')


if not os.path.isfile('auth.data'):
    sys.exit('auth.data file not found!')
with open('auth.data', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
auth_data = dict(l.split('=', 1) for l in lines)
req_keys = [
        'consumer_key', 'consumer_secret',
        'access_token', 'access_token_secret'
        ]
if not all(rk in auth_data.keys() for rk in req_keys):
    sys.exit(
            "auth.data necesita tener las variables '"
            "'consumer_key', 'consumer_secret', "
            "'access_token', 'access_token_secret'."
            )

consumer_key = auth_data['consumer_key']
consumer_secret = auth_data['consumer_secret']
access_token = auth_data['access_token']
access_token_secret = auth_data['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = api.user_timeline(
        screen_name=target,
        count=num_tweets,
        include_rts=include_rts
        )

for tweet in tweets:
    #print(tweet)
    #print()
    #print(dir(tweet))
    #print()
    print('text: ' + tweet.text)
    print('retweeted: ' + str(tweet.retweeted))
    print('retweet_count: ' + str(tweet.retweet_count))
    print('favorited: ' + str(tweet.favorited))
    print('favorite_count: ' + str(tweet.favorite_count))
    if not tweet.favorited:
        for pattern in patterns:
            if re.search(pattern, tweet.text, re.I|re.U):
                print('matched pattern!')
                if tweet.favorite_count >= min_likes:
                    tweet.favorite()
                    print('LIKED!!!')
                    break
    print()
    sleep(wait)
