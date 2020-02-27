import os,json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer

# Print Twitter credentials -- Testing
#print(os.getenv('TWITTER_ACCESS_TOKEN', 'NA'))
#print(os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'NA'))
#print(os.getenv('TWITTER_CONSUMER_KEY', 'NA'))
#print(os.getenv('TWITTER_CONSUMER_SECRET', 'NA'))



access_token =  os.environ.get('TWITTER_ACCESS_TOKEN', 'NA')
access_token_secret =  os.environ.get('TWITTER_ACCESS_TOKEN_SECRET','NA')
consumer_key =  os.environ.get('TWITTER_CONSUMER_KEY','NA')
consumer_secret =  os.environ.get('TWITTER_CONSUMER_SECRET','NA')
twitter_stream_filter = os.environ.get("TWITTER_FILTER_TRACK","landslide").split(",")
kafka_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS","host.docker.internal:9092").split(",")
kafka_topic = os.environ.get('KAFKA_TOPIC', 'lews-twitter')

print("Environment variables:")
print(f"TWITTER_ACCESS_TOKEN = {access_token}")
print(f"TWITTER_ACCESS_TOKEN_SECRET = {access_token_secret}")
print(f"TWITTER_CONSUMER_KEY = {consumer_key}")
print(f"TWITTER_CONSUMER_SECRET = {consumer_secret}")
print(f"TWITTER_FILTER_TRACK = {twitter_stream_filter}")
print(f"KAFKA_BOOTSTRAP_SERVERS = {kafka_servers}")
print(f"KAFKA_TOPIC = {kafka_topic}")

class StdOutListener(StreamListener):


    def on_data(self, data):

        tweet_json=data
    
        producer.send(kafka_topic, tweet_json)
    
        print (data)
    
        return True


    def on_error(self, status):
    
        print (status)


producer = KafkaProducer(bootstrap_servers=kafka_servers,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

l = StdOutListener()

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)

stream.filter(track=twitter_stream_filter,is_async=True)
