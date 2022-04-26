# THIS IS A SIMPLE PYTHON PROGRAM WHICH PLOT LT BASED VTEC
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
from scipy.signal import savgol_filter
PWD1 = os.getcwd()
PWD = PWD1+'/'
FOLDER1 = PWD + 'PLOTS/'
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
NAME_SUBFOLDER1 = 'FIGURE_PNG'
NAME_SUBFOLDER2 = 'FIGURE_PDF'
NAME_SUBFOLDER3 = 'FIGURE_PS'
NAME_SUBFOLDER4 = 'FIGURE_SVG'
SUBFOLDER1 = PATH_TO_FOLDER1+NAME_SUBFOLDER1
os.makedirs(SUBFOLDER1)
PATH_SUBFOLDER1 = SUBFOLDER1 + '/'
SUBFOLDER2 = PATH_TO_FOLDER1+NAME_SUBFOLDER2
os.makedirs(SUBFOLDER2)
PATH_SUBFOLDER2 = SUBFOLDER2 + '/'
SUBFOLDER3 = PATH_TO_FOLDER1+NAME_SUBFOLDER3
os.makedirs(SUBFOLDER3)
PATH_SUBFOLDER3 = SUBFOLDER3 + '/'
SUBFOLDER4 = PATH_TO_FOLDER1+NAME_SUBFOLDER4
os.makedirs(SUBFOLDER4)
PATH_SUBFOLDER4 = SUBFOLDER4 + '/'


data = pd.read_csv('I08220115_LT_BASED.txt', delimiter='\t', header=None)
data14 = pd.read_csv('I08220114_LT_BASED.txt', delimiter='\t', header=None)
data16 = pd.read_csv('I08220116_LT_BASED.txt', delimiter='\t', header=None)



LT = data.iloc[:,2]
VTEC1= data.iloc[:,3]
VTEC= savgol_filter(VTEC1, 51, 2)


data[5]=VTEC
MASK1_START = (data[2] == 19.35)
MASK2_PEAK = (data[2] == 20.583)
MASK3_END = (data[2] == 22.067)
VTEC1_START=data[5].loc[MASK1_START]
VTEC2_PEAK=data[5].loc[MASK2_PEAK]
VTEC3_END=data[5].loc[MASK3_END]

point1_start = [19.35,0]
point2_start = [19.35,VTEC1_START]
x_values_start = [point1_start[0], point2_start[0]]
y_values_start = [point1_start[1], point2_start[1]]

point1_end = [22.067,0]
point2_end = [22.067,VTEC3_END]
x_values_end = [point1_end[0], point2_end[0]]
y_values_end = [point1_end[1], point2_end[1]]

point1_peak = [20.583,0]
point2_peak = [20.583,VTEC2_PEAK]
x_values_peak = [point1_peak[0], point2_peak[0]]
y_values_peak = [point1_peak[1], point2_peak[1]]


LT14 = data14.iloc[:,2]
VTEC141= data14.iloc[:,3]
VTEC14= savgol_filter(VTEC141, 51, 2)
LT16 = data16.iloc[:,2]
VTEC161= data16.iloc[:,3]
VTEC16= savgol_filter(VTEC161, 51, 2)

data16[5]=VTEC16
MASK1_START16 = (data16[2] == 10.467)
MASK2_PEAK16 = (data16[2] == 11.233)
MASK3_END16 = (data16[2] == 12.5)
VTEC1_START16=data16[5].loc[MASK1_START16]
VTEC2_PEAK16=data16[5].loc[MASK2_PEAK16]
VTEC3_END16=data16[5].loc[MASK3_END16]

point1_start16 = [10.467,0]
point2_start16 = [10.467,VTEC1_START16]
x_values_start16 = [point1_start16[0], point2_start16[0]]
y_values_start16 = [point1_start16[1], point2_start16[1]]

point1_end16 = [12.5,0]
point2_end16 = [12.5,VTEC3_END16]
x_values_end16 = [point1_end16[0], point2_end16[0]]
y_values_end16 = [point1_end16[1], point2_end16[1]]

point1_peak16 = [11.233,0]
point2_peak16 = [11.233,VTEC2_PEAK16]
x_values_peak16 = [point1_peak16[0], point2_peak16[0]]
y_values_peak16 = [point1_peak16[1], point2_peak16[1]]


MASK1_START111 = (data[2] == 20.567)
VTEC1_START111=data[5].loc[MASK1_START111]

MASK1_START161 = (data16[2] == 10)
VTEC1_START161=data16[5].loc[MASK1_START161]

rc('font', weight='bold')
rc('axes', linewidth=5)
VTEC_MAX = max(VTEC)
ylimit1 = ((VTEC_MAX // 10) * 10) + 10
ylimit = int(ylimit1)
plt.figure(figsize=(10, 6))
plt.plot(LT14, VTEC14, lw=1.5, color='blue')
plt.plot(LT, VTEC, lw=1.5, color='green')
plt.plot(LT16, VTEC16, lw=1.5, color='red')
plt.plot(x_values_start, y_values_start, 'bo', linestyle="--",lw=1, color='green')
plt.plot(x_values_end, y_values_end, 'bo', linestyle="--",lw=1, color='green')
plt.plot(x_values_peak, y_values_peak, 'bo', linestyle=":",lw=1, color='green')

plt.plot(x_values_start16, y_values_start16, 'bo', linestyle="--",lw=1, color='red')
plt.plot(x_values_end16, y_values_end16, 'bo', linestyle="--",lw=1, color='red')
plt.plot(x_values_peak16, y_values_peak16, 'bo', linestyle=":",lw=1, color='red')

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
#plt.text(point2_start[0],point2_start[1],'15 A')
#plt.text(point2_peak[0],point2_peak[1],'15 PEAK')
#plt.text(point2_end[0],point2_end[1],'15 B')

# plt.annotate('15 A',(point2_start[0],point2_start[1]),textcoords="offset points",xytext=(-30,-10),ha='left')
# plt.annotate('15 PEAK',(point2_peak[0],point2_peak[1]),textcoords="offset points",xytext=(0,-10),ha='left')
# plt.annotate('15 B',(point2_end[0],point2_end[1]),textcoords="offset points",xytext=(0,-10),ha='left')
#
#
# plt.annotate('16 A',(point2_start16[0],point2_start16[1]),textcoords="offset points",xytext=(-30,-10),ha='left')
# plt.annotate('16 PEAK',(point2_peak16[0],point2_peak16[1]),textcoords="offset points",xytext=(3,-5),ha='left')
# plt.annotate('16 B',(point2_end16[0],point2_end16[1]),textcoords="offset points",xytext=(0,-10),ha='left')
plt.annotate('First Hit at Cochin', xy=(20.567, VTEC1_START111), xytext=(19, 40), fontsize=12,
            arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('Second Hit at Cochin', xy=(10.20, VTEC1_START161), xytext=(3, 35), fontsize=12,
            arrowprops=dict(facecolor='green', shrink=0.05))
plt.legend(['14$^{th}$ January 2022','15$^{th}$ January 2022','16$^{th}$ January 2022'], frameon=False, loc='upper left', fontsize=14,markerscale=15)
plt.tight_layout()
GNAME11 = 'VTEC.png'
GNAME21 = 'VTEC.pdf'
GNAME31 = 'VTEC.jpeg'
GNAME41 = 'VTEC.svg'
GNAME111 = PATH_SUBFOLDER1 + GNAME11
GNAME211 = PATH_SUBFOLDER2 + GNAME21
GNAME311 = PATH_SUBFOLDER3 + GNAME31
GNAME411 = PATH_SUBFOLDER4 + GNAME41
plt.savefig(GNAME111, dpi=500, bbox_inches='tight')
plt.savefig(GNAME211, dpi=500, bbox_inches='tight')
plt.savefig(GNAME311, dpi=600, bbox_inches='tight')
plt.savefig(GNAME411, dpi=300, bbox_inches='tight')
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
#--------------------------------------SECTION 3------------------------------------------------------------------------
#---------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
#-------------------------------------------ON 18-02-2022---------------------------SREEKUMAR HARIDAS-------------------































