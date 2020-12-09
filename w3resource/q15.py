#!/opt/anaconda/bin/python
## Question 15: Write a Python program to get the volume of a sphere with radius 6

## import build-in pkgs
import math

## main run part
r = float(input('Please input r: '))
print((4 * math.pi * (r ** 3)) / 3)
