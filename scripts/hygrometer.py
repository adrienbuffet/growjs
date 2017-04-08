import time, os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if len(sys.argv) == 2:
	gpioPin = int(sys.argv[1])
	GPIO.setup(gpioPin, GPIO.IN)
	input = GPIO.input(gpioPin)
	if input:
		print('false')
	else:
		print('true')

