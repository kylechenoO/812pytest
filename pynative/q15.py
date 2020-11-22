#!/opt/anaconda/bin/python
## Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

## import build-in pkgs
import math

def exponent(base, exp):
    return(math.pow(base, exp))

print(exponent(10, 3))
