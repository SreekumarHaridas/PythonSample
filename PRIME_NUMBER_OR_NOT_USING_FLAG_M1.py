# PYTHON CODE TO CHECK WEATHER AN ENTERED NUMBER IS PRIME OR NOT USING FLAG

# ACCEPT THE INTEGER NUMBER AS INPUT FROM USER
number = int(input("ENTER AN INTEGER NUMBER: "))

# INITIALLY SET A 'FLAG' VARIABLE TO 'FALSE'
FLAG = False

# PRIME NUMBERS ARE GREATER THAN 1/ 1 IS NOT A PRIME NUMBER
if number == 1:
    print(number, "IS NOT A PRIME NUMBER")

elif number > 1:
    # CHECKING FACTORS
    for ii in range(2, number):
        if (number % ii) == 0:
            # IF FACTOR IS FOUND THEN THE ENTERED NUMBER IS NOT PRIME, THEN SET THE 'FLAG' VARIABLE TO 'TRUE'
            FLAG = True
            # QUIT THE LOOP
            break

# CHECK THE FLAG IS TRUE OR FALSE USING IF ELSE
    if FLAG:
        print(number, "IS NOT A PRIME NUMBER")
    else:
        print(number, "IS A PRIME NUMBER")