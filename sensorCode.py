#import section
import RPi.GPIO as GPIO				#imports GPIO library to read motion sensor
import time					#imports time library to be able to set up timer
import os					#imports os library so program can run bash commands

#Variable declaration

#state variables
sensorState = 0					#sets sensor state to default of off
monitorState = 1  				#sets monitor state to default of on

#time variables
waitWhileOn = 1200				#sets turn off delay to 20 minutes (1200 seconds)
waitWhileOff = 10				#sets turn on delay to 10 seconds
waitTime = waitWhileOn				#sets wait time to  off delay
lastTime = ""					#sets time tracker to "".  This is used to consolidate  timer count when program is run from command line

#GPIO variables
PirInput = 4					#sets signal pin for sensor
GPIO.setwarnings(False) 			#turns  warnings off
GPIO.setmode(GPIO.BCM)				#sets mode to BCM
GPIO.setup(pirInput, GPIO.IN, GPIO.PUD_DOWN)	#sets up GPIO input


#runs until stopped
while True:
    #Set these local variables every loop
    sensorState= GPIO.input(pirInput)
    startTime = time.time()
    #while loop only executes when sensor stat doesn't match monitor state 
    while sensorState != monitorState:
     #keeps track of how long has lapsed 
     lapsedTime = time.time()-startTime
     timeLeft = round(waitTime-lapsedTime)
     #prints out new time in secondsif it has changes (10,9,8...)
     if(timeLeft != lastTime):
      print("currently waiting for time to change, time left: " + str(timeLeft))
      lastTime = timeLeft
     #only runs if declared wait time has passed
     if (lapsedTime > waitTime):
      print("Changing State.")
      #turns monitor on if it is off
      if(monitorState == 0):
       monitorState = 1
       print("Turning monitor on")
       os.system("sudo sh /home/pi/Calendar/rpi-hdmi.sh on")
       waitTime = waitWhileOn
      #turns monitor off if it is on
      else:
       monitorState = 0
       print("Turning monitor off")
       os.system("sudo sh /home/pi/Calendar/rpi-hdmi.sh off")
       waitTime = waitWhileOff

