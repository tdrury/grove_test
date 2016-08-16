import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D3
# SIG,NC,VCC,GND
ultrasonic_ranger = 3

while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))

    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
