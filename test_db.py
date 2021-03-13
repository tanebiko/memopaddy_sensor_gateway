import unittest
from db import DB
from db import Sensor
from db import SensorDao

class TestDB(unittest.TestCase):
    def tearDown(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        dbo = DB(host, db, user, password)
        dbo.cursor.execute("TRUNCATE sensors");
        
    def test_init(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        db = DB(host, db, user, password)
        self.assertIsNotNone(db)

    def test_initDao(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        dbo = DB(host, db, user, password)
        dao = SensorDao(dbo)
        self.assertIsNotNone(dao)

    def test_insert(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        dbo = DB(host, db, user, password)
        dao = SensorDao(dbo)

        sensor = Sensor(['aaaaa', 1, 'hahaha'])
        dao.insert(sensor)

    def test_update(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        dbo = DB(host, db, user, password)
        dao = SensorDao(dbo)
        sensor = Sensor(['aaaaa', 1, 'hahaha'])
        dao.insert(sensor)
        sensor = Sensor(['aaaaa', 1, 'hahaha'])
        dao.update(sensor)

    def test_findByPid(self):
        host = 'localhost'
        db = 'watergate'
        user = 'root'
        password = 'raspberrypimysql556'
        dbo = DB(host, db, user, password)
        dao = SensorDao(dbo)
        sensor = Sensor(['aaaaa', 1, 'hahaha'])
        dao.insert(sensor)
        sensor = dao.findByPid('hahaha')
        self.assertEqual(sensor.id, 1)
        
