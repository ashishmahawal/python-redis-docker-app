import logging
import json
from APIUtils import APIUtils
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)
from redisOperations import RedisOperations
HOST = "redis"
PORT = "6379"
db = RedisOperations(HOST,PORT,0)

@app.route('/getkey', methods=['GET'])
def getkey():
    args = request.args
    print(f'[getKey] Recieved following args :{request.args}')
    key = args.get('key')
    res = db.getOp(key)
    if res is not None:
        res = res.decode('utf-8')
    print(f'/getKey returning response :{res}')
    return {key:res},200

@app.route('/setkey',methods=['POST'])
def setKey():
    # Flask Request will get body from POST request in this way
    reqBody = request.json
    apiUtils = APIUtils()
    isValidRequest = apiUtils.validatePostRequest(reqBody)
    key = reqBody['key']
    value = apiUtils.convertReqDataToString(reqBody['value'])
    if isValidRequest:
        db.setOp(key,value)
    else:
        return {error:'Invalid Request body'},501
    return reqBody,200

@app.route('/',methods=['GET'])
def baseMethod():
    return {"response":"Hello ,Welcome to Python App by Ashish....."}

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
