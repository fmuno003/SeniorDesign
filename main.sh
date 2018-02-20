#!/bin/bash

import time
import serial

cd GUI
python gui.py
cd .. 
python RandNum.py
cd build
python demo.py

