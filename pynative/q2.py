#!/opt/anaconda/bin/python
## Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

def getSum(intVal):
    result = 0
    for i in range(intVal):
        preVal = 0 if i == 0 else i - 1
        result = preVal + i
        print('Current Number {} Previous Number {} Sum: {}'.format(i, preVal, result))

getSum(10)
