# -*- coding: utf-8 -*-
import tweepy
import csv

"""
福岡にいて、python関連のつぶやきをしている人を探します。
範囲は博多駅を起点に70kmです。北九州市も入っています。

外部に公開するときは必ず差し替え!
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
"""


auth = tweepy.OAuthHandler("5Pt6ob1b92JaUwhAODVLnRFHt", "WlOVWQlHSzHqD90KO4usuQpZ4FV4porfP9YFHYVSnJeZdm9rJN")
auth.set_access_token("955375129072082944-GZrtqDIoaovWQ9vgIDLdYTIIoMhP3FZ", "bCZQQ8Ab3pwiEXGQdCnNTgbDubA7SkbWlTPFOwtNyoksi")

api = tweepy.API(auth)

#csv出力
with open('tweets_python.csv', 'w+',newline='',encoding='utf-8') as f:
    n = 0
    # 「q」には需要に応じて'python' or 'py' or 'Progate' or 'progate' or 'プロゲート'なども追加しましょう
    for status in api.search(q = 'python' or 'py', lang='ja', geocode="33.590045,130.420611,100km", count=100):
        sc_n = status.user.screen_name
        u_loc = status.user.location

        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([n, '@' + sc_n, u_loc])
        n += 1
pass