import tweepy, sys
from tokens import keys
from emoji import emoji

sys.path.append('tokens')

last_tweet = open("last-tweet.txt", "r+")

CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
TOKEN_SECRET = keys['TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)



# Retrieve last White House tweet
wh_tweet = api.user_timeline(id = 'WhiteHouse', count = 1)
tweet_text = wh_tweet[0].text



# Turns words in tweet into emoji -- doesn't work properly yet
def translate(tweet):
    print(tweet)
    for e in emoji:
        if e.lower() in tweet.lower():
            tweet = tweet.lower().replace(e.lower(), emoji[e])

    return tweet          



# Check against last White House tweet
if tweet_text in last_tweet:
    print('same')
    # translated_tweet = translate(tweet_text)
else:
    translated_tweet = translate(tweet_text)
    last_tweet.write(tweet_text)    



print(translated_tweet)