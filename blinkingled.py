import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
 GPIO.output(22, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(16, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
 break
