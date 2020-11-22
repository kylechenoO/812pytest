#!/opt/anaconda/bin/python
## Question 12: Calculate income tax for the given income by adhering to the below rules

def getTax(income):
    if income <= 10000:
        return(0)

    elif income <= 20000:
        return((income - 10000) * 0.1)

    else:
        return(10000 * 0.1 + (income - 20000) * 0.2)

print(getTax(45000))
