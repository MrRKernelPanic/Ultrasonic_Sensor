def reading (sensor):
	import time
	import RPi.GPIO as GPIO

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	if sensor == 0:
		GPIO.setup(23, GPIO.OUT)
		GPIO.setup(24, GPIO.IN)
		GPIO.output(23, GPIO.LOW)
		
		time.sleep(0.3)
		
		GPIO.output(23, True)
		time.sleep(0.00001)
		GPIO.output(23, False)
		
		while GPIO.input(24) == 0:
			signaloff = time.time()
	
		while GPIO.input(24) == 1:
			signalon = time.time()
		
		timepassed = signalon - signaloff
		
		distance = timepassed * 17000
		
		return distance
		
		GPIO.cleanup()

	else:
		print "Incorrect setup"

while True:
	print reading (0)
