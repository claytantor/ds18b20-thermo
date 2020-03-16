import RPi.GPIO as GPIO
import sys
import os
import time

from w1thermsensor import W1ThermSensor

def main(argv):
    print("starting thermo control app.")

    sensor = W1ThermSensor()
    while True:
        temp_all = sensor.get_temperatures([
            W1ThermSensor.DEGREES_C,
            W1ThermSensor.DEGREES_F,
            W1ThermSensor.KELVIN])   
        print(f'F -> {str(round(temp_all[1], 2))}')
        time.sleep(5)

if __name__ == "__main__":
    main(sys.argv[1:])
