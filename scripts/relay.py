import time, os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
	gpioPin = int(sys.argv[1])
except:
	print 'false'
	sys.exit()

try:
	watering = int(sys.argv[2])
except:
	watering = 3

GPIO.setup(gpioPin, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(gpioPin, GPIO.LOW)
time.sleep(watering)
GPIO.output(gpioPin, GPIO.HIGH)

time.sleep(0.2)
print 'true'
