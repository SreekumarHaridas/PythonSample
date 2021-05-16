#THIS CODE COVERT KILOMETER TO MILES OR VICE VERSA ACCORDING TO THE OPTION ENTERED
SELECT = int(input("WHICH CONVERSION DO YOU WANT TO PERFORM: \n FOR KILOMETER TO MILE (enter 1) \n FOR MILE TO KILOMETER  (enter 2)   : "))
# conversion factor
conv_fac = 0.621371

# IF OPTED FOR 1, THE FOLLOWING REGION WORKS
if SELECT == 1 :

    # Taking kilometers input from the user
    kilometers = float(input("Enter value in kilometers: "))
    # calculate miles
    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
# IF OPTED FOR 2, THE FOLLOWING REGION WORKS
elif SELECT == 2 :
    # Taking miles input from the user
    miles = float(input("Enter value in miles: "))
    # calculate kilometers
    kilometers = miles / conv_fac
    print('%0.2f miles is equal to %0.2f kilometers' %(miles,kilometers))
else:
    print ("The entered option is invalid please select a valid option")
