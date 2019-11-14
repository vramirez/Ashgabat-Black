import sys
import json
import time
from tweepy import Cursor
from twitter_client import get_twitter_client

def usage():
    print("Usage:")
    print("python {} <hashtag>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    hashtag = sys.argv[1]
    client = get_twitter_client()
    size=0
    fname = "search_{}.jsonl".format(hashtag)
    with open(fname, 'w') as f:
        for tweets in Cursor(client.search,q=hashtag+" -filter:retweets",count=100,lang="es").pages():
            pagesize=len(tweets)
            size+=pagesize
            print("Writing {} tweets. Total {}".format(pagesize,size))
            for tweet in tweets:
                f.write(json.dumps(tweet._json)+"\n")
            time.sleep(5)

