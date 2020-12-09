#!/opt/anaconda/bin/python
## Question 10: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

## import build-in pkgs

## main run part
inputStr = input('Please input an int: ')
val1 = int(inputStr)
val2 = int(inputStr * 2)
val3 = int(inputStr * 3)
print('val1: {}'.format(val1))
print('val2: {}'.format(val2))
print('val3: {}'.format(val3))
print('sum: {}'.format(val1 + val2 + val3))
