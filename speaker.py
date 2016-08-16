
import time
import grovepi

# Connect the Grove LED to digital port D5
# SIG,NC,VCC,GND
port = 5

# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6

# Digital ports that do not support PWM
# D2, D4, D7, D8

notes = [1911,1702,1516,1431,1275,1136,1012]

grovepi.pinMode(port, "OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        # Reset
        if i >= len(notes):
            i = 0

        # Current frequency
        print (notes[i])

        # Give PWM output to port
        grovepi.analogWrite(port, notes[i])

        # Increment brightness for next iteration
        i = i + 1
        time.sleep(.5)

    except KeyboardInterrupt:
        grovepi.analogWrite(port, 0)
        break
    except IOError:
        print ("Error")