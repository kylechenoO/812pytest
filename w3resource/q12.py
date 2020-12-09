#!/opt/anaconda/bin/python
## Question 12: Write a Python program to print the calendar of a given month and year.

## import build-in pkgs
import calendar

## main run part
inputMonth = int(input('Please input the month: '))
inputYear = int(input('Please input the year: '))
print(calendar.month(inputYear, inputMonth))
