from redisOperations import RedisOperations
import os
HOST = os.getenv('REDIS_HOST',default='localhost')
PORT = os.getenv('REDIS_PORT',default='6379')

db = RedisOperations(HOST,PORT,0)
res = db.getOp("ashish")
print(res.decode('utf-8'))