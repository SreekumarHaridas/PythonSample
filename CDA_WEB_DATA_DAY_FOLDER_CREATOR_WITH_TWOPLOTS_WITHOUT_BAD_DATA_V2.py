# THIS IS A SIMPLE PYTHON PROGRAM WHICH SPLITS THE DATA (WITH ELIMINATING BAD DATA) INTO DAY WISE FILES WITH PLOTS
# AND SAVE THEM IN RESPECTIVE DATE FOLDERS IN PWD, FOR ONE YEAR.
# THE DATA CSV FILE IS DOWNLOADED FROM "https://cdaweb.gsfc.nasa.gov/index.html/"
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
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
startday1 = input("ENTER THE START DATE (AS dd-mm-yyyy): ")
endday1 = input("ENTER THE END DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["startday1", "endday1"]:
    input_log[variable] = eval(variable)
with open("INPUT_LOG_CDA_WEB_DATA_DAY_FOLDER_CREATOR_WITH_TWOPLOTS_WITHOUT_BAD_DATA.txt", 'w') as f1:
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
# --------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
# --------------------------------------------SECTION 3- SAVING THE DATA OF EACH DAY IN TO RESPECTIVE DATE FOLDERS------
for DATES1 in DATE_LIST:
    DATES = str(DATES1)
    try:
        DATES1 = datetime.strptime(DATES, '%Y-%m-%d')
        DATES_NEW_FORMAT = DATES1.strftime('%d-%m-%Y')
        DATES_NEW_FORMAT2 = DATES1.strftime('%d_%m_%Y')
        DATES_NEW_FORMAT3 = DATES1.strftime('%d/%m/%Y')
        SINGLE_DAY_DATA = DATA.loc[DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(DATES)]
        kkk = pd.to_datetime(DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'], format='%Y-%m-%dT%H:%M:%S.%fZ')
        DECIMAL_TIME = {} # CONVERTING "EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ" TO hh.hh DECIMAL HOUR
        for i in kkk:
            i = str(i)
            DECIMAL_TIME1 = dateutil.parser.parse(i)
            DECIMAL_TIME2 = DECIMAL_TIME1.strftime('%H:%M:%S')
            (h, m, s) = DECIMAL_TIME2.split(':')
            s1 = int(s) / 60
            m1 = int(m) + s1
            m2 = m1 / 60
            DECIMAL_TIME[i] = int(h) + m2
            # DECIMAL_TIME[i] = int(h) + int(m) / 60 + int(s) / 60
        DECIMAL_HOUR1 = DECIMAL_TIME.values()
        DECIMAL_HOUR = list(DECIMAL_HOUR1)
        DATA['TIME'] = DECIMAL_HOUR
        SINGLE_DAY_DATA2 = DATA.loc[DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'].str.contains(DATES)]
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
        print("\nSAVING DATA IN TO FILES NAMED '",FILENAME11,"'AND'",FILENAME22,"'IN THE FOLDER '",DATES_NEW_FORMAT2,"'............")
        FILENAME33 = 'DATA_WITH_DECIMAL_TIME_{}.csv'.format(DATES_NEW_FORMAT2)
        FILENAME3 = PATH_TO_DATE_FOLDER + FILENAME33
        FILENAME44 = 'DATA_WITH_DECIMAL_TIME_{}.txt'.format(DATES_NEW_FORMAT2)
        FILENAME4 = PATH_TO_DATE_FOLDER + FILENAME44
        SINGLE_DAY_DATA2.to_csv(FILENAME3, index=False)
        SINGLE_DAY_DATA2.to_csv(FILENAME4, index=False)
        print("\nSAVING DATA IN TO FILES NAMED '",FILENAME33, "'AND'",FILENAME44,"'IN THE FOLDER '",DATES_NEW_FORMAT2,"'............")
        UT1 = SINGLE_DAY_DATA2['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ']
        UT2 = SINGLE_DAY_DATA2['TIME']
        BZ = SINGLE_DAY_DATA2['BZ__GSE_nT']
        FLOW_SPEED = SINGLE_DAY_DATA2['FLOW_SPEED__GSE_km/s']
        FLOW_PRESSURE = SINGLE_DAY_DATA2['FLOW_PRESSURE_nPa']
        ELECTRIC_FIELD = SINGLE_DAY_DATA2['ELECTRIC_FIELD_mV/m']
        AE = SINGLE_DAY_DATA2['5-M_AE_nT']
        AL = SINGLE_DAY_DATA2['5-M_AL-INDEX_nT']
        SYMH_INDEX = SINGLE_DAY_DATA2['SYM/H_INDEX_nT']
        PC_INDEX = SINGLE_DAY_DATA2['5-M_PC(N)-INDEX_']
        # print(list(np.arange(0, 25, 1)))
        # ----------------------------------SECTION 3.1 PLOTTING THE PARAMETERS-----------------------------------------
        # -----------------------------------------------STACK PLOT-----------------------------------------------------
        try:
            print("\nTHE PARAMETERS FOR '",DATES_NEW_FORMAT3,"'ARE PLOTTING NOW.....DO NOT CLOSE THE PROGRAM UNTIL IT IS COMPLETE")
            rc('font', weight='bold')
            #fig = plt.figure(figsize=(8, 12))
            fig = plt.figure(figsize=(9, 16))
            gs = fig.add_gridspec(8, hspace=0)
            axs = gs.subplots(sharex=True, sharey=False)
            #fig.suptitle(DATES_NEW_FORMAT3,fontsize=16, fontweight="bold")
            axs[0].plot(UT2, SYMH_INDEX, lw=1.2, color='black')
            axs[0].set_xlim(0, 24)
            axs[0].set_ylabel("SYM-H (nT)", fontsize=12, fontweight="bold")
            axs[0].yaxis.set_label_position("right")
            axs[0].tick_params(direction='in', labelsize=10,length=2, width=2,grid_alpha=0.5, right=True, labelright=True, left=False, labelleft=False)
            axs[0].locator_params(axis="x", nbins=24)
            axs[0].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[1].plot(UT2, BZ,lw=1.2, color='red')
            axs[1].set_xlim(0, 24)
            axs[1].set_ylabel("IMF B$_{Z}$ (nT)", fontsize=12, fontweight="bold")
            axs[1].yaxis.set_label_position("left")
            axs[1].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[1].locator_params(axis="x", nbins=24)
            axs[1].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[2].plot(UT2, FLOW_SPEED, lw=1.2, color='blue')
            axs[2].set_xlim(0, 24)
            axs[2].set_ylabel("V (km/s)", fontsize=12, fontweight="bold")
            axs[2].yaxis.set_label_position("right")
            axs[2].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=True,
                               labelright=True, left=False, labelleft=False)
            axs[2].locator_params(axis="x", nbins=24)
            axs[2].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[3].plot(UT2, FLOW_PRESSURE, lw=1.2, color='green')
            axs[3].set_xlim(0, 24)
            axs[3].set_ylabel("FP (nPa)", fontsize=12, fontweight="bold")
            axs[3].yaxis.set_label_position("left")
            axs[3].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[3].locator_params(axis="x", nbins=24)
            axs[3].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[4].plot(UT2, ELECTRIC_FIELD, lw=1.2, color='black')
            axs[4].set_xlim(0, 24)
            axs[4].set_ylabel("EF(mV/m)", fontsize=12, fontweight="bold")
            axs[4].yaxis.set_label_position("right")
            axs[4].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=True,
                               labelright=True, left=False, labelleft=False)
            axs[4].locator_params(axis="x", nbins=24)
            axs[4].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[5].plot(UT2, AE, lw=1.2, color='red')
            axs[5].set_xlim(0, 24)
            axs[5].set_ylabel("AE (nT)", fontsize=12, fontweight="bold")
            axs[5].yaxis.set_label_position("left")
            axs[5].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[5].locator_params(axis="x", nbins=24)
            axs[5].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[6].plot(UT2, AL, lw=1.2, color='blue')
            axs[6].set_xlim(0, 24)
            axs[6].set_ylabel("AL (nT)", fontsize=12, fontweight="bold")
            axs[6].yaxis.set_label_position("right")
            axs[6].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=True,
                               labelright=True, left=False, labelleft=False)
            axs[6].locator_params(axis="x", nbins=24)
            axs[6].xaxis.grid(which='major', linestyle=':', linewidth=0.6)
            axs[7].plot(UT2,  PC_INDEX, lw=1.2, color='green')
            axs[7].set_xlim(0, 24)
            axs[7].set_ylabel("PC", fontsize=12, fontweight="bold")
            xlab ='UT (hours)\n {}'.format(DATES_NEW_FORMAT3)
            axs[7].set_xlabel(xlab, fontsize=12, fontweight="bold")
            axs[7].yaxis.set_label_position("left")
            axs[7].tick_params(direction='in', labelsize=10, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[7].locator_params(axis="x", nbins=24)
            axs[7].xaxis.grid(which='major', linestyle=':', linewidth=0.6)
        # Hide x labels and tick labels for all but bottom plot.
        #     for ax in axs:
        #         ax.label_outer()
            FOLDER1 = PATH_TO_DATE_FOLDER + 'FIGURES'
            os.makedirs(FOLDER1)
            PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
            NAME_SUBFOLDER1 = 'FIGURE_PNG'
            NAME_SUBFOLDER2 = 'FIGURE_PDF'
            NAME_SUBFOLDER3 = 'FIGURE_JPEG'
            NAME_SUBFOLDER4 = 'FIGURE_SVG'
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
            # -----------SAVING FIGURES IN A COMMON FOLDER ALONG WITH DAY FOLDERS AND THIS PYTHON PROGRAM
            GNAME1 = 'STACK_PLOT_ON_{}.png'.format(DATES_NEW_FORMAT2)
            GNAME2 = 'STACK_PLOT_ON_{}.pdf'.format(DATES_NEW_FORMAT2)
            GNAME3 = 'STACK_PLOT_ON_{}.jpeg'.format(DATES_NEW_FORMAT2)
            GNAME4 = 'STACK_PLOT_ON_{}.svg'.format(DATES_NEW_FORMAT2)
            GNAME11 = PATH_SUBFOLDER1 + GNAME1
            GNAME21 = PATH_SUBFOLDER2 + GNAME2
            GNAME31 = PATH_SUBFOLDER3 + GNAME3
            GNAME41 = PATH_SUBFOLDER4 + GNAME4
            plt.savefig(GNAME11, dpi=500, bbox_inches='tight')
            plt.savefig(GNAME21, dpi=500, bbox_inches='tight')
            plt.savefig(GNAME31, dpi=500, bbox_inches='tight')
            plt.savefig(GNAME41, dpi=300, bbox_inches='tight')
            # ------------------------------------------STACK PLOT------------------------------------------------------
            # ------------------------------------------SUB PLOT--------------------------------------------------------
            fig1 = plt.figure(figsize=(16, 9))
            # gs = fig.add_gridspec(hspace=2)
            # axs = gs.subplots(4,2)
            axs = fig1.subplots(4,2)
            axs[0,0].plot(UT2, SYMH_INDEX, lw=1.2, color='black')
            axs[0,0].set_title("(a) SYM-H vs UT", fontsize=13, fontweight="bold")
            axs[0,0].set_xlim(0, 24)
            axs[0,0].set_ylabel("SYM-H (nT)", fontsize=12, fontweight="bold")
            axs[0,0].yaxis.set_label_position("left")
            axs[0,0].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[0,0].locator_params(axis="x", nbins=24)
            axs[0,0].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[1,0].plot(UT2, AE, lw=1.2, color='green')
            axs[1,0].set_title("(b) AE vs UT", fontsize=13, fontweight="bold")
            axs[1,0].set_xlim(0, 24)
            axs[1,0].set_ylabel("AE (nT)", fontsize=12, fontweight="bold")
            axs[1,0].yaxis.set_label_position("left")
            axs[1,0].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[1,0].locator_params(axis="x", nbins=24)
            axs[1,0].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[2,0].plot(UT2, AL, lw=1.2, color='blue')
            axs[2,0].set_title("(c) AL vs UT", fontsize=13, fontweight="bold")
            axs[2,0].set_xlim(0, 24)
            axs[2,0].set_ylabel("AL (nT)", fontsize=12, fontweight="bold")
            axs[2,0].yaxis.set_label_position("left")
            axs[2,0].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[2,0].locator_params(axis="x", nbins=24)
            axs[2,0].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[3,0].plot(UT2, BZ, lw=1.2, color='red')
            axs[3,0].set_title("(d) IMF B$_{Z}$ vs UT", fontsize=13, fontweight="bold")
            axs[3,0].set_xlim(0, 24)
            axs[3,0].set_ylabel("IMF B$_{Z}$ (nT)", fontsize=12, fontweight="bold")
            xlab1 = 'UT (hours) - {}'.format(DATES_NEW_FORMAT3)
            axs[3,0].set_xlabel(xlab1, fontsize=12, fontweight="bold")
            axs[3,0].yaxis.set_label_position("left")
            axs[3,0].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[3,0].locator_params(axis="x", nbins=24)
            axs[3,0].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[0,1].plot(UT2, FLOW_SPEED, lw=1.2, color='black')
            axs[0,1].set_title("(e) FLOW SPEED vs UT", fontsize=13, fontweight="bold")
            axs[0,1].set_xlim(0, 24)
            axs[0,1].set_ylabel("V (km/s)", fontsize=12, fontweight="bold")
            axs[0,1].yaxis.set_label_position("left")
            axs[0,1].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[0,1].locator_params(axis="x", nbins=24)
            axs[0,1].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[1,1].plot(UT2, FLOW_PRESSURE, lw=1.2, color='green')
            axs[1,1].set_title("(f) FLOW PRESSURE vs UT", fontsize=13, fontweight="bold")
            axs[1,1].set_xlim(0, 24)
            axs[1,1].set_ylabel("FP (nPa)", fontsize=12, fontweight="bold")
            axs[1,1].yaxis.set_label_position("left")
            axs[1,1].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[1,1].locator_params(axis="x", nbins=24)
            axs[1,1].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[2,1].plot(UT2, ELECTRIC_FIELD, lw=1.2, color='blue')
            axs[2,1].set_title("(g) ELECTRIC FIELD vs UT", fontsize=13, fontweight="bold")
            axs[2,1].set_xlim(0, 24)
            axs[2,1].set_ylabel("EF(mV/m)", fontsize=12, fontweight="bold")
            axs[2,1].yaxis.set_label_position("left")
            axs[2,1].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[2,1].locator_params(axis="x", nbins=24)
            axs[2,1].xaxis.grid(which='major', linestyle=':', linewidth=0.6)

            axs[3,1].plot(UT2, PC_INDEX, lw=1.2, color='red')
            axs[3,1].set_title("(h)  PC Index vs UT", fontsize=13, fontweight="bold")
            axs[3,1].set_xlim(0, 24)
            axs[3,1].set_ylabel("PC", fontsize=12, fontweight="bold")
            xlab2 = 'UT (hours) - {}'.format(DATES_NEW_FORMAT3)
            axs[3,1].set_xlabel(xlab2, fontsize=12, fontweight="bold")
            axs[3,1].yaxis.set_label_position("left")
            axs[3,1].tick_params(direction='in', labelsize=12, length=2, width=2, grid_alpha=0.5, right=False,
                               labelright=False, left=True, labelleft=True)
            axs[3,1].locator_params(axis="x", nbins=24)
            axs[3,1].xaxis.grid(which='major', linestyle=':', linewidth=0.6)
            fig1.tight_layout()
            GNAME11 = 'SUB_PLOT_ON_{}.png'.format(DATES_NEW_FORMAT2)
            GNAME22 = 'SUB_PLOT_ON_{}.pdf'.format(DATES_NEW_FORMAT2)
            GNAME33 = 'SUB_PLOT_ON_{}.jpeg'.format(DATES_NEW_FORMAT2)
            GNAME44 = 'SUB_PLOT_ON_{}.svg'.format(DATES_NEW_FORMAT2)
            GNAME111 = PATH_SUBFOLDER1 + GNAME11
            GNAME212 = PATH_SUBFOLDER2 + GNAME22
            GNAME313 = PATH_SUBFOLDER3 + GNAME33
            GNAME414 = PATH_SUBFOLDER4 + GNAME44
            fig1.savefig(GNAME111, dpi=500, bbox_inches='tight')
            fig1.savefig(GNAME212, dpi=500, bbox_inches='tight')
            fig1.savefig(GNAME313, dpi=500, bbox_inches='tight')
            fig1.savefig(GNAME414, dpi=300, bbox_inches='tight')
            # ------------------------------------------SUB PLOT--------------------------------------------------------
        except OSError:
            print("\nSOME DATES WERE MISSING")
    # ----------------------------------SECTION 3.1_PLOTTING IS OVER----------------------------------------------------
    except OSError:
        print("\nSOME DATES WERE MISSING")
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes....................!!!!!!!!!" %((time.time() - start)/60))
# -------------------------------------SECTION 3 IS OVER----------------------------------------------------------------
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 29-05-2021---------------------------SREEKUMAR HARIDAS--------------------