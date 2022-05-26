#!/bin/bash
while true; #create an infinite loop
do
sleep 300 #refresh time in seconds so 1200 = every 20 min
export XAUTHORITY=/home/pi/.Xauthority; export DISPLAY=:0;xdotool key F5 & #you need to have xdotools installed
done
