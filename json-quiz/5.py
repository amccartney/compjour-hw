import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json"

obj = json.loads(requests.get(data_url).text)

hashtag_objs = obj['entities']['hashtags']
hashtag_texts = []

url_objs = obj['entities']['urls']
urls = []

print("A. " + obj['created_at'])
print("B. " + obj['user']['created_at'])
print("C. " + obj['text'])
print("D. " + obj['user']['name'])
print("E. " + str(obj['id']))
print("F. " + str(len(obj['entities']['user_mentions'])))
for h in hashtag_objs:
	hashtag_texts.append(h['text'])
print("G. " + ','.join(hashtag_texts))
for u in url_objs:
	urls.append(u['display_url'])
print("H. " + ','.join(urls))
