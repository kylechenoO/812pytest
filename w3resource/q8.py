#!/opt/anaconda/bin/python
## Question 8: Write a Python program to display the first and last colors from the following list.

## import build-in pkgs
import re

## main run part
inputStr = input('Please input a list split with blank: ')
inputList = re.split(' ', inputStr)
print('1st item: {}'.format(inputList[0]))
print('last item: {}'.format(inputList[-1]))
