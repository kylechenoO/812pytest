#!/opt/anaconda/bin/python
## Question 9: Reverse a given number and return true if it is the same as the original number

def compareWithReverse(inputVal):
    return(str(inputVal) == str(inputVal)[::-1])

print(compareWithReverse(122221))
