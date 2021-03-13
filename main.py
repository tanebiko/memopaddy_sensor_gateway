import RPi.GPIO as GPIO
import time
import serial
import sys
import lcd_class
import os
from datetime import datetime
from apiClient import ApiClient
import configparser
import db
lcd = lcd_class.LCD()
OFF = 12
ini = configparser.ConfigParser()
ini.read('/home/pi/watergate/config.ini')
apiPath = ini['api']['sensordata']
print(apiPath)
dbHost = ini['mysql']['host']
dbName = ini['mysql']['db']
user = ini['mysql']['user']
passwd = ini['mysql']['passwd']

dbObj = db.DB(dbHost, dbName, user, passwd)

def sendData(code, id, values):
    client = ApiClient(apiPath)
    params = client.createParams(code, id, values)
    print(params)
    res = client.post(params)

def check(button):
    count = 0
    prev_status = not GPIO.input(button)

    while count < 3:
        time.sleep(0.01)
        status = not GPIO.input(button)
        if prev_status == status:
            count += 1
        else:
            prev_status = status
            count = 0
    return status

def switchDown(pin):
    GPIO.setmode(GPIO.BCM)
    for i in range(30):
        status = check(OFF)
        if status == False:
            break
        time.sleep(0.1)
    else:
        lcd.string("Shutdown", lcd.LINE_1)
        time.sleep(1)
        GPIO.remove_event_detect(OFF)
        GPIO.cleanup(OFF)
        lcd.clean()
        os.system("shutdown -h now")
        sys.exit()
            
GPIO.setmode(GPIO.BCM)
GPIO.setup(OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(OFF, GPIO.FALLING)
GPIO.add_event_callback(OFF, switchDown)

port = serial.Serial("/dev/ttyUSB0", 115200, timeout=10)

lcd.string("System started!!", lcd.LINE_1)
while True:
    try:
        line = port.readline()
        print(line)
        line = line.decode('utf8')
        d = line.split(";")
        
        if(len(d) == 13):
            print(len(d))
            print('receive')
            pid = d[5]
            sensorDao = db.SensorDao(dbObj)
            print('te')
            sensor = sensorDao.findByPid(pid)
            print(sensor.code)
            if(sensor != None):
                id = sensor.id
                code = sensor.code
                values = [d[9], d[10]]

                sendData(code, id, values)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
    except:
        continue
