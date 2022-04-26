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

data = pd.read_csv('SWARM_B_24_Nov_2020_22_LT_Ne_LON_76_79.txt', delimiter='\t', header=None)
LT = data.iloc[:,0]
LATITUDE = data.iloc[:,2]
LONGITUDE = data.iloc[:,4]
NE=data.iloc[:,3]
bNE=data.iloc[:,5]
ROD=abs(data.iloc[:,6])
RODI20s=data.iloc[:,8]
mVTEC=data.iloc[:,9]
mROT=abs(data.iloc[:,10])
mROTI10s=data.iloc[:,11]
mROTI20s=data.iloc[:,12]
Te=data.iloc[:,13]
aVTEC=data.iloc[:,14]

Bubble_Index11=data.iloc[:,15]
Bubble_Probability11=data.iloc[:,16]

rc('font', weight='bold')
fig = plt.figure(figsize=(16, 20))
gs = fig.add_gridspec(5, hspace=0.15)
axs = gs.subplots(sharex=True, sharey=False)
axs[0].plot(LT,NE,'.',markersize=1,color='red',label='Ne')
axs[0].plot(LT,bNE,'.',markersize=1,color='black',label='bNe')
axs[0].set_ylabel("Ne (cm$^{-3}$)", fontsize=21, fontweight="bold")
axs[0].yaxis.set_label_position("left")
axs[0].tick_params(direction='in', labelsize=21, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs[0].yaxis.set_major_formatter(formatter)
axs[0].yaxis.get_offset_text().set_fontsize(21)
axs[0].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[0].text(.1, 0.8, '(a)',horizontalalignment='left', transform= axs[0].transAxes, fontsize=21, fontweight="bold", color='black')
axs[0].margins(x=0)
axs[0].set_ylim(ymin=0)
axs2 = axs[0].twinx()
axs2.plot(LT,Te,'.',markersize=1,color='blue', label='Te')
axs2.set_ylabel("Te (K)", fontsize=21, fontweight="bold", color='blue')
axs2.yaxis.set_label_position("right")
axs2.tick_params(direction='in', labelcolor='blue',labelsize=21, length=2, width=2, grid_alpha=0.5, right=True, labelright=True,
                       left=False, labelleft=False)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs2.yaxis.set_major_formatter(formatter)
axs2.yaxis.get_offset_text().set_fontsize(21)
axs2.xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs2.margins(x=0)
axs2.set_ylim(ymin=0)
axs[0].legend(['Ne','bNe'], frameon=False, loc=0,ncol=3, fontsize=16,markerscale=15)
axs2.legend(['Te'], frameon=False, loc=7, fontsize=16,markerscale=15)

axs[1].plot(LT,ROD,lw=1.2, color='green', label='ROD')
axs[1].plot(LT,RODI20s,'.',markersize=2.5,color='red',label='RODI')
axs[1].set_ylabel("ROD & \n RODI (cm$^{-3}$/s)", fontsize=21, fontweight="bold")
axs[1].yaxis.set_label_position("left")
axs[1].tick_params(direction='in', labelsize=21, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs[1].yaxis.set_major_formatter(formatter)
axs[1].yaxis.get_offset_text().set_fontsize(21)
axs[1].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[1].text(.1, 0.8, '(b)',horizontalalignment='left', transform= axs[1].transAxes, fontsize=21, fontweight="bold", color='black')
axs[1].margins(x=0)
axs[1].set_ylim(ymin=0.0)
axs[1].legend(['ROD','RODI'], frameon=False, loc=0,ncol=3, fontsize=16,markerscale=15)

axs[2].plot(LT,mVTEC,'.',markersize=2.5,color='black',label='mVTEC')
axs[2].plot(LT,aVTEC,'.',markersize=2.5,color='blue',label='aVTEC')
axs[2].set_ylabel("mVTEC & \naVTEC (TECU)", fontsize=21, fontweight="bold")
axs[2].yaxis.set_label_position("left")
axs[2].tick_params(direction='in', labelsize=21, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[2].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[2].text(.1, 0.8, '(c)',horizontalalignment='left', transform= axs[2].transAxes, fontsize=21, fontweight="bold", color='black')
axs[2].margins(x=0)
axs[2].set_ylim(ymin=0)
axs[2].legend(['mVTEC','Absolute VTEC'], frameon=False, loc=0,ncol=3, fontsize=16,markerscale=15)

# axs[3].plot(LT,mROT,'.',markersize=1,color='black',label='mROT')
# axs[3].plot(LT,mROTI20s,'.',markersize=1,color='blue',label='mROTI20s')
axs[3].plot(LT,mROT,lw=1.2, color='red', label='mROT')
axs[3].plot(LT,mROTI20s,'.',markersize=2.5,color='green',label='mROTI20s')
axs[3].set_ylabel("mROT & \nmROTI (TECU/s)", fontsize=21, fontweight="bold")
axs[3].yaxis.set_label_position("left")
axs[3].tick_params(direction='in', labelsize=21, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[3].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[3].tick_params(axis='x', which='minor', labelsize=21)
axs[3].text(.1, 0.8, '(d)',horizontalalignment='left', transform= axs[3].transAxes, fontsize=21, fontweight="bold", color='black')
axs[3].legend(['mROT','mROTI'], frameon=False, loc=6,ncol=3,fontsize=16,markerscale=15)
axs[3].margins(x=0)
axs[3].set_ylim(ymin=0.00)

axs[4].plot(LT,Bubble_Index11,'.',markersize=2.5, color='red', label='Bubble Index')
axs[4].plot(LT,Bubble_Probability11,lw=1.2, color='black',label='Bubble Probability')
axs[4].set_ylabel("Bubble Index & \n Probability", fontsize=21, fontweight="bold")
axs[4].yaxis.set_label_position("left")
axs[4].tick_params(direction='in', labelsize=21, length=3,width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
axs[4].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
axs[4].tick_params(axis='x', which='minor', labelsize=21)
axs[4].text(.1, 0.8, '(e)',horizontalalignment='left', transform= axs[4].transAxes, fontsize=21, fontweight="bold", color='black')
axs[4].legend(['Bubble Index','Bubble Probability'], frameon=False, loc=1,ncol=2,fontsize=16,markerscale=15)
axs[4].margins(x=0)
axs[4].set_ylim(ymin=-2, ymax=2)
axs[4].set_xlabel('Local Time (IST hours)', fontsize=21, fontweight="bold")
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
#-------------------------------------------ON 24-08-2021---------------------------SREEKUMAR HARIDAS-------------------































