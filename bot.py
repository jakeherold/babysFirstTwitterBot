#!/bin/python3
# A little bitty twitter bot by a little bitty python programmer
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

# Include unicode error handler because my computer's interpretation of python is garbage. 
# Source: https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# Read Tweets on my timeline
# Note: This is causing issues with the CLI I'm running due to the odd character incoding. Feel free to uncomment and play with the giant json blob. 
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     uprint(str(tweet) + '\n')


# Get list of followers
user = api.get_user('imaketweetbot')
for friend in user.friends():
    print(friend.screen_name)