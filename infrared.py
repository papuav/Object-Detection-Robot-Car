# This module is for the infrared
# To create the object:
# var_name = Infrared(pin)
# 
#

import RPi.GPIO as GPIO
import time
import sys

class Infrared:
    def __init__(self, pin):
        self.pin = pin
        self.setup()
    
    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN)
        
    def check(self):
        while True:
            if GPIO.input(self.pin) == 0:
                return True
                

def main():
    infrared = Infrared(11)
    isThere = infrared.check()
    print(isThere)
    print("done")

if __name__ == "__main__":
    main()
