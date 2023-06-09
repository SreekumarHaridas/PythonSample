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
from scipy.signal import savgol_filter
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
Date_of_the_Day = input("ENTER THE DATE (AS dd-mm-yyyy): ")
CEA = int(input("ENTER THE CUT-OFF ELIVATION ANGLE IN DEGREE (e.g. 50): "))
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["Date_of_the_Day", "CEA"]:
    input_log[variable] = eval(variable)
with open("IGS_GPS_VTEC_DATA_PLOT_WITH_DATE_COLUMN.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
# ---------------------------------SECTION 1--OVER---------------------------------------------------------------------
date_value_1=datetime.strptime(Date_of_the_Day,'%d-%m-%Y')
Date_Value=datetime(date_value_1.year,date_value_1.month,date_value_1.day)
day_of_year = Date_Value.strftime('%j')
Date_of_the_Day2 = datetime.strptime(Date_of_the_Day, '%d-%m-%Y')
Date_of_the_Day3 = Date_of_the_Day2.strftime('%d_%m_%Y')
FOLDER11223 ='LT_BASED_GPS_FIGURE_ON_{}_WITH_DATE'.format(Date_of_the_Day3)
FOLDER1223 = PWD + FOLDER11223
if os.path.exists(FOLDER1223):
    shutil.rmtree(FOLDER1223)
os.makedirs(FOLDER1223)
PATH_TO_FOLDER1223 = FOLDER1223 + '/'  # PATH IN TO FOLDER1223

FOLDER112223 ='LT_BASED_GPS_FILE_ON_{}_WITH_DATE'.format(Date_of_the_Day3)
FOLDER12223 = PWD + FOLDER112223
if os.path.exists(FOLDER12223):
    shutil.rmtree(FOLDER12223)
os.makedirs(FOLDER12223)
PATH_TO_FOLDER12223 = FOLDER12223 + '/'  # PATH IN TO FOLDER12223

DATA_PATH1 = PWD+'IISC061-2023-03-02.txt'
DATA_1= pd.read_csv(DATA_PATH1, delimiter='\t', header=None) 
DATA_PATH2 = PWD+'IISC062-2023-03-03.txt'
DATA_2= pd.read_csv(DATA_PATH2, delimiter='\t', header=None)

DATA_1.sort_values(by=[1])
DATA_2.sort_values(by=[1])

DATA_11=DATA_1.loc[DATA_1.iloc[:,1] >= 18.500000]
DATA_12=DATA_2.loc[DATA_2.iloc[:,1] <= 18.500000]
frames = [DATA_11, DATA_12]
  
DATA1 = pd.concat(frames)
DATA1.iloc[:,1]+= 5.5
DATA1.iloc[:,1].loc[DATA1.iloc[:,1]>=24] -= 24# converting to local time

DATA=DATA1.loc[DATA1.iloc[:,4] >=CEA] 
DATA.drop(DATA.index[DATA.iloc[:,1] < 0],inplace=True)
GPS_TIME=DATA.iloc[:,0]
LT=DATA.iloc[:,1]
PRN=DATA.iloc[:,2]
ELE=DATA.iloc[:,4]
LAT=DATA.iloc[:,5]
LON=DATA.iloc[:,6]
VTEC=DATA.iloc[:,8]
PRN_ARRAY=PRN.to_numpy()
PRN_ARRAY_UNIQUE=np.unique(PRN_ARRAY)
mean_LT=LT.groupby(LT).mean()
mean_VTEC=VTEC.groupby(LT).mean()
date=[Date_of_the_Day]*len(mean_LT)
date_Column=np.array(date)
LT_Column=mean_LT.to_numpy()
VTEC_Column=mean_VTEC.to_numpy()
NEW_DATAFRAME = pd.DataFrame({'DATE': date_Column,'LT': LT_Column,'VTEC': VTEC_Column})
FILE_PATH2 = PATH_TO_FOLDER12223+'LT_BASED_VTEC_DATA_{}_ELE_ANGLE_{}_WITH_DATE.txt'.format(Date_of_the_Day3,CEA)
FILE_PATH3 = PATH_TO_FOLDER12223+'LT_BASED_VTEC_DATA_{}_ELE_ANGLE_{}_WITH_DATE.csv'.format(Date_of_the_Day3,CEA)
NEW_DATAFRAME.to_csv(FILE_PATH2 , header=None, index=False, sep='\t', mode='a') 
NEW_DATAFRAME.to_csv(FILE_PATH3 , index=False) 
VTEC_MAX = max(VTEC)
ylimit1 = ((VTEC_MAX // 10) * 10) + 10
ylimit = int(ylimit1)
plt.figure(figsize=(10, 6))
plt.plot(mean_LT, mean_VTEC, lw=2, color='blue')
plt.xlabel("LT (hours)", fontsize=16, fontweight="bold")
plt.ylabel("VTEC (TECU)", fontsize=16, fontweight="bold")
ax = plt.gca()
plt.setp(ax.spines.values(), linewidth=1)
plt.xlim(0, 24)
plt.ylim(0, ylimit)
plt.xticks(np.arange(0, 25, 1), np.arange(0, 25, 1), fontsize=14, fontweight="bold")
plt.yticks(np.arange(0, ylimit + 10, 10), np.arange(0, ylimit + 10, 10), fontsize=14, fontweight="bold")
plt.tick_params(which='major', direction='in')
plt.grid(which='both', linestyle=':', linewidth=0.4)
GNAME1 = 'LT_BASED_GPS_VTEC_ON_{}.jpeg'.format(Date_of_the_Day3)
GNAME11 = PATH_TO_FOLDER1223+GNAME1
plt.savefig(GNAME11, dpi=600, bbox_inches='tight')
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes....................!!!!!!!!!" %((time.time() - start)/60))

# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 05-05-2023---------------------------SREEKUMAR HARIDAS--------------------