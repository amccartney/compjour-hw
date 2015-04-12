import json
import os.path
from glob import glob
from datetime import datetime
from operator import itemgetter

DATA_DIR = 'data-hold'
PROFILES_DIR = os.path.join(DATA_DIR, 'profiles')
TWEETS_DIR = os.path.join(DATA_DIR, 'tweets')
screen_name = 'repmikehonda'

pfname = os.path.join(PROFILES_DIR, screen_name + '.json')
profile = json.loads(open(pfname).read())

print ("{} goes by the screen_name {}:".format(profile['name'], screen_name))

print ("* Has {} followers and follows {}".format(profile['followers_count'], profile['friends_count']))

cr_date = datetime.strptime(profile['created_at'], '%a %b %d %H:%M:%S +0000 %Y')

days_since_created_at = (datetime.today() - cr_date).days

print ("* Has been on Twitter for {} days".format(days_since_created_at))

daily_tweet_rate = round(profile['statuses_count'] / days_since_created_at, 2)

print ("* Overall Tweet rate of {} tweets/day".format(daily_tweet_rate))

tfname = os.path.join(TWEETS_DIR, screen_name + 'json')
tweets = json.loads(open(tfname).read())

original_tweets = [t for t in tweets if t.get('retweeted_status') == None]

print ("* Has {} original tweets in his last {}". format(len(original_tweets), len(tweets)))

tweets_sorted_by_rts = sorted(original_tweets, key = itemgetter('retweet_count'), reverse = True)

rt = tweets_sorted_by_rts[0]

print ("* Most retweeted tweet has {} RTs and said: {}".format(rt['retweet_count'], rt['text']))