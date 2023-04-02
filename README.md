# Redis-pubsub
This repo demonstrates how Redis can be used as a Publisher/Subscriber platform via a redis-client using python3. In this pattern, publishers can issue messages to any number of subscribers on a channel. These messages are fire-and-forget, in that if a message is published and no subscribers exists, the message evaporates and cannot be recovered.

### Setting up redis locally using docker -

1. make sure docker is installed
2. Fetch latest redis image using `docker pull redis`
3. created a dedicated network for redis `docker network create redis`
4. Spin-up the redis container using `docker run --name redis-docker --network redis --detach --publish 16379:6379 redis:latest redis-server`
