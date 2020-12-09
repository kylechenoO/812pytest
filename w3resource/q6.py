#!/opt/anaconda/bin/python
## Question 6: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

## import build-in pkgs
import re

## main run part
inputStr = input('Please input some numbers split with "," :')
numList = re.split(',', inputStr)
print(numList)
print(tuple(numList))
