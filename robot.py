import RPi.GPIO as GPIO
import time

global distance
trigger = 11
echo = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#Creating a function to handle using the Ultrasonic sensor, as it is a little trickier to use.
def ultra(sensor):
    global distance
    if sensor == 0:

        time.sleep(0.3)

        GPIO.output(trigger, True)

        time.sleep(0.00001)
        GPIO.output(trigger, False)
        while GPIO.input(echo) == 0:
          signaloff = time.time()
        while GPIO.input(echo) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff

        distance = timepassed * 17000
        
        return distance

    else:
        print "Error."

def forward():
	GPIO.output(17,1)
	GPIO.output(23,1)
	time.sleep(1)
	GPIO.output(17,0)
	GPIO.output(23,0)

def reverse():
	GPIO.output(18,1)
	GPIO.output(22,1)
	time.sleep(1)
	GPIO.output(18,0)
	GPIO.output(22,0)

def left():
	GPIO.output(17,0)
	GPIO.output(18,1)
	GPIO.output(22,0)
	GPIO.output(23,1)
	time.sleep(1)
	GPIO.output(17,0)
	GPIO.output(18,0)
	GPIO.output(22,0)
	GPIO.output(23,0)	

def right():
	GPIO.output(17,1)
	GPIO.output(18,0)
	GPIO.output(22,1)
	GPIO.output(23,0)
	time.sleep(1)
	GPIO.output(17,0)
	GPIO.output(18,0)
	GPIO.output(22,0)
	GPIO.output(23,0)

def stop():
	GPIO.output(17,0)
	GPIO.output(18,0)
	GPIO.output(22,0)
	GPIO.output(23,0)

while True:
	ultra(0)
	if distance > 10:
		forward()
	elif distance < 10:
		right()

