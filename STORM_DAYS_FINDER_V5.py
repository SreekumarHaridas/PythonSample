# THIS IS A SIMPLE PYTHON PROGRAM WHICH FIND THE STORM DATES BASED ON ENTERED SYM-H VALUE AND SAVE THE DATES IN A CSV
# FILE IN THE FOLDER CRATED IN PWD. THE DATA CSV FILE IS DOWNLOADED FROM "https://cdaweb.gsfc.nasa.gov/index.html/"
# THE GRAPH BETWEEN 'SYM-H vs DATE' IS PLOTTING IN .jpeg,.png,.pdf and .svg FORMAT AND SAVING THEM IN RESPECTIVE FOLDERS'
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
import datetime as dt
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
SYMH_THRESHOLD = int(input("ENTER THE CUT OF VALUE OF SYM-H FOR STORM (INCLUDE NEGATIVE SIGN IF NEEDED) : "))
startday1 = input("ENTER THE START DATE (AS dd-mm-yyyy): ")
endday1 = input("ENTER THE END DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["SYMH_THRESHOLD", "startday1", "endday1"]:
    input_log[variable] = eval(variable)
with open("INPUT_LOG_STORM_DAYS_FINDER_V5.txt", 'w') as f1:
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
endday_newformat = datetime.strptime(endday_newformat, '%Y-%m-%d')
END_DATE_TIME1 = endday_newformat+dt.timedelta(days=1)
END_DATE_TIME1 = END_DATE_TIME1.strftime('%Y-%m-%d')
END_DATE_TIME = END_DATE_TIME1+'T00:00:00.000Z'
startday_newformat1 = startday2.strftime('%d_%m_%Y')
endday_newformat1 = endday2.strftime('%d_%m_%Y')
FOLDER11 = 'STORM_DETAILS_{}_TO_{}'.format(startday_newformat1, endday_newformat1)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
NAME_SUBFOLDER1 = 'SYMH_FIGURE_PNG'
NAME_SUBFOLDER2 = 'SYMH_FIGURE_PDF'
NAME_SUBFOLDER3 = 'SYMH_FIGURE_JPEG'
NAME_SUBFOLDER4 = 'SYMH_FIGURE_SVG'
SUBFOLDER1 = PATH_TO_FOLDER1 + NAME_SUBFOLDER1
os.makedirs(SUBFOLDER1)
PATH_SUBFOLDER1 = SUBFOLDER1 + '/'
SUBFOLDER2 = PATH_TO_FOLDER1 + NAME_SUBFOLDER2
os.makedirs(SUBFOLDER2)
PATH_SUBFOLDER2 = SUBFOLDER2 + '/'
SUBFOLDER3 = PATH_TO_FOLDER1 + NAME_SUBFOLDER3
os.makedirs(SUBFOLDER3)
PATH_SUBFOLDER3 = SUBFOLDER3 + '/'
SUBFOLDER4 = PATH_TO_FOLDER1 + NAME_SUBFOLDER4
os.makedirs(SUBFOLDER4)
PATH_SUBFOLDER4 = SUBFOLDER4 + '/'
# --------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
# --------------------------------------------SECTION 3- SAVING THE STORM DATES AND FIGURES FOLDERS---------------------
try:
    MASK = (DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] >= START_DATE_TIME) & (
                DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] <= END_DATE_TIME)
    DATA = DATA.loc[MASK]
    MASK2 = (DATA['SYM/H_INDEX_nT'] <= SYMH_THRESHOLD)
    DATA2 = DATA.loc[MASK2]
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
    if len(ST_DATES_LIST) == 0:
        print("\n NO STORM DATES WERE FOUND CORRESPONDING TO THE ENTERED PARAMETERS ")
    else:
        for STORM_DATES in ST_DATES_LIST:
            try:
                SINGLE_DAY_DATA = DATA.loc[DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(STORM_DATES)]
                SYMH_MIN = SINGLE_DAY_DATA['SYM/H_INDEX_nT'].min()
                SINGLE_DAY_DATA1 = SINGLE_DAY_DATA.loc[SINGLE_DAY_DATA['SYM/H_INDEX_nT'] == SYMH_MIN]
                STORM_DETAILS = SINGLE_DAY_DATA1[['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ', 'SYM/H_INDEX_nT']]
                FILENAME11 = 'STORM_DATES_DETAILS_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
                print("\nTHE STORM DETAILS FOR THE DATE '", STORM_DATES, "' ARE SAVING TO THE FILE '", FILENAME11,
                      "' IN THE FOLDER '", FOLDER11, "'....")
                FILENAME1 = PATH_TO_FOLDER1 + FILENAME11
                # STORM_DETAILS.to_csv(FILENAME1, index=False)
                with open(FILENAME1, 'a') as f:
                    STORM_DETAILS.to_csv(f, index=False)
            except OSError:
                print("\nSOME DATA WERE MISSING")
        FILENAME22 = 'DETAILED_STORM_REPORT_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
        print("\nA DETAILED STORM REPORT IS SAVING TO THE FILE '", FILENAME22, "' IN THE FOLDER '", FOLDER11, "'....\n")
        FILENAME2 = PATH_TO_FOLDER1 + FILENAME22
        DATA2.to_csv(FILENAME2, index=False)
        # ----PLOTTING THE SYM/H VALUES FOR THE ENTERED PERIOD----------------------------------------------------------
        print("\nTHE GRAPH BETWEEN 'SYM-H vs DATE' IS PLOTTING AND SAVING IN THE FOLDER'", FOLDER11,
              "'....DO NOT CLOSE THE PROGRAM UNTIL IT IS COMPLETE\n")
        DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] = pd.to_datetime(DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'],
                                                                     format='%Y-%m-%dT%H:%M:%S.%fZ')
        DATA = DATA[['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ', 'SYM/H_INDEX_nT']]
        DATA = DATA.set_index(['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'])
        rc('font', weight='bold')
        SYMH_MAX = DATA['SYM/H_INDEX_nT'].max()
        SYMH_MIN = DATA['SYM/H_INDEX_nT'].min()
        minylimit1 = ((SYMH_MIN // 10) * 10) + 10
        minylimit = int(minylimit1)
        maxylimit1 = ((SYMH_MAX // 10) * 10) + 10
        maxylimit = int(maxylimit1)
        DATA.plot(figsize=(16, 9), legend=False, lw=0.5, color='blue')
        ax = plt.gca()
        plt.xlabel("DATE", fontsize=16, fontweight="bold")
        plt.ylabel("SYM-H (nT)", fontsize=16, fontweight="bold")
        plt.setp(ax.spines.values(), linewidth=1)
        plt.ylim(minylimit, maxylimit)
        plt.xticks(fontsize=14, fontweight="bold")
        plt.yticks(np.arange(minylimit+(-20), maxylimit + 20, 20), np.arange(minylimit+(-20), maxylimit + 20, 20), fontsize=14, fontweight="bold")
        tiltle1 = 'SYM-H FOR THE PERIOD : {} TO {}'.format(startday1, endday1)
        plt.tick_params(which='both', direction='in')
        plt.grid(which='major', linestyle=':', linewidth=0.1)
        plt.title(tiltle1, fontsize=18, fontweight="bold")
        plt.axhline(y=SYMH_THRESHOLD, ls='--', lw=0.5, color='red')
        plt.tight_layout()
        # -----------SAVING FIGURES IN A COMMON FOLDER ALONG WITH DAY FOLDERS AND THIS PYTHON PROGRAM
        GNAME1 = 'STORM_PLOT_{}_TO_{}.png'.format(startday_newformat1, endday_newformat1)
        GNAME2 = 'STORM_PLOT_{}_TO_{}.pdf'.format(startday_newformat1, endday_newformat1)
        GNAME3 = 'STORM_PLOT_{}_TO_{}.jpeg'.format(startday_newformat1, endday_newformat1)
        GNAME4 = 'STORM_PLOT_{}_TO_{}.svg'.format(startday_newformat1, endday_newformat1)
        GNAME11 = PATH_SUBFOLDER1 + GNAME1
        GNAME21 = PATH_SUBFOLDER2 + GNAME2
        GNAME31 = PATH_SUBFOLDER3 + GNAME3
        GNAME41 = PATH_SUBFOLDER4 + GNAME4
        plt.savefig(GNAME11, dpi=500, bbox_inches='tight')
        plt.savefig(GNAME21, dpi=500, bbox_inches='tight')
        plt.savefig(GNAME31, dpi=500, bbox_inches='tight')
        plt.savefig(GNAME41, dpi=300, bbox_inches='tight')
        # ------------------------------------------PLOTTING IS OVER----------------------------------------------------
    # ----------------------------------SECTION 3 IS OVER---------------------------------------------------------------
except OSError:
    print("\nYOU ENTERED WRONG DATES....PLEASE RE RUN THE CODE AND ENTER DATES PROPERLY")
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 19-06-2021---------------------------SREEKUMAR HARIDAS--------------------