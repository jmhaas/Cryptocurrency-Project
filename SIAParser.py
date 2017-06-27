import requests
import json
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

hdr = {'User-Agent': 'Mac:r/bitcoin-ethereum.sentiment.analysis:v1.0' +
       '(by /u/jmhaas821'}
url = 'https://www.reddit.com/r/bitcoin/new/.json'
req = requests.get(url, headers=hdr)
json_data = json.loads(req.text)
posts = json.dumps(json_data['data']['children'], indent=4, sort_keys=True)

data_all = json_data['data']['children']
num_of_posts = 0
while len(data_all) <= 100:
    time.sleep(2)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/bitcoin/new/.json?after=' + str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    data_all += data['data']['children']
    if num_of_posts == len(data_all):
        break

    else:
        num_of_posts = len(data_all)

sia = SIA()
pos_list = []
neg_list = []
neu_list = []
for post in data_all:
    res = sia.polarity_scores(post['data']['title'])

    print(res)

    if res['compound'] > 0.2:
        pos_list.append(post['data']['title'])
    elif res['compound'] < -0.2:
        neg_list.append(post['data']['title'])
    elif res['compound'] == 0.0:
        neu_list.append(post['data']['title'])


with open("pos_news_titles.txt", 'w') as f_pos:
    for post in pos_list:
        f_pos.write(post.encode("utf-8") + "\n")

with open("neg_news_titles.txt", 'w') as f_neg:
    for post in neg_list:
        f_neg.write(post.encode("utf-8") + "\n")

with open ("neu_news_title.txt", 'w') as f_neu:
    for post in neu_list:
        f_neu.write(post.encode("utf-8") + "\n")
