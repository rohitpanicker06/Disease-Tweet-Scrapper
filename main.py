import tweepy
import random
import json

def getClient():

#inputting my credentials for my application
    API_KEY = 'zltspIevSPOUSg9Lo9w5D0dfa'
    API_KEY_SECRET = 'ZkA222v3VjR0uwLYCaDbHDzlcRJ1gOiNeeCOXTs5TxRKD7rtKg'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAADe4iQEAAAAAU6RTWe2Qcnhav4hu7535nOiq%2Biw%3DmwWe99H4Wr25tWbdsWoKIYeh45z9Ah8ITVnZUGRfkW3fci5VgD'
    ACCESS_TOKEN = '1583522101733904384-N87zLJOVGnHqQfORqmuF5naR2i0uOe'
    ACCESS_TOKEN_SECRET = 'ctHEw04fm9jOfHSXcVbP9Gz6KBGPkruov6B9S3AcJSlrN'

    #creating an object for twitter client and passing above attributes to the clien

    client = tweepy.Client(bearer_token=BEARER_TOKEN,
                           consumer_key=API_KEY,
                           consumer_secret=API_KEY_SECRET,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
    return client


def searchTweets(client, query):
    tweets = client.search_recent_tweets(query=query, max_results=20)

    tweet_data = tweets.data
    results = []

    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj)

    else:
        return []
    return results


def getTweet(client, id):
    tweet = client.get_tweet(id, expansions=['author_id'], user_fields=['username'])
    return tweet


client = getClient()
tweets = searchTweets(client, 'diseases')

objs = []

if len(tweets) > 0:
    for tweet in tweets:
        twt = getTweet(client, tweet['id'])
        obj = {}
        obj['id'] = tweet['id']
        obj['username'] = twt.includes['users'][0].username
        obj['text'] = tweet['text']
        objs.append(obj)

f = open("TweepyResponse18October.json", "w")
j = json.dumps(objs)
f.write(j)
f.close()