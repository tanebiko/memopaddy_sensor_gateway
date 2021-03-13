import unittest
from apiClient import ApiClient
from db import DB

class ApiClientTest(unittest.TestCase):
    def test_createParams(self):
        http = '160.16.10.1'
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        conn = DB(host, db, user, password)
        client = ApiClient(host)

        params = client.createParams('aaaaa', 1, [1000, 2000])
        print(params)

    def test_post(self):
        http = '160.16.10.1'
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        conn = DB(host, db, user, password)
        client = ApiClient(host)

        params = client.createParams('aaaaa', 1, [1000, 2000])
        response = client.post(params)
        print(response)
        
        
        
