# -*- coding: utf-8 -*-
import tweepy
import csv

"""
福岡にいて、python関連のつぶやきをしている人を探します。
範囲は博多駅を起点に70kmです。北九州市も入っています。

外部に公開するときは必ずtweepy.OAuthHandler, auth.set_access_tokenの中身差し替え!
"""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

#csv出力
with open('tweets_python.csv', 'w+',newline='',encoding='utf-8') as f:
    n = 0
    for status in api.search(q = 'python' or 'py', lang='ja', geocode="33.590045,130.420611,100km", count=100):
        sc_n = status.user.screen_name
        u_loc = status.user.location

        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([n, '@' + sc_n, u_loc])
        n += 1
pass