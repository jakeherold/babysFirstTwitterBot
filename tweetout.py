#!/bin/python3
# Takes command line input and tweets them out based on space delimiters (unless quote wrapped)
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.0.2

# Modules
import sys
import tweepy                 # Docs: http://docs.tweepy.org/en/latest/api.html#api-reference
from PIL import Image         # Docs: https://pillow.readthedocs.io/en/5.1.x/
from PIL import ImageFile
from secrets import *


# Instatntiate OAuth Handler Instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth) # Creates an API object, which will act as the primary handler for most of our bot's actions.

# Command line input
arguments = sys.argv[1:]
if (len(arguments) == 1):
    for tweet in arguments:
        print("Sending out tweet: '" + str(tweet) + "'")
        api.update_status(tweet)
else:
    print("One tweet at a time, yah hoser! NO TWEET FOR YOU!")