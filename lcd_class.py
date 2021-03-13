import RPi.GPIO as GPIO
import time

class LCD:
    RS = 7
    E = 8
    D4 = 25
    D5 = 24
    D6 = 23
    D7 = 18
    WIDTH = 16
    CHR = True
    CMD = False
    LINE_1 = 0x80
    LINE_2 = 0xC0
    PULSE = 0.0005
    DELAY = 0.0005

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.E, GPIO.OUT)
        GPIO.setup(self.D4, GPIO.OUT)
        GPIO.setup(self.D5, GPIO.OUT)
        GPIO.setup(self.D6, GPIO.OUT)
        GPIO.setup(self.D7, GPIO.OUT)

        self.byte(0x33, self.CMD)
        self.byte(0x32, self.CMD)
        self.byte(0x06, self.CMD)
        self.byte(0x0C, self.CMD)
        self.byte(0x28, self.CMD)
        self.byte(0x01, self.CMD)
        time.sleep(self.DELAY)

    def byte(self, bits, mode):
        GPIO.output(self.RS, mode)
        GPIO.output(self.D4, False)
        GPIO.output(self.D5, False)
        GPIO.output(self.D6, False)
        GPIO.output(self.D7, False)
        if bits&0x10==0x10:
            GPIO.output(self.D4, True)
        if bits&0x20==0x20:
            GPIO.output(self.D5, True)
        if bits&0x40==0x40:
            GPIO.output(self.D6, True)
        if bits&0x80==0x80:
            GPIO.output(self.D7, True)

        self.toggle_enable()

        GPIO.output(self.D4, False)
        GPIO.output(self.D5, False)
        GPIO.output(self.D6, False)
        GPIO.output(self.D7, False)
        if bits&0x01==0x01:
            GPIO.output(self.D4, True)
        if bits&0x02==0x02:
            GPIO.output(self.D5, True)
        if bits&0x04==0x04:
            GPIO.output(self.D6, True)
        if bits&0x08==0x08:
            GPIO.output(self.D7, True)

        self.toggle_enable()

    def toggle_enable(self):
        time.sleep(self.DELAY)
        GPIO.output(self.E, True)
        time.sleep(self.PULSE)
        GPIO.output(self.E, False)
        time.sleep(self.DELAY)

    def string(self, message, line):
        message = message.ljust(self.WIDTH, " ")
        self.byte(line, self.CMD)
        for i in range(self.WIDTH):
            self.byte(ord(message[i]), self.CHR)
            

    def clean(self):
        GPIO.cleanup(self.RS)
        GPIO.cleanup(self.E)
        GPIO.cleanup(self.D4)
        GPIO.cleanup(self.D5)
        GPIO.cleanup(self.D6)
        GPIO.cleanup(self.D7)
