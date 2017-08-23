#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = 'cognitiva_la', count = 100, include_rts = True)
for tweet in tweets:
    print(tweet.created_at)
    print(tweet.text)
    tweet.favorite()
    print()
