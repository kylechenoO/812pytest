#!/opt/anaconda/bin/python
## Question 11: Write a code to extract each digit from an integer, in the reverse order

## import build-in pkgs
import re

def getReverse(inputVal):
    return(re.sub(r'^ | $', '', re.sub('', ' ', str(inputVal)[::-1])))

print(getReverse(19378))
