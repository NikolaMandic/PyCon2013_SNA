import twython
from twython import TwythonStreamer
from utils import *
import networkx as net

import matplotlib.pyplot as plt
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after


retweets=net.DiGraph()
hashtag_net=net.Graph()
c=0


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:

          global c
          if c>100:
            print c
            print "disconnecting"
            self.disconnect()
          #if c>50000: 
            
          ### process tweet to extract information
          c+=1
          try:
              author=data['user']['screen_name']
              entities=data['entities']
              mentions=entities['user_mentions']
              hashtags=entities['hashtags']

              for rt in mentions:
                      alter=rt['screen_name']
                      retweets.add_edge(author,alter)

              tags=[tag['text'].lower() for tag in hashtags]
              for t1 in tags:
                      for t2 in tags:
                              if t1 is not t2:
                                      c+=1
                                      add_or_inc_edge(hashtag_net,t1,t2)
          except :
              print ':-('


          print data['text'].encode('utf-8')
        # Want to disconnect after the first result?

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
class StdOutListener:
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""



if __name__ == '__main__':
    #l = StdOutListener()
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)

    #words = ["#teen"]
    #stream = Stream(auth, l)
    print "here"
    #stream.filter(track=words)

    print APP_KEY
    print APP_SECRET
    print OAUTH_TOKEN
    print OAUTH_TOKEN_SECRET
    stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    stream.statuses.filter(track='twitter')
    net.draw(hashtag_net)
    plt.draw()
    plt.show()
    print "here1"


##people = [123,124,125]
#locations = ["-122.75,36.8", "-121.75,37.8"] #, follow=people, locations=locations

