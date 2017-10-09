import RPi.GPIO as GPIO
import time
import json

class RelayBox():

    def __init__(self):
        l = [23, 25, 12, 16]
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for y in l:
            GPIO.setup(y, GPIO.OUT)
            GPIO.output(y, GPIO.HIGH)

    def run(self):
        while True:
            with open('/home/pi/RelayBox/status.json') as infile:
                data = json.load(infile)
            infile.close()
            self.ch1 = data["ch1"]
            self.ch2 = data["ch2"]
            self.ch3 = data["ch3"]
            self.ch4 = data["ch4"]
            if self.ch1 == True:
                GPIO.output(23, GPIO.LOW)
            else: GPIO.output(23, GPIO.HIGH)

            if self.ch2 == True:
                GPIO.output(25, GPIO.LOW)
            else: GPIO.output(25, GPIO.HIGH)

            if self.ch3 == True:
                GPIO.output(12, GPIO.LOW)
            else: GPIO.output(12, GPIO.HIGH)

            if self.ch4 == True:
                GPIO.output(16, GPIO.LOW)
            else: GPIO.output(16, GPIO.HIGH)
            time.sleep(.250)

if __name__ == "__main__":
    relayity = RelayBox()
    relayity.run()
