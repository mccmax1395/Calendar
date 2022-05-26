# Raspberry Pi Zero W Calendar

This repository is for running a calendar app on a Raspberry Pi Zero W.  

## Setup
To Be able to use all of the functionality of this repository there are a few tools that need to be installed beforehand.  Run the following command:

```bash
sudo apt install xdotool
```

next there are a few files that need to be changed to reflect your user if you aren't using pi as your default or Clone  this repo at /home/pi/:
sensorCode.py: Lines 46 and 52
motionSensor.service: Line 8

to be able to run your motion sensor service, you must move it to the right folder.  In the Calendar directory run the following command:
```bash
sudo cp motionSensor.service /etc/systemd/system/motionSensor.service
```

You also must change the file permissions for motionSensor.py.  In the Calendar directory run the following command:
```bash
chmod 755 sensorCode.py
```

Finally you can start your service by running the following commands:
```bash
sudo systemctl daemon-reload
sudo systemctl start motionSensor.service
```
if you want your service to start up after a reboot, run this command:
```bash
 sudo systemctl enable motionSensor.service
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

