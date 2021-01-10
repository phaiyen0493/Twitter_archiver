#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import json
import csv


# Enter Twitter API Keys
access_token = "1314305404042649606-Ce6s4Fwyw0h1WO85LF6Svc2XEa7waE"
access_token_secret = "GKNan6Ym1N4DF6A1TtBZ0azNtkqzy7mVMaRRWb4i0tuur"
consumer_key = "MQE25wUr0YHgcrnAzB5cEGrfL"
consumer_secret = "j1Q7XjHHczaQtzjGqWVO2Wi2rimGVXs3S3o24nuzND6iTgg2fO"

# Create tracklist with the words that will be searched for
userlist = ['25073877', '15207668', '14344823', '22203756', '939091', '14377605', '722793491059769344', '43963249', '242618658', '65493023', '15976697', '14828860']
tracklist = ['#voteTrump','#taxreform', '#RNC2020', '#republicans', '#reopeningschools', '#maga', '#conservative', '#keepamericangreat', '#americafirst', '#buildthewall', 'blacklivesmatter', '#trumpsupporters', '#libertarian', '#rightwing', '#democrats', '#obama', '#trump', '#hillary', '#for the people', '#trumpshutdown', '#protectourcare', '#actonclimate', '#endshutdown', '#equalityact', '#endgunviolence', '#election2020', '#ILeftTheGOP', '#gop']
languagelist = ['en']
counter = 0
num_tweets_to_grab = 500


# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):

	def on_data(self, status):
		global counter
		global num_tweets_to_grab
		tweet = json.loads(status)
	
		#print ("running.." + str(rc))
		if '' in status.lower() and 'retweeted_status' not in tweet.keys() and tweet['in_reply_to_user_id'] == None:
			#outputStr = tweet['created_at'] + "," + tweet['user']['id_str'] + "," + tweet['user']['name'] + ',"' + tweet['text'] + '"'
			#print (outputStr.encode('utf8'))
			print(status.encode('utf8'))
			
			counter += 1
			if counter == num_tweets_to_grab:
				return False
			return True

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream


if __name__ == '__main__':  
# Handle Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(languages = languagelist, track = tracklist, follow=userlist)
	