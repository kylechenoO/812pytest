#!/opt/anaconda/bin/python
## Question 14: Write a Python program to calculate number of days between two dates.

## import build-in pkgs
import datetime

## main run part
dt1 = (2014, 7, 2)
dt2 = (2014, 7, 11)
print((datetime.date(dt2[0], dt2[1], dt2[2]) - datetime.date(dt1[0], dt1[1], dt1[2])).days)
