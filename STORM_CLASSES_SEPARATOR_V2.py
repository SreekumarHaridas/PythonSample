# THIS IS A SIMPLE PYTHON PROGRAM WHICH CLASSIFY THE STORMS IF PRESENT, BASED ON SYM-H VALUE AND SAVE THE DATES IN A CSV
# FILE IN THE FOLDERS CRATED IN PWD. THE DATA CSV FILE IS DOWNLOADED FROM "https://cdaweb.gsfc.nasa.gov/index.html/"
# STORM CLASSIFICATIONS 1) SUPER STORM--   SYM/H VALUE <-100 nT. 2) INTENSE STORM--  -50 nT>SYM/H VALUE>=-100 nT. 3) MODERATE STORM--  -30 nT>SYM/H VALUE>=-50 nT
import time
start = time.time()
import shutil
import os
from datetime import datetime, date
import numpy as np
import pandas as pd
import dateutil.parser
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
startday1 = input("ENTER THE START DATE (AS dd-mm-yyyy): ")
endday1 = input("ENTER THE END DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["startday1", "endday1"]:
    input_log[variable] = eval(variable)
with open("INPUT_LOG_STORM_CLASSES_SEPARATOR_V2.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
DATA_PATH = PWD+'OMNI_HRO_5MIN_136293.csv' # CHANGE THE DATA FILE NAME AS YOU WANT...BUT SHOULD BE A ".csv" FILE
DATA = pd.read_csv(DATA_PATH, header=0, comment='#') # SETTING "comment='#'" WE ELIMINATE THE COMMENTS STARTS WITH # IN THE DATA FILE TO BE LOADED
# DATA = DATA.replace([99.99,999.99,9999.99,99999.9],[math.nan,math.nan,math.nan,math.nan])
DATA = DATA.replace([99.99,999.99,9999.99,99999.9],[np.nan,np.nan,np.nan,np.nan]) # ELIMINATING BAD DATA IN DATAFRAME
# ---------------------------------SECTION 1--OVER----------------------------------------------------------------------
# --------------------------------------------------SECTION 2-----------------------------------------------------------
# CONVERTING ENTERED DATE FORMAT '%d-%m-%Y' IN TO '%Y-%m-%d' AS IN LOADED CSV FILE
startday2 = datetime.strptime(startday1, '%d-%m-%Y')
startday_newformat = startday2.strftime('%Y-%m-%d')
endday2 = datetime.strptime(endday1, '%d-%m-%Y')
endday_newformat = endday2.strftime('%Y-%m-%d')
DATE_LIST = pd.date_range(start=startday_newformat, end=endday_newformat) # CREATING A LIST OF DATES RANGES FROM ENTERED START AND END DATES
DATE_LIST = DATE_LIST.date
START_DATE_TIME = startday_newformat+'T00:00:00.000Z'
END_DATE_TIME = endday_newformat+'T23:55:00.000Z'
startday_newformat1 = startday2.strftime('%d_%m_%Y')
endday_newformat1 = endday2.strftime('%d_%m_%Y')
FOLDER11 = 'STORM_DETAILS_{}_TO_{}'.format(startday_newformat1, endday_newformat1)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
NAME_SUBFOLDER1 = 'SUPER_STORM'
NAME_SUBFOLDER2 = 'INTENSE_STORM'
NAME_SUBFOLDER3 = 'MODERATE_STORM'
SUBFOLDER1 = PATH_TO_FOLDER1+NAME_SUBFOLDER1
os.makedirs(SUBFOLDER1)
PATH_SUBFOLDER1 = SUBFOLDER1 + '/'
SUBFOLDER2 = PATH_TO_FOLDER1+NAME_SUBFOLDER2
os.makedirs(SUBFOLDER2)
PATH_SUBFOLDER2 = SUBFOLDER2 + '/'
SUBFOLDER3 = PATH_TO_FOLDER1+NAME_SUBFOLDER3
os.makedirs(SUBFOLDER3)
PATH_SUBFOLDER3 = SUBFOLDER3 + '/'
# --------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
# --------------------------------------------SECTION 3- SAVING THE STORM DATES AND RESPECTIVE TIME IN TO A FOLDER------
try:
    MASK = (DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] >= START_DATE_TIME) & (
                DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] <= END_DATE_TIME)
    DATA = DATA.loc[MASK]
    # ---------SECTION 3.1----DETAILS OF SUPER STORM IS SAVING IF EXIST (SUPER STORM--SYM/H VALUE <-100 nT)-------------
    MASK2 = (DATA['SYM/H_INDEX_nT'] < -100)
    DATA2 = DATA.loc[MASK2]
    if DATA2.empty == True:
        print("\nNO SUPER STORMS ('SYM/H VALUE <-100 nT') DATES WERE FOUND IN THE ENTERED DATE INTERVAL..................")
        MISSING_INFORMATION1 = PATH_SUBFOLDER1 + 'MISSING_INFORMATION.txt'
        INFO1 = 'NO SUPER STORMS ("SYM/H VALUE <-100 nT") DATES WERE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(startday1, endday1)
        with open(MISSING_INFORMATION1, 'a') as f11:
            f11.write(INFO1 + "\n")
    else:
        print("\nSUPER STORM EVENTS ('SYM/H VALUE <-100 nT') WERE FOUND THE ENTERED DATE INTERVAL AND THE DATE AND RESPECTIVE TIME WERE SAVING")
        kkkk = pd.to_datetime(DATA2['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        ST_DATE1 = {}  # CONVERTING "EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ" TO hh.hh DECIMAL HOUR
        for iii in kkkk:
            iii = str(iii)
            DOY1 = dateutil.parser.parse(iii)
            ST_DATE1[iii] = DOY1.strftime('%Y-%m-%d')
        ST_DATE2 = ST_DATE1.values()
        ST_DATE3 = list(ST_DATE2)
        ST_DATE4 = set(ST_DATE3)
        ST_DATES_LIST = sorted(ST_DATE4)
        for STORM_DATES in ST_DATES_LIST:
            try:
                SINGLE_DAY_DATA = DATA.loc[DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(STORM_DATES)]
                SYMH_MIN = SINGLE_DAY_DATA['SYM/H_INDEX_nT'].min()
                SINGLE_DAY_DATA1 = SINGLE_DAY_DATA.loc[SINGLE_DAY_DATA['SYM/H_INDEX_nT'] == SYMH_MIN]
                STORM_DETAILS = SINGLE_DAY_DATA1[['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ', 'SYM/H_INDEX_nT']]
                FILENAME11 = 'SUPER_STORM_DATES_DETAILS_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
                print("\nTHE SUPER_STORM DETAILS FOR THE DATE '", STORM_DATES, "' ARE SAVING TO THE FILE '", FILENAME11,
                      "' IN THE FOLDER '", NAME_SUBFOLDER1, "'....")
                FILENAME1 = PATH_SUBFOLDER1 + FILENAME11
                # STORM_DETAILS.to_csv(FILENAME1, index=False)
                with open(FILENAME1, 'a') as f2:
                    STORM_DETAILS.to_csv(f2, index=False)
            except OSError:
                print("\nSOME DATA WERE MISSING")
        FILENAME22 = 'DETAILED_SUPER_STORM_REPORT_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
        print("\nA DETAILED SUPER STORM REPORT IS SAVING TO THE FILE '", FILENAME22, "' IN THE FOLDER '", FOLDER11, "'....\n")
        FILENAME2 = PATH_SUBFOLDER1 + FILENAME22
        DATA2.to_csv(FILENAME2, index=False)
    # -------------------------------------------SECTION 3.1 IS OVER----------------------------------------------------
    # --SECTION 3.2----DETAILS OF INTENSE STORM IS SAVING IF EXIST (INTENSE STORM-- -50 nT>SYM/H VALUE>=-100 nT)--------
    MASK3 = (DATA['SYM/H_INDEX_nT'] >= (-100)) & (DATA['SYM/H_INDEX_nT'] < (-50))
    DATA3 = DATA.loc[MASK3]
    if DATA3.empty == True:
        print("\nNO INTENSE STORMS ('-50 nT>SYM/H VALUE>=-100 nT') DATES WERE FOUND IN THE ENTERED DATE INTERVAL..................")
        MISSING_INFORMATION2 = PATH_SUBFOLDER2 + 'MISSING_INFORMATION.txt'
        INFO2 = 'NO INTENSE STORMS ("-50 nT>SYM/H VALUE>=-100 nT") DATES WERE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(startday1, endday1)
        with open(MISSING_INFORMATION2, 'a') as f3:
            f3.write(INFO2 + "\n")
    else:
        print("\nINTENSE STORM EVENTS ('-50 nT>SYM/H VALUE>=-100 nT') WERE FOUND THE ENTERED DATE INTERVAL AND THE DATE AND RESPECTIVE TIME WERE SAVING")
        kkkkk = pd.to_datetime(DATA3['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        ST_DATE18 = {}  # CONVERTING "EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ" TO hh.hh DECIMAL HOUR
        for iiii in kkkkk:
            iiii = str(iiii)
            DOY18 = dateutil.parser.parse(iiii)
            ST_DATE18[iiii] = DOY18.strftime('%Y-%m-%d')
        ST_DATE28 = ST_DATE18.values()
        ST_DATE38 = list(ST_DATE28)
        ST_DATE481 = set(ST_DATE38)
        ST_DATE48 = ST_DATE481-ST_DATE4
        ST_DATES_LIST8 = sorted(ST_DATE48)
        for STORM_DATES8 in ST_DATES_LIST8:
            try:
                SINGLE_DAY_DATA8 = DATA3.loc[DATA3['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(STORM_DATES8)]
                SYMH_MIN8 = SINGLE_DAY_DATA8['SYM/H_INDEX_nT'].min()
                SINGLE_DAY_DATA18 = SINGLE_DAY_DATA8.loc[SINGLE_DAY_DATA8['SYM/H_INDEX_nT'] == SYMH_MIN8]
                STORM_DETAILS8 = SINGLE_DAY_DATA18[['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ', 'SYM/H_INDEX_nT']]
                FILENAME118 = 'INTENSE_STORM_DATES_DETAILS_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
                print("\nTHE INTENSE_STORM DETAILS FOR THE DATE '", STORM_DATES8, "' ARE SAVING TO THE FILE '", FILENAME118,
                      "' IN THE FOLDER '", NAME_SUBFOLDER2, "'....")
                FILENAME18 = PATH_SUBFOLDER2 + FILENAME118
                # STORM_DETAILS.to_csv(FILENAME1, index=False)
                with open(FILENAME18, 'a') as f4:
                    STORM_DETAILS8.to_csv(f4, index=False)
            except OSError:
                print("\nSOME DATA WERE MISSING")
        FILENAME228 = 'DETAILED_INTENSE_STORM_REPORT_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
        print("\nA DETAILED INTENSE STORM REPORT IS SAVING TO THE FILE '", FILENAME228, "' IN THE FOLDER '", NAME_SUBFOLDER2, "'....\n")
        FILENAME28 = PATH_SUBFOLDER2 + FILENAME228
        DATA3.to_csv(FILENAME28, index=False)
    # -------------------------------------------SECTION 3.2 IS OVER----------------------------------------------------
    # --SECTION 3.3----DETAILS OF MODERATE STORM IS SAVING IF EXIST (MODERATE STORM-- -30 nT>SYM/H VALUE>=-50 nT)-------
    MASK4 = (DATA['SYM/H_INDEX_nT'] >= -50) & (DATA['SYM/H_INDEX_nT'] < -30)
    DATA4 = DATA.loc[MASK4]
    if DATA4.empty == True:
        print("\nNO MODERATE STORMS ('-30 nT>SYM/H VALUE>=-50 nT') DATES WERE FOUND IN THE ENTERED DATE INTERVAL..................")
        MISSING_INFORMATION3 = PATH_SUBFOLDER3 + 'MISSING_INFORMATION.txt'
        INFO3 = 'NO MODERATE STORMS ("-30 nT>SYM/H VALUE>=-50 nT") DATES WERE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(startday1, endday1)
        with open(MISSING_INFORMATION3, 'a') as f5:
            f5.write(INFO3 + "\n")
    else:
        print("\nMODERATE STORM EVENTS ('-30 nT>SYM/H VALUE>=-50 nT') WERE FOUND THE ENTERED DATE INTERVAL AND THE DATE AND RESPECTIVE TIME WERE SAVING")
        kkkkkk = pd.to_datetime(DATA4['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        ST_DATE19 = {}  # CONVERTING "EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ" TO hh.hh DECIMAL HOUR
        for iiiii in kkkkkk:
            iiiii = str(iiiii)
            DOY19 = dateutil.parser.parse(iiiii)
            ST_DATE19[iiiii] = DOY19.strftime('%Y-%m-%d')
        ST_DATE29 = ST_DATE19.values()
        ST_DATE39 = list(ST_DATE29)
        ST_DATE4911 = set(ST_DATE39)
        ST_DATE491 = ST_DATE4911-ST_DATE4
        ST_DATE49 = ST_DATE491-ST_DATE48
        ST_DATES_LIST9 = sorted(ST_DATE49)
        for STORM_DATES9 in ST_DATES_LIST9:
            try:
                SINGLE_DAY_DATA9 = DATA4.loc[DATA4['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(STORM_DATES9)]
                SYMH_MIN9 = SINGLE_DAY_DATA9['SYM/H_INDEX_nT'].min()
                SINGLE_DAY_DATA19 = SINGLE_DAY_DATA9.loc[SINGLE_DAY_DATA9['SYM/H_INDEX_nT'] == SYMH_MIN9]
                STORM_DETAILS9 = SINGLE_DAY_DATA19[['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ', 'SYM/H_INDEX_nT']]
                FILENAME119 = 'MODERATE_STORM_DATES_DETAILS_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
                print("\nTHE MODERATE_STORM DETAILS FOR THE DATE '", STORM_DATES9, "' ARE SAVING TO THE FILE '", FILENAME119,
                      "' IN THE FOLDER '", NAME_SUBFOLDER3, "'....")
                FILENAME19 = PATH_SUBFOLDER3 + FILENAME119
                # STORM_DETAILS.to_csv(FILENAME1, index=False)
                with open(FILENAME19, 'a') as f6:
                    STORM_DETAILS9.to_csv(f6, index=False)
            except OSError:
                print("\nSOME DATA WERE MISSING")
        FILENAME229 = 'DETAILED_MODERATE_STORM_REPORT_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
        print("\nA DETAILED MODERATE STORM REPORT IS SAVING TO THE FILE '", FILENAME229, "' IN THE FOLDER '", NAME_SUBFOLDER3, "'....\n")
        FILENAME29 = PATH_SUBFOLDER3 + FILENAME229
        DATA4.to_csv(FILENAME29, index=False)
    # -------------------------------------------SECTION 3.3 IS OVER----------------------------------------------------
except OSError:
    print("\nYOU ENTERED WRONG DATES....PLEASE RE RUN THE CODE AND ENTER DATES PROPERLY")
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# -------------------------------------SECTION 3 IS OVER----------------------------------------------------------------
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 01-06-2021---------------------------SREEKUMAR HARIDAS--------------------