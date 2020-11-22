#!/opt/anaconda/bin/python
## Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

def getResult(inputList1, inputList2):
    return([ val for val in inputList1 if val % 2 != 0 ] + [ val for val in inputList2 if val % 2 == 0 ])

print(getResult([1, 2, 3, 4], [5, 6, 7, 8]))
