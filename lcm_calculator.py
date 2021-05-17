# FUNCTION TO FIND LCM OF TWO NUMBERS

# define a function
def lcm_calculator(a, b):
   # CHOOSE THE GREATER NUMBER USING IF ELSE CONDITIONAL STATEMENTS
   if a > b:
       greater = a
   else:
       greater = b

   while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


#BY SREEKUMAR HARIDAS ON 17/05/2021
