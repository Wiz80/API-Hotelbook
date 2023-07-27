import redis
import os
from dotenv import load_dotenv

load_dotenv()


# Redis connection
def getRedisConnection():
    return redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)
