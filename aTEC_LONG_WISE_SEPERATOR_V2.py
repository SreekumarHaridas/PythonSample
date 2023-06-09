import time
start = time.time()
import shutil
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import math
import pandas as pd
import dateutil.parser
from scipy import signal
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
Date_of_the_Day = input("ENTER THE DATE (AS dd-mm-yyyy): ")
Hour = input("ENTER THE HOUR (e.g. '00 or 23' ): ")
Time_Block = int(input("ENTER THE TIME (e.g. '0 to 11' ): "))
LAT1 = int(input("ENTER THE LATITUDE1 IN DEGREE (e.g. '0' ): "))
LAT2 = int(input("ENTER THE LATITUDE2 IN DEGREE (e.g. '30' ): "))
LON1 = int(input("ENTER THE LONGITUDE1 IN DEGREE (e.g. '60' ): "))
LON2 = int(input("ENTER THE LONGITUDE2 IN DEGREE (e.g. '90' ): "))
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["Date_of_the_Day", "Hour", "Time_Block", "LAT1","LAT2","LON1", "LON2"]:
    input_log[variable] = eval(variable)
with open("aTEC_LONG_WISE_SEPERATOR_V2.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
DATA_PATH = PWD+'ATEC_DATA_06_02_2023_16_3.csv'
DATA = pd.read_csv(DATA_PATH, header=0, comment='#') # SETTING "comment='#'" WE ELIMINATE THE COMMENTS STARTS WITH # IN THE DATA FILE TO BE LOADED

DATA3=DATA.loc[(DATA['LONGITUDE'] >= LON1 )& (DATA['LONGITUDE']  <= LON2) & (DATA['LATITUDE']  >= LAT1) & (DATA['LATITUDE'] <= LAT2)] # FILTERING THE DATA FRAME BASED ON THE ENTERED COORDINATES
date_value_1=datetime.strptime(Date_of_the_Day,'%d-%m-%Y')
Date_Value=datetime(date_value_1.year,date_value_1.month,date_value_1.day)
day_of_year = Date_Value.strftime('%j')
Date_of_the_Day2 = datetime.strptime(Date_of_the_Day, '%d-%m-%Y')
Date_of_the_Day3 = Date_of_the_Day2.strftime('%d_%m_%Y')
FOLDER1122 = 'dTEC_FIGURES_{}'.format(Date_of_the_Day3)
FOLDER122 = PWD + FOLDER1122
if os.path.exists(FOLDER122):
    shutil.rmtree(FOLDER122)
os.makedirs(FOLDER122)
PATH_TO_FOLDER122 = FOLDER122 + '/'  # PATH IN TO FOLDER122

FOLDER11 = 'aTEC_{}_LAT_{}_{}_LONG_{}_{}_{}_{}'.format(Date_of_the_Day3,LAT1,LAT2,LON1,LON2,Hour,Time_Block)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
FILE_NAME = 'aTEC_{}_LAT_{}_{}_LONG_{}_{}_{}_{}.txt'.format(Date_of_the_Day3,LAT1,LAT2,LON1,LON2,Hour,Time_Block)
FILE_NAME_2 = PATH_TO_FOLDER1 + FILE_NAME
DATA4 = DATA3.replace(np.nan, 'nan', regex=True)
DATA4.to_csv(FILE_NAME_2, header=None, index=None, sep='\t', mode='a')
daTEC_1 = DATA3['ATEC'].replace(np.nan, 0)
daTEC=signal.detrend(daTEC_1)

rc('font', weight='bold')
rc('axes', linewidth=10)
daTEC_MAX = max(daTEC)
ylimit11 = ((daTEC_MAX // 10) * 10) + 10
ylimit1 = int(ylimit11)
daTEC_MIN = min(daTEC)
ylimit21 = ((daTEC_MIN // 10) * 10) -10
ylimit2 = int(ylimit21)
plt.figure(figsize=(16,9))
plt.plot(DATA3['LATITUDE'],daTEC, lw=3, color='black')
plt.xlabel("Latitude (degree)", fontsize=33, fontweight="bold")
plt.ylabel("dTEC (TECU)", fontsize=33, fontweight="bold")
ax = plt.gca()
plt.setp(ax.spines.values(), linewidth=1)
plt.xlim(0, 30)
plt.ylim(ylimit2, ylimit1)
plt.xticks(np.arange(0, 31, 5), np.arange(0, 31, 5), fontsize=32, fontweight="bold")
plt.yticks(np.arange(ylimit2, ylimit1 + 10, 10), np.arange(ylimit2, ylimit1 + 10, 10), fontsize=32, fontweight="bold")
plt.tick_params(which='major', direction='in')
plt.grid(which='both', linestyle=':', linewidth=0.4)
plt.tight_layout()
GNAME31 = 'INDIAN_dTEC_PLOT_{}_{}_{}.jpeg'.format(Date_of_the_Day3,Hour,Time_Block)
GNAME311 = PATH_TO_FOLDER122 + GNAME31
plt.savefig(GNAME311, dpi=1000, bbox_inches='tight')
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes....................!!!!!!!!!" %((time.time() - start)/60))
# -------------------------------------SECTION 3 IS OVER----------------------------------------------------------------
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 27-03-2023---------------------------SREEKUMAR HARIDAS--------------------