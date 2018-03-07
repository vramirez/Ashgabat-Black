#A python3 file

import os,configparser,math,sys,time,tweepy,json

config = configparser.RawConfigParser()
config.read('twauth.properties')


consumer_key=config.get('OAuth','key')
consumer_secret=config.get('OAuth','key_secret')
access_key=config.get('OAuth','token')
access_secret=config.get('OAuth','token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
scream_name="transmilenio"
tudei=time.strftime("%Y%m%d")

if len(sys.argv)>1 :
        scream_name=str.lower(sys.argv[1])


for scream_name in sys.argv[1].split(","):
	print("Downloading up to 3200 most recent tweets from: "+scream_name)
	filename=scream_name+"_tweets_"+tudei+".json"
	alltweets=[]
	tweets = api.user_timeline(screen_name = scream_name,count=200)
	alltweets.extend(tweets)
	oldest = alltweets[-1].id -1


	while (len(tweets)>1):
		tweets = api.user_timeline(screen_name = scream_name,count=200,max_id=oldest)
		alltweets.extend(tweets)
		oldest = alltweets[-1].id -1 	
		print("Getting new:"+str(len(tweets))+" total: "+str(len(alltweets)))


	for tweet in alltweets:
		with open(filename, 'a+') as outfile:
			json.dump(tweet._json, outfile)
			outfile.write("\n")
			outfile.close()
	

