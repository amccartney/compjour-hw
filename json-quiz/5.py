import tweepy

tweet = client.statuses_lookup([586227094285225984])[0]
tweet_dict = tweet._json
print(json.dumps(tweet_dict, indent = 2))
