import time
import redis
import configparser
# while True:
#     print(time.time())
#     time.sleep(10)

CONFIG = configparser.RawConfigParser()
CONFIG.read('../config/config.ini')

# redis配置
redis_host = CONFIG.get('redis', 'host')
redis_port = CONFIG.get('redis', 'port')
redis_password = CONFIG.get('redis', 'password')

print(redis_host)
print(redis_port)
print(redis_password)

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)

print(redis_client.get('foo'))