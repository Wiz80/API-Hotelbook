import redis

# Redis connection
def getRedisConnection():
    return redis.Redis(host='localhost', port=6379, db=0)
