#!/bin/python3
# A little bitty twitter bot stream by a little bitty python programmer
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.0.1

# Modules
import requests
import random
import tweepy                 # Docs: http://docs.tweepy.org/en/latest/api.html#api-reference
from PIL import Image         # Docs: https://pillow.readthedocs.io/en/5.1.x/
from PIL import ImageFile
from io import BytesIO
from secrets import *

# Instatntiate OAuth Handler Instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth) # Creates an API object, which will act as the primary handler for most of our bot's actions.

ImageFile.LOAD_TRUNCATED_IMAGES = True

def tweet_image(url,username,status_id):
    filename = 'temp.png'

    # Send a get request
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        i = Image.open(BytesIO(request.content))
        i.save(filename)
        scramble(filename)

        api.update_with_media('scramble.png', status='Scrambled an image for: @{0}'.format(username), in_reply_to_status_id=status_id)
    else:
        print("Unable to download image")

def scramble(filename):
    BLOCKLEN = 64  # Adjust and be careful here.
    img = Image.open(filename)
    width, height = img.size
    xblock = width // BLOCKLEN
    yblock = height // BLOCKLEN
    # creates sequence of 4-tuples (box) defining the left, upper, right, and lower pixel coordinate
    blockmap = [(xb * BLOCKLEN, yb * BLOCKLEN, (xb + 1) * BLOCKLEN, (yb + 1) * BLOCKLEN)
                for xb in range(xblock) for yb in range(yblock)]
    shuffle = list(blockmap)
    #shuffle the sequence
    random.shuffle(shuffle)
    # Creates a new image with the given mode and size.
    result = Image.new(img.mode, (width, height))
    for box, sbox in zip(blockmap, shuffle):
        # Returns a rectangular region from this original image.
        crop = img.crop(sbox)
        # Pastes the cropped pixel into the new image Object
        result.paste(crop, box)
    result.save('scramble.png')

class BotStreamer(tweepy.StreamListener):
    # This gets called when a new status arrives. This is passed from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        # Entities provides information that doesn't require parsing
        if 'media' in status.entities:
            for image in status.entities['media']:
                tweet_image(image['media_url'],username, status_id)




# Stream Object
myStreamListener = BotStreamer()
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@imaketweetbot'])