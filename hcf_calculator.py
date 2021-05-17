# FUNCTION TO FIND HCF OF TWO NUMBERS

# define a function
def hcf_calculator(a, b):

# CHOOSE THE SMALLEST NUMBER USING IF ELSE CONDITIONAL STATEMENTS
    if a > b:
        smaller = b
    else:
        smaller = a
    for ii in range(1, smaller+1):
        if((a % ii == 0) and (b % ii == 0)):
            hcf = ii
    return hcf

#BY SREEKUMAR HARIDAS ON 17/05/2021