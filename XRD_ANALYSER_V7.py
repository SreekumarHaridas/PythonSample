# THIS IS A PYTHON PROGRAM TO FIND THE LATTICE PARAMETERS OF SEVEN CRYSTAL SYSTEMS USING THE OUTPUTS OBTAINED FROM XRD MACHINE

import math
#from run import *   # run.py FUNCTION IS CREATED BY SREEKUMAR HARIDAS FOR REPEATEDLY RUN PYTHON CODES AFTER COMPLETION
#----------------------------------SECTION 1--USER INPUTS---------------------------------------------------------------
input_log = {}
H = int(input("PLEASE ENTER THE h VALUE (E.G 2)  : "))
K = int(input("PLEASE ENTER THE k VALUE (E.G 0)  : "))
L = int(input("PLEASE ENTER THE l VALUE (E.G 1)  : "))
wave_length = float(input("PLEASE ENTER THE WAVE LENGTH OF THE X RAY IN ANGSTROM UNIT  (E.G 1.5406 Å):  "))
peak_position1 = float(input("PLEASE ENTER THE PEAK POSITION ANGLE IN DEGREE (2 THETA):     "))
order = int(input("PLEASE ENTER THE ORDER OF DIFFRACTION (E.G 1) : "))
#----------------------------------SECTION 1--USER INPUTS OVER----------------------------------------------------------
#----------------------------------SECTION 2----------------------------------------------------------------------------
#-------------------CALCULATION OF INTER PLANAR SPACING-----------------------------------------------------------------
#-------------------------------STARTING--------------------------------------------------------------------------------
d1 = order*wave_length #NUMERATOR OF THE BRAGG'S EQUATION
peak_position2 = (peak_position1*math.pi)/180.0 # CONVERTING ANGLE IN DEGREE TO RADIAN
peak_position = peak_position2/2
d2 = 2*math.sin(peak_position) #DENOMINATOR OF THE BRAGG'S EQUATION
d = d1/d2 #THE BRAGG'S EQUATION, d IS IN ANGSTROM UNIT
dd = d**2
onebydd = 1/dd
print("\n THE INTER PLANAR SPACING 'd' IS", d)
#----------------CALCULATION OF INTER PLANAR SPACING IS OVER------------------------------------------------------------
#-----------------------------------SECTION 2---------------------------------------------------------------------------
while True:
    CRYSTAL_SYSTEM = input("PLEASE SELECT THE CRYSTAL SYSTEM (ENTER YOUR CHOICE: 1. CUBIC/ 2. TETRAGONAL/ 3. HEXAGONAL\n4.RHOMBOHEDRAL/5.ORTHORHOMBIC/6. MONOCLINIC/7. TRICLINIC):")

# ----------------------------------SECTION 1A---SAVING OF ENTERED PARAMETERS-------------------------------------------
    for variable in ["H", "K", "L", "wave_length", "peak_position1", "order", "CRYSTAL_SYSTEM"]:
        input_log[variable] = eval(variable)
    with open("INPUT_LOG_XRD_ANALYSER_V7.txt", 'w') as f:
        str_input_log = repr(input_log)
        f.write("input_log = " + str_input_log + "\n")
    # ----------------------------------SECTION 1A---SAVING OF ENTERED PARAMETERS IS OVER-------------------------------
    # ----------------------------------SECTION 3-----------------------------------------------------------------------
    if CRYSTAL_SYSTEM in ('1', '2', '3', '4', '5', '6', '7'):
        #----------------------------------SECTION 3A-------------------------------------------------------------------
        if CRYSTAL_SYSTEM == '1':       # CUBIC
            name = 'CUBIC'
            namee = 'cubic'
            a = d*(math.sqrt((H**2 + K**2 + L**2)))
            print("\nTHE LATTICE PARAMETER 'a' FOR THE '", name, "' CRYSTAL SYSTEM IS : ", a)
        #----------------------------------SECTION 3A-------------------------------------------------------------------
        #----------------------------------SECTION 3B-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '2':  #TETRAGONAL
            name = 'TETRAGONAL'
            namee = 'tetragonal'
            while True:
                SELECT = input("WHICH LATTICE PARAMETER YOU WANT TO FIND FIRST ? a/c: ")
                if SELECT in ('a', 'A', 'c', 'C'):
                    if SELECT == 'A' or SELECT == 'a':
                        h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2)  : "))
                        k1 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 1)  : "))
                        a = d*(math.sqrt((h1**2+k1**2)))
                        print("\nLATTICE PARAMETER 'a' FOR THE '", name,"'CRYSTAL SYSTEM IS : ", a)
                        l1 = int(input("\nPLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'c'(E.G 1)  : "))
                        c = d*l1
                        print("\nLATTICE PARAMETER 'c' FOR THE '", name,"'CRYSTAL SYSTEM IS : ", c)
                    elif SELECT == 'C' or SELECT == 'c':
                        l1 = int(input("\nPLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'c'(E.G 1)  : "))
                        c = d*l1
                        print("\nLATTICE PARAMETER 'c' FOR THE '", name,"'CRYSTAL SYSTEM IS : ", c)
                        h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2)  : "))
                        k1 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 1)  : "))
                        a = d*(math.sqrt((h1**2+k1**2)))
                        print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
                    break
                else:
                    print("\nSORRY THE ENTERED LATTICE PARAMETER DOES NOT MATCH WITH AVAILABLE ,PLEASE TRY WITH VALID PARAMETER a/c")
        #----------------------------------SECTION 3B-------------------------------------------------------------------
        #----------------------------------SECTION 3C-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '3':  # HEXAGONAL
            name = 'HEXAGONAL'
            namee = 'hexagonal'
            while True:
                SELECT = input("WHICH LATTICE PARAMETER YOU WANT TO FIND FIRST ? a/c: ")
                if SELECT in ('a', 'A', 'c', 'C'):
                    if SELECT == 'A' or SELECT == 'a':
                        h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2)  : "))
                        k1 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 1)  : "))
                        aaa = h1**2+(h1*k1)+k1**2
                        aa = (4/3)*aaa
                        a = d*aa
                        print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
                        l1 = int(input("\nPLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'c'(E.G 1)  : "))
                        c = d*l1
                        print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
                    elif SELECT == 'C' or SELECT == 'c':
                        l1 = int(input("\nPLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'c'(E.G 1)  : "))
                        c = d*l1
                        print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
                        h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2)  : "))
                        k1 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 1)  : "))
                        aaa = h1**2+(h1*k1)+k1**2
                        aa = (4/3)*aaa
                        a = d*aa
                        print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
                    break
                else:
                    print("\nSORRY THE ENTERED LATTICE PARAMETER DOES NOT MATCH WITH AVAILABLE ,PLEASE TRY WITH VALID PARAMETER a/c")
        #----------------------------------SECTION 3C-------------------------------------------------------------------
        #----------------------------------SECTION 3D-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '4':  # RHOMBOHEDRAL
            name = 'RHOMBOHEDRAL'
            namee = 'rhombohedral'
            ALPHA1 = float(input("\nPLEASE ENTER THE ALPHA ANGLE IN IN DEGREE : "))
            ALPHA = (ALPHA1*math.pi)/180.0 # CONVERTING ANGLE IN DEGREE TO RADIAN
            aaaaa = (H**2+K**2+L**2)*((math.sin(ALPHA))**2)
            aaaa = 2*((H*K)+(K*L)+(H*L))*((math.cos(ALPHA))**2-math.cos(ALPHA))
            aaa = aaaaa+aaaa
            aa = aaa/(1-(3*(math.cos(ALPHA))**2)+(2*(math.cos(ALPHA))**3))
            a = d*math.sqrt(aa)
            print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
        #----------------------------------SECTION 3D-------------------------------------------------------------------
        #----------------------------------SECTION 3E-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '5':   # ORTHORHOMBIC
            name = 'ORTHORHOMBIC'
            namee = 'orthorhombic'
            print("\nSINCE YOU ARE OPTED FOR'", name,"' CRYSTAL SYSTEM, WE FIRST FIND PARAMETER 'a'")
            print("\nCHOOSE A MILLER INDICES WITH k AND l VALUES ARE ZERO (E.G 200)")
            h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2) : "))
            a = d*h1
            print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
            print("\nNOW WE ARE GOING TO FIND THE PARAMETER 'c' FOR '", name,"'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES WITH h AND k VALUES ARE ZERO (E.G 004)")
            l1 = int(input('PLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF "c"(E.G 4)  :     '))
            c = d*l1
            print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
            print("\nNOW WE ARE GOING TO FIND PARAMETER 'b' FOR '", name, "'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES, THAT DEFINITELY CONTAINS k (E.G 220)")
            h2 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 2)  : "))
            k2 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 2)  : "))
            l2 = int(input("\nPLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 0)  : "))
            try:
                cc1 = (h2**2)/(a**2)
                cc2 = (l2**2)/(c**2)
                cc3 = cc1+cc2
                cc = onebydd-cc3
                b = k2/(math.sqrt(cc))
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", b)
            except ZeroDivisionError:
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS OBTAINED AS INFINITY!!!!-")
        #----------------------------------SECTION 3E-------------------------------------------------------------------
        #----------------------------------SECTION 3F-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '6':  # MONOCLINIC
            name = 'MONOCLINIC'
            namee = 'monoclinic'
            print("\nSINCE YOU ARE OPTED FOR'", name, "' CRYSTAL SYSTEM, WE FIRST FIND PARAMETER 'a'")
            print("\nCHOOSE A MILLER INDICES WITH k AND l VALUES ARE ZERO (E.G 200)")
            h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2) : "))
            BETTA1 = float(input("\nPLEASE ENTER THE BETTA ANGLE IN IN DEGREE : "))
            BETTA = (BETTA1*math.pi)/180.0  # CONVERTING ANGLE IN DEGREE TO RADIAN
            aa = d*h1
            a = aa/math.sin(BETTA)
            print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
            print("\nNOW WE ARE GOING TO FIND PARAMETER 'b' FOR '", name, "'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES, THAT DEFINITELY CONTAINS k AND NOT CONTAINS l (E.G 220)")
            h2 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 2)  : "))
            k2 = int(input("\nPLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 2)  : "))
            try:
                bbbbb = (math.sin(BETTA)) ** 2 / d ** 2
                bbbb = h2 ** 2 / a ** 2
                bbb = bbbbb - bbbb
                bb = (k2 ** 2) * (math.sin(BETTA)) ** 2
                bb2 = bb / bbb
                b = math.sqrt(bb2)
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", b)
            except ZeroDivisionError:
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS OBTAINED AS INFINITY!!!!-")
            print("\nNOW WE ARE GOING TO FIND THE PARAMETER 'c' FOR '", name, "'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES WITH NON ZERO l VALUE (E.G 211)")
            h3 = int(input('PLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF "c"(E.G 2)  :     '))
            k3 = int(input('PLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF "c"(E.G 1)  :     '))
            l3 = int(input('PLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF "c"(E.G 1)  :     '))
            c7 = (math.sin(BETTA))**2/d**2
            c6 = h3**2/a**2
            c5 = ((k3**2)*(math.sin(BETTA))**2)/(b**2)
            c4 = c6+c5
            c3 = c7-c4
            if h3 == 0:
                c2 = l3**2/c3
                c = math.sqrt(c2)
                print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
            else:
                co1 = l3**2    # COEFFICIENT 1
                co2 = -(2*h3*l3*math.cos(BETTA))/a  # COEFFICIENT 2
                co3 = -c3    # COEFFICIENT 3
                delta = (co2**2)-(4*co1*co3)
                if delta < 0:
                    print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS NOT A REAL NUMBER ")
                elif delta == 0:
                    c1 = -(co2/(2*co1))
                    c = 1/c1
                    print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
                else:
                    c11 = (-co2+math.sqrt(delta))/(2*co1)
                    c12 = (-co2-math.sqrt(delta))/(2*co1)
                    ca = 1/c11
                    cb = 1/c12
                    print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", ca, "OR", cb)
        #----------------------------------SECTION 3F-------------------------------------------------------------------
        # ----------------------------------SECTION 3G-------------------------------------------------------------------
        elif CRYSTAL_SYSTEM == '7':  # TRICLINIC
            name = 'TRICLINIC'
            namee = 'triclinic'
            ALPHA1 = float(input("\nPLEASE ENTER THE ALPHA ANGLE IN IN DEGREE : "))
            BETTA1 = float(input("\nPLEASE ENTER THE BETTA ANGLE IN IN DEGREE : "))
            GAMA1 = float(input("\nPLEASE ENTER THE GAMA ANGLE IN IN DEGREE : "))
            ALPHA = (ALPHA1*math.pi)/180.0  # CONVERTING ANGLE IN DEGREE TO RADIAN
            BETTA = (BETTA1*math.pi)/180.0  # CONVERTING ANGLE IN DEGREE TO RADIAN
            GAMA = (GAMA1*math.pi)/180.0  # CONVERTING ANGLE IN DEGREE TO RADIAN
            dr = 1-(math.cos(ALPHA)**2)-(math.cos(BETTA)**2)-(math.cos(GAMA)**2)+(2*(math.cos(ALPHA))*(math.cos(BETTA))*(math.cos(GAMA)))
            lhs = dr/dd
            print("\nSINCE YOU ARE OPTED FOR'", name, "' CRYSTAL SYSTEM, WE FIRST FIND PARAMETER 'a'")
            print("\nCHOOSE A MILLER INDICES WITH k AND l VALUES ARE ZERO (E.G 200)")
            h1 = int(input("\nPLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'a'(E.G 2) : "))
            a2 = d*h1*math.sin(ALPHA)
            a = a2/(math.sqrt(dr))
            print("\nLATTICE PARAMETER 'a' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", a)
            print("\nNOW WE ARE GOING TO FIND PARAMETER 'c' FOR '", name, "'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES WITH h AND k VALUES ARE ZERO (E.G 004)")
            l2 = int(input('PLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF "c"(E.G 4)  :     '))
            c2 = d*l2*math.sin(GAMA)
            c = c2/(math.sqrt(dr))
            print("\nLATTICE PARAMETER 'c' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", c)
            print("\nNOW WE ARE GOING TO FIND PARAMETER 'b' FOR '", name, "'CRYSTAL SYSTEM")
            print("\nCHOOSE A MILLER INDICES WITH NON ZERO k VALUE (E.G 211)")
            h3 = int(input("PLEASE ENTER THE h VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 2)  : "))
            k3 = int(input("PLEASE ENTER THE k VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 1)  : "))
            l3 = int(input("PLEASE ENTER THE l VALUE OF THE PEAK CHOSEN FOR CALCULATION OF 'b'(E.G 1)  : "))
            b10 = (h3**2*(math.sin(ALPHA)**2))/a**2
            b9 = (l3**2*(math.sin(GAMA)**2))/c**2
            b8 = (2*h3*l3*((math.cos(GAMA)*math.cos(ALPHA))-math.cos(BETTA)))/(a*c)
            lhs2 = lhs-(b10+b9+b8)
            rhs1 = k3**2*(math.sin(BETTA)**2)
            rhs2 = ((2*k3*l3*((math.cos(GAMA)*math.cos(BETTA))-math.cos(ALPHA)))/c)+((2*h3*k3*((math.cos(ALPHA)*math.cos(BETTA))-math.cos(GAMA)))/a)
            co1 = rhs1     # COEFFICIENT 1
            co2 = rhs2     # COEFFICIENT 2
            co3 = -lhs2    # COEFFICIENT 3
            delta = (co2**2)-(4*co1*co3)
            if delta < 0:
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS NOT A REAL NUMBER ")
            elif delta == 0:
                b1 = -(co2/(2*co1))
                b = 1/b1
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", b)
            else:
                c11 = (-co2+math.sqrt(delta))/(2*co1)
                c12 = (-co2-math.sqrt(delta))/(2*co1)
                ba = 1/c11
                bb = 1/c12
                print("\nLATTICE PARAMETER 'b' FOR THE '", name, "'CRYSTAL SYSTEM IS : ", ba, "OR", bb)
        # ----------------------------------SECTION 3G-------------------------------------------------------------------
        break
    else:
        print("\nSORRY ENTERED CODE DOES NOT MATCH WITH AVAILABLE CRYSTAL SYSTEM,PLEASE TRY WITH VALID CODE IN THE INSTRUCTIONS")
        #-----------------------------CRYSTAL SYSTEMS SELECTION IS OVER-------------------------------------------------
    #--------------------------------------SECTION 3--------------------------------------------------------------------
#---------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
#-------------------------------------------ON 20-05-2021---------------------------SREEKUMAR HARIDAS-------------------
