# PYTHON CODE TO CHECK WEATHER AN ENTERED NUMBER IS PRIME OR NOT
# ACCEPT THE INTEGER NUMBER AS INPUT FROM USER
number = int(input("ENTER AN INTEGER NUMBER: "))

# PRIME NUMBERS ARE GREATER THAN 1/ 1 IS NOT A PRIME NUMBER
if number > 1:
    # CHECKING FACTORS
    for ii in range(2, number):
        if (number % ii) == 0:
            print(number, "IS NOT A PRIME NUMBER BECAUSE")
            print(ii, "TIMES", number // ii, "IS", number)
            print("BY DEFINITION PRIME NUMBERS ARE POSITIVE INTEGERS HAVING ONLY TWO FACTORS, 1 AND THE INTEGER ITSELF")
            # QUIT THE LOOP
            break
    else:
        print(number, "IS A PRIME NUMBER")
else:
    print(number, "IS NOT A PRIME NUMBER")