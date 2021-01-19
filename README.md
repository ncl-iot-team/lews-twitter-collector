# LEWS Data-pipeline Module for Twitter Data Collection

This is the pipeline module for Tweet collection using streaming API and publish to a Kafka topic

## Pre-Requisites

- Docker 18.09.0 or higher

- Kafka Broker

- Streaming data in json format

### Install and run Kafka Broker
#### Ubuntu 18.04
Follow https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-18-04
#### Windows 
Follow https://medium.com/@shaaslam/installing-apache-kafka-on-windows-495f6f2fd3c8
#### MacOS
Follow https://medium.com/pharos-production/apache-kafka-macos-installation-guide-a5a3754f09c

## Running in local environment
### Install dependancies
Install dependancies given in requirements.txt. 
```bash
pip install -r requirements.txt
```

### Running the module

Running
```bash
python lews_tweet_collector.py
```

## Running in Docker (Recommended for Production)
### Building the Docker Image


```bash
docker build --tag lews-twitter-collector .
```

### Usage

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
