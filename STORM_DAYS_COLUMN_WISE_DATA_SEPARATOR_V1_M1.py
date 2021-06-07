# THIS IS A SIMPLE PYTHON PROGRAM WHICH SEPARATES THE COLUMN WISE DATA OF ENTERED PERIOD OF STORM EVENTS INTO ".csv"
# AND ".txt" FILES
import time
start = time.time()
import shutil
import os
import matplotlib.pyplot as plt
from matplotlib import rc
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
with open("INPUT_LOG_STORM_DAYS_COLUMN_WISE_DATA_SEPARATOR_V1_M1.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
DATA_PATH = PWD+'OMNI_HRO_5MIN_136293.csv'
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
FOLDER11 = 'EVENT_DETAILS_{}_TO_{}'.format(startday_newformat1, endday_newformat1)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
# --------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
# --------------------------------------------SECTION 3- SAVING THE STORM DATES AND FIGURES FOLDERS---------------------
try:
    MASK = (DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] >= START_DATE_TIME) & (
                DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] <= END_DATE_TIME)
    DATA = DATA.loc[MASK]
    HEADERS = DATA.columns
    print("THE COLUMN HEADERS ARE.......'", HEADERS, "'")
    if DATA.empty == True:
        print(
            "\nTHE '.csv' FILE IS EMPTY SO THAT NO DATA FRAME CAN BE GENERATED FROM IT........................")
        MISSING_INFORMATION1 = PATH_TO_FOLDER1 + 'MISSING_INFORMATION.txt'
        INFO1 = 'NO SUPER STORMS ("SYM/H VALUE <-100 nT") DATES WERE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(
            startday1, endday1)
        with open(MISSING_INFORMATION1, 'a') as f11:
            f11.write(INFO1 + "\n")
    else:
        print(
            "\nTHE COLUMN DATA FROM THE ENTERED '.csv' FILE ARE SAVING TO SEPARATE '.csv' AND '.txt' FILES")
        NAME_SUBFOLDER1 = 'COLUMN_WISE_SEPARATED_DATA'
        NAME_SUBFOLDER2 = 'CSV_FILES'
        NAME_SUBFOLDER3 = 'TEXT_FILES'
        SUBFOLDER1 = PATH_TO_FOLDER1 + NAME_SUBFOLDER1
        os.makedirs(SUBFOLDER1)
        PATH_SUBFOLDER1 = SUBFOLDER1 + '/'
        SUBFOLDER2 = PATH_SUBFOLDER1 + NAME_SUBFOLDER2
        os.makedirs(SUBFOLDER2)
        PATH_SUBFOLDER2 = SUBFOLDER2 + '/'
        SUBFOLDER3 = PATH_SUBFOLDER1 + NAME_SUBFOLDER3
        os.makedirs(SUBFOLDER3)
        PATH_SUBFOLDER3 = SUBFOLDER3 + '/'
        for column in HEADERS:
            POSITION_OF_COLUMN = HEADERS.get_loc(column)+1
            try:
                FILE_NAME_1 = 'COLUMN{}.csv'.format(POSITION_OF_COLUMN)
                FILE_NAME_11 = PATH_SUBFOLDER2 + FILE_NAME_1
                DATA[column].to_csv(FILE_NAME_11, index=False)
                FILE_NAME_2 = 'COLUMN{}.txt'.format(POSITION_OF_COLUMN)
                FILE_NAME_22 = PATH_SUBFOLDER3 + FILE_NAME_2
                DATA[column].to_csv(FILE_NAME_22, index=False)
                FILE_NAME_3 = 'COLUMN{}_WITHOUT_HEADER.txt'.format(POSITION_OF_COLUMN)
                FILE_NAME_33 = PATH_SUBFOLDER3 + FILE_NAME_3
                DATA[column].to_csv(FILE_NAME_33, index=False, header=None)
            except OSError:
                print("\nCOLUMN DATA'",column,"'WERE MISSING'")
    # ----------------------------------SECTION 3 IS OVER---------------------------------------------------------------
except OSError:
    print("\nYOU ENTERED WRONG DATES....PLEASE RE RUN THE CODE AND ENTER DATES PROPERLY")
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 06-06-2021---------------------------SREEKUMAR HARIDAS--------------------