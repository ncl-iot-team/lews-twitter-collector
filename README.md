# LEWS Twitter Data Collector

This program collects Twitter data in real-time and publishes to a Kafka broker

## Pre-Requisites

- Docker 18.09.0 or higher

- Kafka Broker

- Twitter API Credentials (access token, access token secret, consumer key, consumer secret)


## Building the Docker Image


```bash
docker build --tag lews-twitter-collector .
```

## Usage

```bash
docker run -e TWITTER_ACCESS_TOKEN="<access token>" \
-e TWITTER_ACCESS_TOKEN_SECRET="<access token secret>" \
-e TWITTER_CONSUMER_KEY="<consumer key>" \
-e TWITTER_CONSUMER_SECRET="<consumer secret>" \
-e TWITTER_FILTER_TRACK="<comma separated filter tracks>" \
-e KAFKA_BOOTSTRAP_SERVERS="<comma separated kafka-broker-host:port>" \
-e KAFKA_TOPIC="<kafka-topic-to-publish-to>" lews-twitter-collector
```
