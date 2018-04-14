#!/bin/python3
# A little bitty twitter bot stream by a little bitty python programmer
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.0.1

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