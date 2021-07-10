import json
import argparse
import pycountry
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

# import twitter keys and tokens
from configration import *

# create instance of elasticsearch
es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])


class TweetStreamListener(StreamListener):
    def __init__(self, es_index_name):
        self.es_index_name = es_index_name

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print(tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print(sentiment)

        if dict_data["user"]["location"] != None:
            user_geo = dict_data["user"]["location"]
        # There was an issue parsing the 'geo' attribute - TODO
        # elif dict_data["geo"] != None: 
        # user_geo = dict_data["geo"]
        elif dict_data["place"] != None:
            user_geo = dict_data["place"]
        else:
            user_geo = 'unknown'

        print(f'Discovered GEO: {user_geo}')

        for c in pycountry.countries:
            if c.name in user_geo or c.alpha_2 in user_geo:
                # Country's name
                print(c.name)
                # Country's code
                print(c.alpha_2)
                user_geo = c.name
                break
        print(f'Final GEO: {user_geo}')

        # add text and sentiment info to elasticsearch
        es.index(index=self.es_index_name,
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "geo": user_geo,
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Twitter topic arguments')
    parser.add_argument('--index-name', help='ElasticSearch Index Name', required=True)
    parser.add_argument('--filter', help='Twitter filter to use', required=True)
    args = parser.parse_args()

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener(args.index_name)

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for the required keyword
    stream.filter(track=[args.filter])