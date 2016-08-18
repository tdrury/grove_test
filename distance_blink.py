

import time
import grovepi

# Connect the Grove LED to digital port D4
led = 4
ultrasonic_ranger = 3


grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)
    if (distance > 10) and (distance < 100):
        grovepi.digitalWrite(led,1)		# Send HIGH to switch on LED
        print ("LED ON!")
    else:
        grovepi.digitalWrite(led,0)		# Send LOW to switch off LED
        print ("LED OFF!")

