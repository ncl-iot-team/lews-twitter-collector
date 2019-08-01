import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

# Print Twitter credentials -- Testing
#print(os.getenv('TWITTER_ACCESS_TOKEN', 'NA'))
#print(os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'NA'))
#print(os.getenv('TWITTER_CONSUMER_KEY', 'NA'))
#print(os.getenv('TWITTER_CONSUMER_SECRET', 'NA'))

access_token =  os.getenv('TWITTER_ACCESS_TOKEN', 'NA')
access_token_secret =  os.getenv('TWITTER_ACCESS_TOKEN_SECRET','NA')
consumer_key =  os.getenv('TWITTER_CONSUMER_KEY','NA')
consumer_secret =  os.getenv('TWITTER_CONSUMER_SECRET','NA')


class StdOutListener(StreamListener):


    def on_data(self, data):
    
        producer.send_messages(os.getenv('KAFKA_TOPIC','lews-twitter'), data.encode('utf-8'))
    
        print (data)
    
        return True


    def on_error(self, status):
    
        print (status)


kafka = KafkaClient(os.getenv('KAFKA_BROKER','host.docker.internal:9092'))

producer = SimpleProducer(kafka)

l = StdOutListener()

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)

stream.filter(track="rain")
