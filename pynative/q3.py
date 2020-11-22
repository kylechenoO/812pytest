#!/opt/anaconda/bin/python
## Question 3: Given a string, display only those characters which are present at an even index number.

def getEvenVal(inputStr):
    return([ inputStr[i] for i in range(0, len(inputStr), 2) ])

print(getEvenVal('ABC'))
