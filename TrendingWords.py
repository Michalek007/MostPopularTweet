import tweepy

bearer_token = '<your bearer_token>'
client = tweepy.Client(bearer_token= bearer_token)
keyword = ' -keyword'

# choose keywords that are interesting for you
query_list = ['wino', 'browar', 'piwo']
tweet_stats = {}
for i in range(len(query_list)):
    query = query_list[i] + keyword
    response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at','lang','public_metrics'], expansions=['author_id'], user_fields=['username'])
    like_count = 0
    retweet_count = 0
    reply_count = 0
    quote_count = 0
    for tweet in response.data:
        like_count += tweet.public_metrics['like_count']
        retweet_count += tweet.public_metrics['retweet_count']
        reply_count += tweet.public_metrics['reply_count']
        quote_count += tweet.public_metrics['quote_count']
    tweet_stats[query_list[i]] = [like_count, retweet_count, reply_count, quote_count]
print("Statistic are in the following order: likes, retweets, replies, quotes.")
print(tweet_stats)
