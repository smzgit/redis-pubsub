import redis
import json
from essential_generators import DocumentGenerator

gen = DocumentGenerator()
redis_cli = None
channel = "quotes_channel"

def check_redis_conn():
    global redis_cli
    try:
        redis_cli = redis.Redis(host="localhost", port=16379, decode_responses=True, encoding="utf-8")
        print(f'Pinging redis server....')
        print(redis_cli.ping())
        return True
    except Exception as ex:
        print(f'Failed to connect to Redis server\nError :  {ex}')
        return False


def get_msg_to_publish():
    try:
        sentence = gen.sentence()
        return sentence
    except Exception as ex:
        print(f'Failed to get quotes from url\nError : {str(ex)}')
        return str(ex)


def publish_msg(message, channel):
    try:
        op = redis_cli.publish(channel, json.dumps(message))
        print(f'Published msg to {channel}, with response = {op}')
        return True
    except Exception as ex:
        print(f'error in publishing msg = {message} to channel = {channel}\nError: {ex}')
        return False


if __name__ == '__main__':
    redis_up = check_redis_conn()
    if redis_up:
        message = get_msg_to_publish()
        op = publish_msg(message, channel)
        if op:
            print(f"Successfully published message = {message} to channel = {channel}")
        else:
            print(f"Failed to publish message = {message} to channel = {channel}")
    else:
        print(f'Redis server is not accessible.')
