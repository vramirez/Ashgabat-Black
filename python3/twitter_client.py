# Chap02-03/twitter_client.py 
import os 
import sys 
from tweepy import API 
from tweepy import OAuthHandler 
import configparser
def get_twitter_auth(): 
	"""Setup Twitter authentication. 

	Return: tweepy.OAuthHandler object 
	""" 
	try:
		config = configparser.RawConfigParser()
		config.read('twauth.properties')
		consumer_key = config.get('OAuth','key')
		consumer_secret = config.get('OAuth','key_secret')
		access_token = config.get('OAuth','token')
		access_secret = config.get('OAuth','token_secret')

		#consumer_key = os.environ['TWITTER_CONSUMER_KEY'] 
		#consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'] 
		#access_token = os.environ['TWITTER_ACCESS_TOKEN'] 
		#access_secret = os.environ['TWITTER_ACCESS_SECRET'] 
	except KeyError: 
		sys.stderr.write("TWITTER_* environment variables not set\n") 
		sys.exit(1) 
	auth = OAuthHandler(consumer_key, consumer_secret) 
	auth.set_access_token(access_token, access_secret) 
	return auth 

def get_twitter_client(): 
  """Setup Twitter API client. 
 
  Return: tweepy.API object 
  """ 
  auth = get_twitter_auth() 
  client = API(auth) 
  return client 

