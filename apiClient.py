import requests
import threading
import json
import time

class ApiClient():
    def __init__(self, host):
        self.host = host

    def createParams(self, code, id, values):
        return {
            "id": id,
            "code": code,
            "value1": int(values[0]),
            "value2": int(values[1])
        }
    
    def post(self, data):
        headers = {
            'content-type': 'application/json',
            'X-Memopaddy-Sensor-Type': 'gate'}
        for i in range(3):
            s = requests.session()
            try:
                print('send')
                r = s.post(self.host,
                           data=json.dumps(data),
                           headers=headers,
                           timeout=10)
                #r = s.get('https://www.google.co.jp')
                try:
                    result = json.loads(r.text)
                except:
                    result ='Error1'
                if(r.status_code==200):
                    result = 'Success'
                else:
                    result = r.status_code
                break
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                result = 'Error2'
            except:
                break
            return result
