#!/opt/anaconda/bin/python
## Question 4: Write a Python program which accepts the radius of a circle from the user and compute the area.

## import build-in pkgs
import math

## main run part
try:
    r = float(input('Please input r: '))
    print(math.pi * r ** 2)

except Exception as e:
    print('ERROR: {}'.format(e))
