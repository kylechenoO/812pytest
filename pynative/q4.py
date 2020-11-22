#!/opt/anaconda/bin/python
## Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def getNewString(inputStr, n):
    return(inputStr[n:])

print(getNewString('ABCDEFG', 3))
