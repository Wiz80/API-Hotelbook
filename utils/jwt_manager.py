from jwt import encode, decode
from config.redis import getRedisConnection


def createToken(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    # Connect to Redis and store the session data
    connection = getRedisConnection()
    # Assuming 'id' is a unique identifier for the user
    connection.set(data['id'], token)
    return token


def validateToken(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=["HS256"])
    # Connect to Redis and verify the session data
    connection = getRedisConnection()
    redis_token = connection.get(data['id'])
    if not redis_token or redis_token.decode('utf-8') != token:
        raise Exception("Invalid session or token.")
    return data
