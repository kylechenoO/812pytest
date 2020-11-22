#!/opt/anaconda/bin/python
## Question 13: Print multiplication table form 1 to 10
import sys

for i in range(1, 11):
    for j in range(1, 11):
        ## print('{} '.format(i * j), end = " ")
        sys.stdout.write('{} '.format(i * j))

    ## print('\n')
    sys.stdout.write('\n')
    sys.stdout.flush()

