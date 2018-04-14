import csv
import tweepy
from urlextract import URLExtract
from textblob import TextBlob

#insert your twitter api access data below.

consumer_key = 	'x' 
consumer_secret = 	'x'

access_token = 	'x'
access_token_secret = 'x'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#searching for AI on Twitter via Twitter APi
public_tweets = api.search('AI')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)

#Writing the mined data to a csv file and analyse it with TextBlob
csvfile = open('twitter_sentiment.csv', 'w') #open file for operation
writer = csv.writer(csvfile)   

for tweet in public_tweets:
    foo = tweet.text 

    analysis = TextBlob(tweet.text).sentiment
    emotion = analysis.polarity
    if emotion == 0:
        writer.writerow([foo,'neutral', emotion])
    elif emotion > 0:
       writer.writerow([foo,'positive', emotion]) 
    else : 
       writer.writerow([foo,'negative', emotion])         
    
csvfile.close()
print("succss")