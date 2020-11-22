#!/opt/anaconda/bin/python
## Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
import numpy as np

def getDivisibleFive(inputList):
    return([ val for val in inputList if val % 5 == 0 ])

print(getDivisibleFive([1, 2, 3, 4, 5, 11, 25, 666, 100]))
