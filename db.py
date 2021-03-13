import MySQLdb

class DB:
  def __init__(self, host, db, user, passwd):
    self.conn = MySQLdb.connect(host=host,db=db,user=user,passwd=passwd,charset="utf8")
    self.cursor = self.conn.cursor()

  def close(self):
    self.cursor.close()
    self.conn.close

class Sensor:
  def __init__(self, values):
    self.code = values[0]
    self.id = values[1]
    self.pid = values[2]

class SensorDao:
  def __init__(self, db):
    self.db = db
  def insert(self, sensor):
    self.db.cursor.execute("INSERT INTO sensors VALUES(%s, %s, %s)", (sensor.code, sensor.id, sensor.pid))
    self.db.conn.commit()
  def update(self, sensor):
    self.db.cursor.execute("UPDATE sensors SET code=%s, id=%s, pid=%s", (sensor.code, sensor.id, sensor.pid))
    self.db.conn.commit()
  def findByPid(self, pid):
    print(pid)
    self.db.cursor.execute("SELECT code, id, pid FROM sensors WHERE pid=%s", (pid,))
    if(self.db.cursor.rowcount == 0):
      return None
    model = Sensor(self.db.cursor.fetchone())
    return model
  def delete(self, code, id):
    self.db.cursor.execute("DELETE FROM sensors WHERE code=%s and id=%d", (code, id))
    self.db.conn.commit
