# THIS IS A SIMPLE PYTHON PROGRAM WHICH PLOT PARAMETERS OBTAINED FROM SWARM DATA
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
from matplotlib import ticker
#----------------------------------SECTION 1--USER INPUTS---------------------------------------------------------------
input_log = {}
DATE = input("ENTER THE DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
#print(PWD)
while True:
    SPACECRAFT = input("PLEASE ENTER THE SWARM SPACECRAFT (ENTER YOUR CHOICE: A. SWARM-A/ B. SWARM-B/ C. SWARM-C):")
# ----------------------------------SECTION 1A---SAVING OF ENTERED PARAMETERS-------------------------------------------
    for variable in ["DATE", "SPACECRAFT"]:
        input_log[variable] = eval(variable)
    with open("INPUT_LOG_SWARM_PARAMETERS_PLOT.txt", 'w') as f:
        str_input_log = repr(input_log)
        f.write("input_log = " + str_input_log + "\n")
    # ----------------------------------SECTION 1A---SAVING OF ENTERED PARAMETERS IS OVER-------------------------------
    if SPACECRAFT in ('a', 'A', 'b', 'B', 'c', 'C'):
        break
    else:
        print("\nSORRY ENTERED CODE DOES NOT MATCH WITH AVAILABLE STATIONS,PLEASE TRY WITH VALID CODE IN THE INSTRUCTIONS")
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


data = pd.read_csv('SWARM_C_15_Jan_2022_22_LT_Ne_LON_74_75.txt', delimiter='\t', header=None)
data = data.replace([-35],[np.nan])
LT = data.iloc[:,0]
LATITUDE = data.iloc[:,2]
NE=data.iloc[:,3]
logNe=np.log10(NE)
Te=data.iloc[:,13]

data2 = pd.read_csv('SWARM_C_15_Jan_2022_22_LT_Ne_LON_74_75_PRN.txt', delimiter='\t', header=None)
#data2 = data2.replace([-34.982,34.971],[np.nan,np.nan])
LT2 = data2.iloc[:,0]
LATITUDE2 = data2.iloc[:,2]
LONGITUDE2 = data2.iloc[:,3]
PRN=data2.iloc[:,4]
TEC=data2.iloc[:,5]
PRNLIST=list(set(PRN))
rc('font', weight='bold')
rc('axes', linewidth=3)
fig = plt.figure(figsize=(20, 16))
gs = fig.add_gridspec(3, hspace=0)
axs = gs.subplots(sharex=True, sharey=False)
axs[0].plot(LATITUDE,logNe,linestyle='-',lw=2,color='red',label='Ne')
axs[0].set_ylabel("log$_{10}$Ne (cm$^{-3}$)", fontsize=28, fontweight="bold")
axs[0].yaxis.set_label_position("left")
axs[0].tick_params(direction='in', labelsize=28, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[0].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[0].text(.1, 0.8, '(a)',horizontalalignment='left', transform= axs[0].transAxes, fontsize=28, fontweight="bold", color='black')
axs[0].margins(x=0)
axs[0].set_ylim(ymin=2, ymax=6)
axs[0].legend(frameon=False, loc=0,ncol=3, fontsize=21,markerscale=15)
axs[1].plot(LATITUDE,Te,linestyle='-',lw=2,color='blue',label='Te')
axs[1].set_ylabel("Te (K)", fontsize=28, fontweight="bold")
axs[1].yaxis.set_label_position("left")
axs[1].tick_params(direction='in', labelsize=28, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[1].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[1].text(.1, 0.8, '(b)',horizontalalignment='left', transform= axs[1].transAxes, fontsize=28, fontweight="bold", color='black')
axs[1].margins(x=0)
axs[1].set_ylim(ymin=500, ymax=3900)
axs[1].legend(frameon=False, loc=0,ncol=3, fontsize=28,markerscale=15)
for PRNNEW in PRNLIST: 
    print(PRNNEW)
    labl='PRN-'+str(PRNNEW)
    data1=data2.loc[PRN==PRNNEW]
    LAT1 = data1.iloc[:,2]
    TEC1=data1.iloc[:,5]    
    axs[2].plot(LAT1,TEC1,'.',markersize=3, label=labl)
    axs[2].set_ylabel("aVTEC (TECU)", fontsize=28, fontweight="bold")
    axs[2].yaxis.set_label_position("left")
    axs[2].tick_params(direction='in', labelsize=28, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
    axs[2].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[2].text(.1, 0.5, '(c)',horizontalalignment='left', transform= axs[2].transAxes, fontsize=28, fontweight="bold", color='black')
    axs[2].margins(x=0)
    axs[2].set_ylim(ymin=0, ymax=14.5)
    axs[2].set_xlabel('Geographic Latitude (degree)', fontsize=32, fontweight="bold")
axs[2].legend(frameon=False, loc=0,ncol=3, fontsize=21,markerscale=15)
fig.tight_layout()
GNAME11 = 'STACKED_2.png'
GNAME21 = 'STACKED_2.pdf'
GNAME31 = 'STACKED_2.jpeg'
GNAME41 = 'STACKED_2.svg'
GNAME111 = PATH_SUBFOLDER1 + GNAME11
GNAME211 = PATH_SUBFOLDER2 + GNAME21
GNAME311 = PATH_SUBFOLDER3 + GNAME31
GNAME411 = PATH_SUBFOLDER4 + GNAME41
plt.savefig(GNAME111, dpi=500, bbox_inches='tight')
plt.savefig(GNAME211, dpi=500, bbox_inches='tight')
plt.savefig(GNAME311, dpi=600, bbox_inches='tight')
plt.savefig(GNAME411, dpi=300, bbox_inches='tight')

#--------------------------------------SECTION 3----PLOTTING OF SWARM_PARAMETERS IS BEGINS HERE-------------------------
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
#--------------------------------------SECTION 3------------------------------------------------------------------------
#---------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
#-------------------------------------------ON 13-01-2022---------------------------SREEKUMAR HARIDAS-------------------































