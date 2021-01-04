FROM python:3.9
COPY . /app
WORKDIR /apd 
ENTRYPOINT ["python", "lews_tweet_collector.py"]