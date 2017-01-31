# pylint: disable-all

"""
space for running word generation logic
"""
from tweet_getter import get_tweets_w_handle
from word_generator import generate_words
from random import shuffle
from tweet_data_cleaner import get_clean_data

djt = get_tweets_w_handle('realDonaldTrump', 100)
ct = get_tweets_w_handle('ChuckTingle', 100)

CONTENT = djt+ct

shuffle(CONTENT)

CONTENT = get_clean_data(CONTENT)

TOTAL_ITERATIONS = 1000
generate_words(TOTAL_ITERATIONS, CONTENT, 3)
