# Autonomous Target Robot

## Description
The objective of our project is to design an autonomous robot which functions as a target for long range target practice. Our design will communicate with the base station via cellular network, from which we connect to from base station’s virtual network. The base station will provide the operational boundary for which we will pull random GPS destinations, for which the robot will navigate to whilst positioning itself in the environment. At each destination, we will activate our turret to face the origin location and raise the target, counting the number of hits on target upon returning to its origin location.


## Contributors
Taylor Che: www.linkedin.com/in/taylor-che-655718117
 
Samuel Choi: https://www.linkedin.com/in/samuelkihongchoi

Francisco Munoz: https://www.linkedin.com/in/francisco-munoz

## Google Drive
https://drive.google.com/drive/folders/1mi6Ag-w6s8RqYlxPKCcS-EA4RBJQ7rSs

## Objectives
* GPS Boundary and Destination Mapping
* Autonomous GPS Navigation
* Implementation of Kalman Filter
* Targeting System
* Serial Communication (Raspberry Pi/ Arduino Uno)

## Parts List
* 1 - Raspberry Pi 3 Model B
* 1 - Arduino Uno
* 3 - L298N Motor Drivers
* 1 - Adafruit BNO055 Absolute Orientation Sensor
* 1 - BU-353-S4 USB GPS Receiver
* 1 - 11.1V Lithium Polymer (LiPo) Battery
* 1 - 7.2V Nickel-metal Hydride (NiMH) Battery
* 2 - NEMA-17 Stepper Motor
* 1 - Adafruit TB6612 Motor Driver
* 1 - SMAKN DC/DC Converter 12V Step Down  to 5V/3A Power Supply Module
* 1 - SW-420 Vibration Sensor

## Coding Languages
Python 2.7.13

C

## Environments
Raspbian GNU/Linux 9

Arduino Uno IDE

## Manual
When using this code, the directory before cloning must be /home/pi/Desktop/

All the directories used in the python code are set to this default directory and allows everything to communicate smoothly
```
git clone https://github.com/fmuno003/SeniorDesign
cd SeniorDesign
cd build
python demo.py
```

## Video 
https://youtu.be/rq3PR1blC0o
