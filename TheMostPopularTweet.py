import tweepy
import json

Bearer_Token = "<Your bearer_token>"

client = tweepy.Client(bearer_token=Bearer_Token)

keyword = ' -keyword'
link = 'https://twitter.com/'
status = '/status/'

print("Write your keyword: ")
query = str(input())
query_list = [query]

last_tweet = 'last'
hit_tweet = {last_tweet: 0}
most_popular_tweet = []
ID = {}
ID_list = []
links_list = []
for i in range(len(query_list)):
    query = query_list[i] + keyword
    response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at','lang','public_metrics'], expansions=['author_id'], user_fields=['username'])
    users = {}
    for u in response.includes['users']:
        users[u['id']] = u['username']
    for tweet in response.data:
        if tweet.public_metrics['like_count'] > hit_tweet[last_tweet]:
            hit_tweet.clear()
            ID.clear()
            last_tweet = tweet.text
            hit_tweet[tweet.text] = tweet.public_metrics['like_count']
            ID[users[tweet.author_id]] = tweet.id


    ID_list.append(ID)
    most_popular_tweet.append(hit_tweet)
    hit_tweet.clear()
    last_tweet = 'last'
    hit_tweet[last_tweet] = 0

for key in ID:
    links_list.append(link + key + status + str(ID[key]))
with open('C:\\Users\\Public\\tweets.json', 'w', encoding='utf-8') as write_file:
    json.dump(links_list, write_file)

print(links_list[0])
