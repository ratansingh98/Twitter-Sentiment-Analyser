# Imports
import tweepy
from textblob import TextBlob
import pprint
import csv

class tweetss:
    def __init__(self,search_input):   
        # Authentication
        consumer_key = 'CONSUMER_KEY_HERE'
        consumer_secret = 'CONSUMER_SECRET_HERE'

        access_token = 'ACCESS_TOKEN_HERE'
        access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        api = tweepy.API(auth)  

        # Retrieve Tweets
        public_tweets = api.search(search_input)

        # Write Tweets to csv
        with open('data/ data.csv', 'w', encoding='utf-8') as csvfile:
            fieldnames = ['Text', 'Polarity', 'Subjectivity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    
            for tweet in public_tweets:
                analysis = TextBlob(tweet.text)
                writer.writerow({'Text': tweet.text, 'Polarity': analysis.sentiment[0], 'Subjectivity': analysis.sentiment[1]})

