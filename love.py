#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time, random

x = [23, 24, 2, 4]
t = [4, 2, 24, 23]

class RelayBox():

  def __init__(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    for y in x:
      GPIO.setup(y, GPIO.OUT)
      GPIO.output(y, GPIO.HIGH)

  def mode1(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    w = rando2/rando1
    print("Mode 1, Time: ", w)
    for y in x:
      GPIO.output(y,GPIO.LOW)
    time.sleep(w) 
    self.checkSwitch()
    for y in x:
      GPIO.output(y,GPIO.HIGH)
    time.sleep(w)
    self.checkSwitch()

  def mode2(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    w = rando2/rando1
    print("Mode 2, Time: ", w)
    for y in x:
      GPIO.output(y,GPIO.LOW)
      time.sleep(w)
      self.checkSwitch()
    for y in x:
      GPIO.output(y,GPIO.HIGH)
      time.sleep(w)
      self.checkSwitch()

  def mode3(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    w = rando2/rando1
    print("Mode 3, Time: ", w)
    for y in x:
      GPIO.output(y,GPIO.LOW)
      time.sleep(w)
      self.checkSwitch()
    for y in t:
      GPIO.output(y,GPIO.HIGH)
      time.sleep(w)
      self.checkSwitch()

  def mode4(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    rando3 = random.randint(1,4)
    w = rando2/rando1
    for z in range(int(rando1)):
      s = random.choices(x, k=rando3)
      print("Mode 4, Time: ", w, "Set: ", s)
      for y in s:
        GPIO.output(y, GPIO.LOW)
      time.sleep(w)
      self.checkSwitch()
      for y in s:
        GPIO.output(y, GPIO.HIGH)
      time.sleep(w)
      self.checkSwitch()

  def mode5(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    w = rando2/rando1
    print("Mode 5, Time: ", w)
    for y in t:
      GPIO.output(y,GPIO.LOW)
      time.sleep(w)
      self.checkSwitch()
    for y in t:
      GPIO.output(y,GPIO.HIGH)
      time.sleep(w)
      self.checkSwitch()

  def mode6(self):
    rando1 = float(random.randint(1,5))
    rando2 = float(random.randint(1,2))
    w = rando2/rando1
    print("Mode 6, Time: ", w)
    for y in t:
      GPIO.output(y,GPIO.LOW)
      time.sleep(w)
      self.checkSwitch()
    for y in x:
      GPIO.output(y,GPIO.HIGH)
      time.sleep(w)
      self.checkSwitch()

  def off(self):
    for y in x:
      GPIO.output(y, GPIO.HIGH)
    
  def on(self):
    for y in x:
      GPIO.output(y, GPIO.LOW)
 
  def checkSwitch(self):
    if not GPIO.input(3): self.run()

  def run(self):
    while True:
      if not GPIO.input(3):
        self.on()
      else:
        self.off()
        z = random.randint(1,6)
        if z == 1: self.mode1()
        if z == 2: self.mode2()
        if z == 3: self.mode3()
        if z == 4: self.mode4()
        if z == 5: self.mode5()
        if z == 6: self.mode6()

if __name__ == "__main__":
    relayity = RelayBox()
    try:
      relayity.run()
    except:
      print("OOPS")
      relayity.off()
      GPIO.cleanup()
