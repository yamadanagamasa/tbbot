import tweepy
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

consumer_key = 'BRDeJviFEF568vfxonil3mbCo'
consumer_secret = 'V62gimExxDqd0qHhNjoVVn3HkjPkr4mUgCajqqpNLq0fUXhXbX'
access_token = '1322165929757700097-VuXLQSxjQRpieVsX0sF9N3xvuk5Z5Z'
access_token_secret = 'ASWtiiQJ6E71vcEmZQIwzKRR69b9MlvGOK1msoKcfJQvx'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    for status in api.search(q='ごはん', count=100):
        tweet_id = status.id
# 例外処理をする
        try:
# いいね実行
            api.create_favorite(tweet_id)
            print("ok")
        except:
            print('error')

sched.start()