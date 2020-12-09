#!/opt/anaconda/bin/python
## Question 7: Write a Python program to accept a filename from the user and print the extension of that.

## import build-in pkgs
import re

## main run part
inputStr = input('Please input a file name: ')
print(re.sub('^.*\.', '', inputStr))
