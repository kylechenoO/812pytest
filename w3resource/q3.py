#!/opt/anaconda/bin/python
## Question 3: Write a Python program to display the current date and time.

## import build-in pkgs
import time

## main run part
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
