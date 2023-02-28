import redis
import json

from exp_1_pub import check_redis_conn, channel


if __name__ == '__main__':
    redis_up = check_redis_conn()
    if redis_up:
        from exp_1_pub import redis_cli

        subs = redis_cli.pubsub()
        subs.subscribe(channel)
        print(f'Subsribed to channel = {channel}')
        print('\nGetting the message...........')
        for msg in subs.listen():
            print(msg)
    else:
        print(f'Redis server is not accessible.')