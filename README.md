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
-e TWITTER_FILTER_TRACK="<filter tracks>" \
-e MODULE_NAME="LEWS-TWITTER-DATA-COLLECTOR" \
-e CONSUMER_GROUP="LEWS-TWITTER-DATA-COLLECTOR-CG01" \
-e KAFKA_TARGET_BOOTSTRAP_SERVERS="<kafka_bootstrap_server>" \
-e KAFKA_TARGET_TOPIC="<topic>" lews-twitter-collector
```
