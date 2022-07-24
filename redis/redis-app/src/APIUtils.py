import json
class APIUtils(object):

    def __init__(self):
        pass
    def validatePostRequest(self,data):
        isValidRequest = False
        if data is not None:
            if "key" in data:
                isValidRequest = True
        return isValidRequest

    def convertReqDataToString(self,data):
        processedData = None
        if type(data) is dict:
            processedData = json.dumps(data)
        elif type(data) is list:
            processedData = ''.join(str(x) for x in data)
        else:
            processedData = data
        return processedData
