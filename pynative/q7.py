#!/opt/anaconda/bin/python
## Question 7: Return the total count of sub-string “Emma” appears in the given string

def getTimesParm(inputStr, parmStr):
    return(inputStr.count(parmStr))

print(getTimesParm('Hello world, hello, Hello', 'Hello'))
