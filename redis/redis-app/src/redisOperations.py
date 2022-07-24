import redis

class RedisOperations(object):

    def __init__(self,host: str,port: int,dbNum: int):
        self._host = host
        self._port = port
        self._dbNum = dbNum
        print(f'[RedisOperations] _host :{self._host}')
        print(f'[RedisOperations] _port :{self._port}')
        self._redisDB = self.createDBInstance(dbNum)
    
    def createDBInstance(self,dbNum: int):
        redisConn = redis.StrictRedis(host=self._host, port=self._port, db=dbNum)
        print(f'[getRedisDB] Successfully connected to Redis DB')
        return redisConn

    def setOp(self,key:str,value: str):
        if self._redisDB is None:
            raise Exception(f'Create Redis DB Instance first')
        try:
            res = self._redisDB.set(key,value)
            print(f'Redis Set Operation :{res}')
        except Exception as e:
            print(f'Exception :{e} while setting key :{key} ')

    def getOp(self,key: str):
        if self._redisDB is None:
            raise Exception(f'Create Redis DB Instance first')
        try:
            res = self._redisDB.get(key)
            return res
            print(f'Redis Get Operation :{res}')
        except Exception as e:
            print(f'Exception :{e} while getting key :{key} ')

    def getAll():
        if self._redisDB is None:
            raise Exception(f'Create Redis DB Instance first')
        try:
            res = self._redisDB.get(key)
            print(f'Redis Get Operation :{res}')
        except Exception as e:
            print(f'Exception :{e} while getting key :{key} ')
        


