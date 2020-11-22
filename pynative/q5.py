#!/opt/anaconda/bin/python
## Question 5: Given a list of numbers, return True if first and last number of a list is same

def getSameFirstAndLast(inputList):
    return( True if inputList[0] == inputList[-1] else False)

print(getSameFirstAndLast([1, 2, 3, 4, 1]))
