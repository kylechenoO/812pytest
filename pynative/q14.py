#!/opt/anaconda/bin/python
## Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)

def getHalfPyramid(size):
    for i in range(size):
        print('*' * (size - i))

getHalfPyramid(5)
