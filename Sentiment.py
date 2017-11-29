from textblob import TextBlob
import tweepy

consumer_key = '8fyYqm49CTRR5H0JRkhx####'
consumer_secret = 'eM5L0a0WYzZtT8r3quBiE4SVOz1IjZYHcST1gy####'

access_token = '4015739903-dq9HrBPcWmS4Lfulwcx9gBqrAG73######'
access_token_secret = 'todlONeA68QUgmPYRuKMz8EhyYEdFBlE#######'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Mubarakan')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
//hjgjahgjahgadfgshkjhdkjhkajhsdkjhs cjhksjdhfkjhfksjhfkjs
