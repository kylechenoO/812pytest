#!/opt/anaconda/bin/python
## Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

## import build-in pkgs
import sys

## getProduct function
def getProduct(val1, val2):
    product_val = val1 * val2
    if product_val > 1000:
        return(val1 + val2)
    else:
        return(product_val)

## main run part
try:
    input_val1 = int(input('Please input val1: '))
    input_val2 = int(input('Please input val2: '))

except:
    print('Please input int values')
    sys.exit(-1)

print(getProduct(input_val1, input_val2))
