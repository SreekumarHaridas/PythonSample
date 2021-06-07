# THIS IS A SIMPLE PYTHON PROGRAM WHICH SPLITS THE DATA FOR ONE YEAR DOWNLOADED FROM "https://cdaweb.gsfc.nasa.gov/index.html/"
# IN TO DIFFERENT DATES FOLDERS IN PWD
import time
start = time.time()
import shutil
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
#----------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
startday1 = input("ENTER THE START DATE (AS dd-mm-yyyy): ")
endday1 = input("ENTER THE END DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
#print(PWD)
for variable in ["startday1", "endday1"]:
    input_log[variable] = eval(variable)
with open("INPUT_LOG_CDA_WEB_DATA_DAY_FOLDER_CREATOR.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
DATA_PATH = PWD+'OMNI_HRO_5MIN_136293.csv'
DATA = pd.read_csv(DATA_PATH, header=0, comment='#') # SETTING "comment='#'" WE ELIMINATE THE COMMENTS STARTS WITH # IN THE DATA FILE TO BE LOADED
#----------------------------------SECTION 1--OVER----------------------------------------------------------------------
#---------------------------------------------------SECTION 2-----------------------------------------------------------
# CONVERTING ENTERED DATE FORMAT '%d-%m-%Y' IN TO '%Y-%m-%d' AS IN LOADED CSV FILE
startday2 = datetime.strptime(startday1, '%d-%m-%Y')
startday_newformat = startday2.strftime('%Y-%m-%d')
endday2 = datetime.strptime(endday1, '%d-%m-%Y')
endday_newformat = endday2.strftime('%Y-%m-%d')
DATE_LIST = pd.date_range(start=startday_newformat, end=endday_newformat) # CREATING A LIST OF DATES RANGES FROM ENTERED START AND END DATES
DATE_LIST = DATE_LIST.date
#---------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
#---------------------------------------------SECTION 3- SAVING THE DATA OF EACH DAY IN TO RESPECTIVE DATE FOLDERS------
for DATES1 in DATE_LIST:
    DATES = str(DATES1)
    try:
        DATES1 = datetime.strptime(DATES, '%Y-%m-%d')
        DATES_NEW_FORMAT = DATES1.strftime('%d-%m-%Y')
        DATES_NEW_FORMAT2 = DATES1.strftime('%d_%m_%Y')
        SINGLE_DAY_DATA = DATA.loc[DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(DATES)]
        DATE_FOLDER = PWD + DATES_NEW_FORMAT2
        if os.path.exists(DATE_FOLDER):
            shutil.rmtree(DATE_FOLDER)
        os.makedirs(DATE_FOLDER)
        PATH_TO_DATE_FOLDER = DATE_FOLDER + '/'  # PATH IN TO FOLDER1
        FILENAME11 = 'DATA_{}.csv'.format(DATES_NEW_FORMAT2)
        FILENAME1 = PATH_TO_DATE_FOLDER+FILENAME11
        FILENAME22 = 'DATA_{}.txt'.format(DATES_NEW_FORMAT2)
        FILENAME2 = PATH_TO_DATE_FOLDER + FILENAME22
        SINGLE_DAY_DATA.to_csv(FILENAME1, index=False)
        SINGLE_DAY_DATA.to_csv(FILENAME2, index=False)
        print("\nSAVING DATA IN TO FILES NAMED '",FILENAME11,"'AND'", FILENAME22,"'IN THE FOLDER '", DATES_NEW_FORMAT2,"'............")
    except OSError:
        print("\nSOME DATES WERE MISSING")
print("\n TOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' seconds, HERE NUMPY LIBRARY IS USED FOR DATA FILE LOADING!!!!!!!!!" %(time.time() - start))
#--------------------------------------SECTION 3 IS OVER----------------------------------------------------------------
#---------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
#-------------------------------------------ON 25-05-2021---------------------------SREEKUMAR HARIDAS-------------------































