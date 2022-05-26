
import RPi.GPIO as GPIO

PIR_input = 4				#read PIR Output
#LED = 32				#LED for signalling motion detected	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN, GPIO.PUD_DOWN)	
#GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, GPIO.LOW)

while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        print("on")
    else:
        print("off")
