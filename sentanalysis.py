from textblob import TextBlob
from twitcredentials import * 
import numpy as np
import sys
import tweepy
import matplotlib as mpl
mpl.use("TkAgg")
from matplotlib import pyplot as pyplot

# Establish connection to twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

item = input("Enter word/hashtag you want to search for: ")
num_items = int(input("How many tweets do you want to analyze? (Max 50): "))

'''
search for tweets containing specified item (as many as specified by num_items)
Only returns tweets written in english 
'''
tweets = tweepy.Cursor(api.search, q=item, lang="en").items(num_items)

'''
These arrays are used to store polarity values of all the gathered tweets in their respective arrays
'''
negative_sentiments = []
neutral_sentiments = []
positive_sentiments = []
sentiment_totals = []

'''
Initialize variables to keep track of number of tweets belonging to each sentiment type
These variables are eventually used to represent the total number of tweets for each sentiment type
'''
negative = 0
positive = 0
neutral = 0

# Initialized sentiments array to use for matplotlib bar chart (will be x-axis values)
sentiments = ["Negative", "Neutral", "Positive"]

# use a for loop to print out each tweet, and use textblob to check sentiment of tweet
for tweet in tweets:
	# print out the text portion of the tweet
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment.polarity)
	'''
	Polarity can range from -1.0 to 1.0, so we categorize each polarity score
	Polarity < 0.0 --> Negative sentiment
	Polarity == 0.0 --> Netural sentiment
	Polarity > 0.0 --> Positive sentiment
	'''
	if (analysis.sentiment.polarity < 0.0):
		print("This tweet is likely negative\n")
		# increment negative variable to add to tweet count 
		negative = negative + 1
	elif (analysis.sentiment.polarity == 0.0):
		print("This tweet is likely neutral\n")
		# increment neutral variable to add to tweet count 
		neutral = neutral + 1
	elif (analysis.sentiment.polarity > 0.0):
		print("This tweet is likely positive\n")
		# increment positive variable to add to tweet count 
		positive = positive + 1
	print
			
# add total number of negative, neutral and positive tweets to an array
sentiment_totals.append(negative)
sentiment_totals.append(neutral)
sentiment_totals.append(positive)

print(negative)
print(neutral)
print(positive)
print(sentiments)

# create data visualization 
pyplot.title("Polarity for " + str(num_items) + " tweets containing \"" + item + "\"")
# use a bar chart
pyplot.bar(sentiments, sentiment_totals, color=['xkcd:coral','xkcd:lightblue','xkcd:lime'], edgecolor='k')
pyplot.xlabel("Type of Sentiment")
pyplot.ylabel("Number of Tweets")
pyplot.show()
