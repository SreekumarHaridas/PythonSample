import time
start = time.time()
import shutil
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['timezone'] = 'Asia/Calcutta'
import matplotlib.dates as mdates
from matplotlib import rc
from datetime import datetime, date
import numpy as np
import pandas as pd
import dateutil.parser
import datetime as dt
from dateutil import tz
import sympy as sym
from scipy.misc import derivative
PWD1 = os.getcwd()
PWD = PWD1+'/'

DATA_PATH_1 = PWD+'MERGED_FILE_COL.txt'
DATA_1 = pd.read_csv(DATA_PATH_1, delimiter='\t', header=None)
DATE1=DATA_1.iloc[:,0]
LT1=DATA_1.iloc[:,1]
VTEC1=DATA_1.iloc[:,2]
DATA_1['datetime'] = pd.to_datetime(DATE1) + pd.to_timedelta(LT1, unit='H')
DATA_1 = DATA_1.set_index(['datetime'])

DATA_PATH_2 = PWD+'MERGED_FILE_BAN.txt'
DATA_2 = pd.read_csv(DATA_PATH_2, delimiter='\t', header=None)
DATE2=DATA_2.iloc[:,0]
LT2=DATA_2.iloc[:,1]
VTEC2=DATA_2.iloc[:,2]
DATA_2['datetime'] = pd.to_datetime(DATE2) + pd.to_timedelta(LT2, unit='H')
DATA_2 = DATA_2.set_index(['datetime'])

DATA_PATH_3 = PWD+'MERGED_FILE_HYD.txt'
DATA_3 = pd.read_csv(DATA_PATH_3, delimiter='\t', header=None)
DATE3=DATA_3.iloc[:,0]
LT3=DATA_3.iloc[:,1]
VTEC3=DATA_3.iloc[:,2]
DATA_3['datetime'] = pd.to_datetime(DATE3) + pd.to_timedelta(LT3, unit='H')
DATA_3 = DATA_3.set_index(['datetime'])

DATA_PATH_4 = PWD+'MERGED_FILE_LCK.txt'
DATA_4 = pd.read_csv(DATA_PATH_4, delimiter='\t', header=None)
DATE4=DATA_4.iloc[:,0]
LT4=DATA_4.iloc[:,1]
VTEC4=DATA_4.iloc[:,2]
DATA_4['datetime'] = pd.to_datetime(DATE4) + pd.to_timedelta(LT4, unit='H')
DATA_4 = DATA_4.set_index(['datetime'])

DATA_PATH_5 = PWD+'AVG_STD_VTEC_RANDOM_COL.txt'
DATA_51 = pd.read_csv(DATA_PATH_5, delimiter='\t', header=None)
DATA_5 = pd.concat([DATA_51] * 7, ignore_index=True)
Data_position5=np.arange(0,len(DATA_5),1)
DATA_5.insert(3,'3',Data_position5)
ALT5=DATA_5.iloc[:,3]
AVTEC5=DATA_5.iloc[:,1]
SVTEC5=DATA_5.iloc[:,2]

DATA_PATH_6 = PWD+'AVG_STD_VTEC_RANDOM_BAN.txt'
DATA_61 = pd.read_csv(DATA_PATH_6, delimiter='\t', header=None)
DATA_6 = pd.concat([DATA_61] * 7, ignore_index=True)
Data_position6=np.arange(0,len(DATA_6),1)
DATA_6.insert(3,'3',Data_position6)
ALT6=DATA_6.iloc[:,3]
AVTEC6=DATA_6.iloc[:,1]
SVTEC6=DATA_6.iloc[:,2]

DATA_PATH_7 = PWD+'AVG_STD_VTEC_RANDOM_HYD.txt'
DATA_71 = pd.read_csv(DATA_PATH_7, delimiter='\t', header=None)
DATA_7 = pd.concat([DATA_71] * 7, ignore_index=True)
Data_position7=np.arange(0,len(DATA_7),1)
DATA_7.insert(3,'3',Data_position7)
ALT7=DATA_7.iloc[:,3]
AVTEC7=DATA_7.iloc[:,1]
SVTEC7=DATA_7.iloc[:,2]

DATA_PATH_8 = PWD+'AVG_STD_VTEC_RANDOM_LCK.txt'
DATA_81 = pd.read_csv(DATA_PATH_8, delimiter='\t', header=None)
DATA_8 = pd.concat([DATA_81] * 7, ignore_index=True)
Data_position8=np.arange(0,len(DATA_8),1)
DATA_8.insert(3,'3',Data_position8)
ALT8=DATA_8.iloc[:,3]
AVTEC8=DATA_8.iloc[:,1]
SVTEC8=DATA_8.iloc[:,2]


FOLDER11 = 'CONSOLIDATED_VTEC_TIME_SERIES'
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1


rc('font', weight='bold')
rc('axes', linewidth=3) 
fig = plt.figure(figsize=(18, 10))
gs = fig.add_gridspec(4, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)
# Plotting the error bar
light_green = (152/255, 251/255, 152/255)
axs[0].errorbar(ALT5, AVTEC5, SVTEC5, linestyle='-', marker='o', markersize=1,
                  markeredgecolor='blue', markerfacecolor='blue', color=light_green, linewidth=2)
axs[0].plot(VTEC1, lw=2, color='red')
axs[0].set_ylabel("VTEC\n(TECU)", fontsize=21, fontweight="bold")
axs[0].yaxis.set_label_position("left")
axs[0].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
   
axs[0].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[0].margins(x=0)
axs[0].text(.1, 0.8, '(a)', horizontalalignment='left', transform=axs[0].transAxes, fontsize=21, fontweight="bold",
                color='black')
axs[0].set_ylim(ymin=0,ymax=120)
axs[0].set_xlim(xmin=0, xmax=20160)


axs[1].errorbar(ALT6, AVTEC6, SVTEC6, linestyle='-', marker='o', markersize=1,
                  markeredgecolor='blue', markerfacecolor='blue', color=light_green, linewidth=2)
axs[1].plot(VTEC2, lw=2, color='red')
axs[1].set_ylabel("VTEC\n(TECU)", fontsize=21, fontweight="bold")
axs[1].yaxis.set_label_position("left")
axs[1].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
   
axs[1].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[1].margins(x=0)
axs[1].text(.1, 0.8, '(b)', horizontalalignment='left', transform=axs[1].transAxes, fontsize=21, fontweight="bold",
                color='black')
axs[1].set_ylim(ymin=0,ymax=120)
axs[1].set_xlim(xmin=0, xmax=20160)

axs[2].errorbar(ALT7, AVTEC7, SVTEC7, linestyle='-', marker='o', markersize=1,
                  markeredgecolor='blue', markerfacecolor='blue', color=light_green, linewidth=2)
axs[2].plot(VTEC3, lw=2, color='red')
axs[2].set_ylabel("VTEC\n(TECU)", fontsize=21, fontweight="bold")
axs[2].yaxis.set_label_position("left")
axs[2].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
   
axs[2].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[2].margins(x=0)
axs[2].text(.1, 0.8, '(c)', horizontalalignment='left', transform=axs[2].transAxes, fontsize=21, fontweight="bold",
                color='black')
axs[2].set_ylim(ymin=0,ymax=120)
axs[2].set_xlim(xmin=0, xmax=20160)

axs[3].errorbar(ALT8, AVTEC8, SVTEC8, linestyle='-', marker='o', markersize=1,
                  markeredgecolor='blue', markerfacecolor='blue', color=light_green, linewidth=2)
axs[3].plot(VTEC4, lw=2, color='red')
axs[3].set_ylabel("VTEC\n(TECU)", fontsize=21, fontweight="bold")
axs[3].yaxis.set_label_position("left")
axs[3].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[3].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[3].margins(x=0)
axs[3].text(.1, 0.8, '(d)', horizontalalignment='left', transform=axs[3].transAxes, fontsize=21, fontweight="bold",
                color='black')
axs[3].set_ylim(ymin=0,ymax=120)
axs[3].set_xlim(xmin=0, xmax=20160)
axs[3].set_xticks(np.arange(0, 20160, 2880))
labels=['00','00','00', '00', '00', '00', '00']
axs[3].set_xticklabels(labels, fontsize=21, fontweight="bold")
axs[3].set_xticks(np.arange(1440, 20160, 2880), minor=True)
labels2=['12\n25/02','12\n26/02','12\n27/02', '12\n28/02', '12\n01/03', '12\n02/03', '12\n03/03']
axs[3].set_xticklabels(labels2, fontsize=21, fontweight="bold", minor=True)
axs[3].set_xlabel('Date and Time (LT)', fontsize=21, fontweight="bold")
fig.tight_layout()
GNAME3 = 'STACKED_1.jpeg'
GNAME31 = PATH_TO_FOLDER1 + GNAME3
plt.savefig(GNAME31, dpi=600, bbox_inches='tight')
   
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 17-05-2022---------------------------SREEKUMAR HARIDAS--------------------