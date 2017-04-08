import time, os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if len(sys.argv) == 3:
	gpioPin = int(sys.argv[1])
	watering = int(sys.argv[2])
	GPIO.setup(gpioPin, GPIO.OUT, initial=GPIO.HIGH)

	GPIO.output(gpioPin, GPIO.LOW)
	time.sleep(watering)
	GPIO.output(gpioPin, GPIO.HIGH)

	time.sleep(0.2)
	print 'true'

elif len(sys.argv) == 2:
	gpioPin = int(sys.argv[1])
	GPIO.setup(gpioPin, GPIO.OUT, initial=GPIO.HIGH)

	GPIO.output(gpioPin, GPIO.LOW)
	time.sleep(3)
	GPIO.output(gpioPin, GPIO.HIGH)

	time.sleep(0.2)
	print 'true'

else:
	print 'false'
