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
	print("Downloading info for user: "+scream_name)
	filename=scream_name+"_user_"+tudei+".json"
	yuser = api.get_user(screen_name = scream_name)
	with open(filename, 'a+') as outfile:
		json.dump(yuser._json, outfile)
		outfile.write("\n")
		outfile.close()
	

