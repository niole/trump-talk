# pylint: disable-all
import tweepy
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from os import getenv

CONSUMER_KEY = getenv('CONSUMER_KEY')
CONSUMER_SECRET = getenv('CONSUMER_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(AUTH)

def get_tweets_w_handle(handle, count):
    return map(lambda tweet: tweet.text, API.user_timeline(screen_name = handle, count = count, include_rts = True))

def get_tweets(count):
    return map(lambda tweet: (tweet.id, tweet.text), API.user_timeline(screen_name = 'realDonaldTrump', count = count, include_rts = True))

def get_tweets_since_id(tweet_id, count):
    return map(lambda tweet: (tweet.id, tweet.text), API.user_timeline(screen_name = 'realDonaldTrump', since_id = tweet_id, count = count, include_rts = True))
