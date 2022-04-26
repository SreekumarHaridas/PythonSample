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
LT = data.iloc[:,2]
VTEC1= data.iloc[:,3]
VTEC= savgol_filter(VTEC1, 51, 2)
rc('font', weight='bold')
rc('axes', linewidth=5)
VTEC_MAX = max(VTEC)
ylimit1 = ((VTEC_MAX // 10) * 10) + 10
ylimit = int(ylimit1)
plt.figure(figsize=(10, 6))
plt.plot(LT, VTEC, lw=1.5, color='blue')
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































