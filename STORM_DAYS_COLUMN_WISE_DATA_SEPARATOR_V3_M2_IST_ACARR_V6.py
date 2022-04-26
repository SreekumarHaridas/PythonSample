# THIS IS A SIMPLE PYTHON PROGRAM WHICH SEPARATES THE COLUMN WISE DATA OF ENTERED PERIOD OF STORM EVENTS INTO ".csv"
# AND ".txt" FILES
# PARAMETERS IN EACH COLUMNS WILL PLOT (vs IST ) IN VERTICALLY STACKED MANNER WITHOUT GAP AND WITH GAP AND SAVING THEM IN FOLDERS STACKED_1 AND STACKED_2
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
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
startday1 = input("ENTER THE START DATE (AS dd-mm-yyyy): ")
endday1 = input("ENTER THE END DATE (AS dd-mm-yyyy): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["startday1", "endday1"]:
    input_log[variable] = eval(variable)
with open("STORM_DAYS_COLUMN_WISE_DATA_SEPARATOR_V3_M2_IST_ACARR_V6.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
DATA_PATH = PWD+'OMNI_HRO_1MIN_80295.csv'
DATA = pd.read_csv(DATA_PATH, header=0, comment='#') # SETTING "comment='#'" WE ELIMINATE THE COMMENTS STARTS WITH # IN THE DATA FILE TO BE LOADED
# DATA = DATA.replace([99.99,999.99,9999.99,99999.9],[math.nan,math.nan,math.nan,math.nan])
DATA = DATA.replace([99.99,999.99,9999.99,99999.9],[np.nan,np.nan,np.nan,np.nan]) # ELIMINATING BAD DATA IN DATAFRAME

DATA_PATH2 = PWD+'OMNI2_H0_MRG1HR_82456.csv'
DATA12 = pd.read_csv(DATA_PATH2, header=0, comment='#') # SETTING "comment='#'" WE ELIMINATE THE COMMENTS STARTS WITH # IN THE DATA FILE TO BE LOADED
# DATA12 = DATA12.replace([99.99,999.99,9999.99,99999.9],[math.nan,math.nan,math.nan,math.nan])
DATA12 = DATA12.replace([99.99,999.99,9999.99,99999.9],[np.nan,np.nan,np.nan,np.nan]) # ELIMINATING BAD DATA IN DATAFRAME
# ---------------------------------SECTION 1--OVER----------------------------------------------------------------------
# --------------------------------------------------SECTION 2-----------------------------------------------------------
# CONVERTING ENTERED DATE FORMAT '%d-%m-%Y' IN TO '%Y-%m-%d' AS IN LOADED CSV FILE
startday2 = datetime.strptime(startday1, '%d-%m-%Y')
startday_newformat = startday2.strftime('%Y-%m-%d')
endday2 = datetime.strptime(endday1, '%d-%m-%Y')
endday_newformat = endday2.strftime('%Y-%m-%d')
DATE_LIST = pd.date_range(start=startday_newformat, end=endday_newformat) # CREATING A LIST OF DATES RANGES FROM ENTERED START AND END DATES
DATE_LIST = DATE_LIST.date
startday_newformat = datetime.strptime(startday_newformat, '%Y-%m-%d')
START_DATE_TIME1 = startday_newformat-dt.timedelta(days=1)
START_DATE_TIME1 = START_DATE_TIME1.strftime('%Y-%m-%d')
START_DATE_TIME = START_DATE_TIME1+'T18:30:00.000Z'
END_DATE_TIME = endday_newformat+'T18:30:00.000Z'
startday_newformat1 = startday2.strftime('%d_%m_%Y')
endday_newformat1 = endday2.strftime('%d_%m_%Y')
FOLDER11 = 'EVENT_DETAILS_{}_TO_{}'.format(startday_newformat1, endday_newformat1)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1
# --------------------------------------------SECTION 2 IS OVER---------------------------------------------------------
# --------------------------------------------SECTION 3- SAVING THE STORM DATES AND FIGURES FOLDERS---------------------
try:
    MASK = (DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] >= START_DATE_TIME) & (
                DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] <= END_DATE_TIME)
    DATA = DATA.loc[MASK]
    HEADERS = DATA.columns
    print("THE COLUMN HEADERS ARE.......'", HEADERS, "'")
    if DATA.empty == True:
        print("\nTHE '.csv' FILE IS EMPTY SO THAT NO DATA FRAME CAN BE GENERATED FROM IT........................")
        MISSING_INFORMATION1 = PATH_TO_FOLDER1 + 'MISSING_INFORMATION.txt'
        INFO1 = 'NO SUPER STORMS ("SYM/H VALUE <-100 nT") DATES WERE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(
            startday1, endday1)
        with open(MISSING_INFORMATION1, 'a') as f11:
            f11.write(INFO1 + "\n")
    else:
        print("\nTHE COLUMN DATA FROM THE ENTERED '.csv' FILE ARE SAVING TO SEPARATE '.csv' AND '.txt' FILES")
        NAME_SUBFOLDER1 = 'COLUMN_WISE_SEPARATED_DATA'
        NAME_SUBFOLDER2 = 'CSV_FILES'
        NAME_SUBFOLDER3 = 'TEXT_FILES'
        SUBFOLDER1 = PATH_TO_FOLDER1 + NAME_SUBFOLDER1
        os.makedirs(SUBFOLDER1)
        PATH_SUBFOLDER1 = SUBFOLDER1 + '/'
        SUBFOLDER2 = PATH_SUBFOLDER1 + NAME_SUBFOLDER2
        os.makedirs(SUBFOLDER2)
        PATH_SUBFOLDER2 = SUBFOLDER2 + '/'
        SUBFOLDER3 = PATH_SUBFOLDER1 + NAME_SUBFOLDER3
        os.makedirs(SUBFOLDER3)
        PATH_SUBFOLDER3 = SUBFOLDER3 + '/'
        for column in HEADERS:
            column1 = column
            PUNCTUATIONS = '''!()- []{};:'"\,<>./?@#$%^&*~'''
            for ele in column1:
                if ele in PUNCTUATIONS:
                    column1 = column1.replace(ele, "_")
            try:
                FILE_NAME_1 = '{}.csv'.format(column1)
                FILE_NAME_11 = PATH_SUBFOLDER2 + FILE_NAME_1
                DATA[column].to_csv(FILE_NAME_11, index=False)
                FILE_NAME_2 = '{}.txt'.format(column1)
                FILE_NAME_22 = PATH_SUBFOLDER3 + FILE_NAME_2
                DATA[column].to_csv(FILE_NAME_22, index=False)
                FILE_NAME_3 = '{}_WITHOUT_HEADER.txt'.format(column1)
                FILE_NAME_33 = PATH_SUBFOLDER3 + FILE_NAME_3
                DATA[column].to_csv(FILE_NAME_33, index=False, header=None)
            except OSError:
                print("\nCOLUMN DATA'",column,"'WERE MISSING'")
    # PLOTTING PARAMETERS IN VERTICALLY STACKED MANNER WITHOUT GAP AND WITH GAP AND SAVING THEM IN FOLDERS STACKED_1 AND STACKED_2
    print("\nTHE COLUMNS WISE DATA ARE PLOTTING NOW.....DO NOT CLOSE THE PROGRAM UNTIL IT IS COMPLETE")
    DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'] = pd.to_datetime(DATA['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'], utc=True, format='%Y-%m-%dT%H:%M:%S.%fZ')
    DATA = DATA.set_index(['EPOCH_TIME_yyyy-mm-ddThh:mm:ss.sssZ'])
    #DATA.index = DATA.index.tz_convert(tz='Asia/Calcutta')
    #DATA = DATA.index.tz_convert(tz='Asia/Calcutta')
    #DATA = DATA.tz_localize(tz='GMT')
    #DATA = DATA.tz_convert(tz='Asia/Calcutta')
    DATA['IST'] = DATA.index.tz_convert(tz='Asia/Calcutta')
    FILE_NAME_122 = 'TIME_IN_IST.csv'
    FILE_NAME_1122 = PATH_SUBFOLDER2 + FILE_NAME_122
    DATA['IST'].to_csv(FILE_NAME_1122, index=False)
    FILE_NAME_1223 = 'TIME_IN_IST.txt'
    FILE_NAME_11223 = PATH_SUBFOLDER3 + FILE_NAME_1223
    DATA['IST'].to_csv(FILE_NAME_11223, index=False, header=None)
    FILE_NAME_12234 = 'TIME_IN_IST_WITHOUT_HEADER.txt'
    FILE_NAME_112234 = PATH_SUBFOLDER3 + FILE_NAME_12234
    DATA['IST'].to_csv(FILE_NAME_112234, index=False)
    DATA = DATA.set_index(['IST'])
    rc('font', weight='bold')
    #DATA.plot(figsize=(9, 16),subplots=True, sharex=True, sharey=False,legend=False, lw=0.5, color='blue')
    # # gs = fig.add_gridspec(8, hspace=0)
    # # axs = gs.subplots(sharex=True, sharey=False)
    fig = plt.figure(figsize=(18, 10))
    gs = fig.add_gridspec(5, hspace=0)
    axs = gs.subplots(sharex=True, sharey=False)
    axs[0].plot(DATA['FLOW_SPEED__GSE_km/s'], lw=1.2, color='black')
    axs[0].set_ylabel("Vsw\n(km/s)", fontsize=21, fontweight="bold")
    axs[0].yaxis.set_label_position("left")
    axs[0].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
    axs[0].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[0].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[0].margins(x=0)
    axs[0].set_ylim(ymin=0)
    axs2 = axs[0].twinx()
    axs2.plot(DATA['FLOW_PRESSURE_nPa'], lw=1.2, color='blue')
    axs2.set_ylabel("Psw\n(nPa)", fontsize=21, fontweight="bold", color='blue')
    axs2.yaxis.set_label_position("right")
    ymin1 = round(DATA['FLOW_PRESSURE_nPa'].min())
    ymax1 = round(DATA['FLOW_PRESSURE_nPa'].max())
    axs2.set_yticks(np.arange(ymin1, ymax1, 4))
    axs2.tick_params(direction='in', labelcolor='blue', labelsize=21, length=2, width=2, grid_alpha=0.5, right=True,
                     labelright=True,
                     left=False, labelleft=False)
    axs2.xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs2.margins(x=0)
    axs2.set_ylim(ymin=0)
    axs[1].plot(DATA['BZ__GSE_nT'], lw=1.2, color='red')
    axs[1].set_ylabel("IMF B$_{Z}$\n(nT)", fontsize=21, fontweight="bold")
    axs[1].yaxis.set_label_position("left")
    ymin = round(DATA['BZ__GSE_nT'].min())
    ymax = round(DATA['BZ__GSE_nT'].max())
    axs[1].set_yticks(np.arange(ymin,ymax,10))
    axs[1].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[1].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[1].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[1].margins(x=0)

    axs[2].plot(DATA['ELECTRIC_FIELD_mV/m'], lw=1.2, color='green')
    axs[2].set_ylabel("EF\n(mV/m)\n", fontsize=21, fontweight="bold")
    axs[2].yaxis.set_label_position("left")
    axs[2].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[2].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[2].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[2].margins(x=0)

    axs[3].plot(DATA['SYM/H_INDEX_nT'], lw=1.2, color='black')
    axs[3].set_ylabel("SYM-H\n(nT)", fontsize=21, fontweight="bold")
    axs[3].yaxis.set_label_position("left")
    axs[3].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[3].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[3].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[3].margins(x=0)
    MASK12 = (DATA12['TIME_AT_CENTER_OF_HOUR_yyyy-mm-ddThh:mm:ss.sssZ'] >= START_DATE_TIME) & (
            DATA12['TIME_AT_CENTER_OF_HOUR_yyyy-mm-ddThh:mm:ss.sssZ'] <= END_DATE_TIME)
    DATA12 = DATA12.loc[MASK12]
    if DATA12.empty == True:
        print("\nTHE Kp INDEX DATA FILE IS EMPTY........................")
        MISSING_INFORMATION122 = PATH_TO_FOLDER1 + 'MISSING_INFORMATION_Kp.txt'
        INFO122 = 'NO Kp VALUES ARE FOUND IN THE ENTERED DATE INTERVAL {} TO {} \n'.format(
            startday1, endday1)
        with open(MISSING_INFORMATION122, 'a') as f1122:
            f1122.write(INFO122 + "\n")
    else:
        DATA12['TIME_AT_CENTER_OF_HOUR_yyyy-mm-ddThh:mm:ss.sssZ'] = pd.to_datetime(DATA12['TIME_AT_CENTER_OF_HOUR_yyyy-mm-ddThh:mm:ss.sssZ'],
                                                                         utc=True, format='%Y-%m-%dT%H:%M:%S.%fZ')
        DATA12 = DATA12.set_index(['TIME_AT_CENTER_OF_HOUR_yyyy-mm-ddThh:mm:ss.sssZ'])
        DATA12['IST'] = DATA12.index.tz_convert(tz='Asia/Calcutta')
        #DATA12 = DATA12.set_index(['IST'])
        axs3 = axs[3].twinx()
        #axs3.plot(DATA12['3-H_KP*10_'], lw=1.2, color='blue')
        axs3.bar(DATA12['IST'],DATA12['3-H_KP*10_'], align='center', width=0.25, edgecolor='blue', color='none')
        axs3.set_ylabel("Kp", fontsize=21, fontweight="bold", color='blue')
        axs3.yaxis.set_label_position("right")
        ymin2 = round(DATA12['3-H_KP*10_'].min())
        ymax2 = round(DATA12['3-H_KP*10_'].max())
        axs3.set_yticks(np.arange(ymin2, ymax2, 10))
        axs3.tick_params(direction='in', labelcolor='blue', labelsize=21, length=2, width=2, grid_alpha=0.5, right=True,
                         labelright=True, left=False, labelleft=False)
        axs3.xaxis.grid(which='both', linestyle=':', linewidth=0.4)
        axs3.margins(x=0)
        axs3.set_ylim(ymin=0)
        axs3.set_xlim(xmin=pd.Timestamp(START_DATE_TIME), xmax=pd.Timestamp(END_DATE_TIME))
    der = sym.diff(DATA['SYM/H_INDEX_nT'])
    DATA['DERI_SYM/H_INDEX_nT'] = sym.diff(DATA['SYM/H_INDEX_nT'])
    DER_SYMH_MIN = DATA['DERI_SYM/H_INDEX_nT'].min()
    DER_DATA = DATA.loc[DATA['DERI_SYM/H_INDEX_nT'] == DER_SYMH_MIN]
    DER_DATA_TIME = DER_DATA['DERI_SYM/H_INDEX_nT']
    FILENAME_DER = 'DETAILS_OF_DERIVATIVE_OF_SYMH_{}_TO_{}.csv'.format(startday_newformat1, endday_newformat1)
    print("\nTHE DETAILS OF DERIVATIVE OF SYMH ARE SAVING TO THE FILE '", FILENAME_DER,
          "' IN THE FOLDER '", NAME_SUBFOLDER1, "'....")
    FILENAME1 = PATH_SUBFOLDER1 + FILENAME_DER
    #der = derivative(DATA['SYM/H_INDEX_nT'],1.0, dx=10)
    #der = np.gradient(DATA['SYM/H_INDEX_nT'],10)
    with open(FILENAME1, 'a') as f2:
        DER_DATA_TIME.to_csv(f2, index=True)
    axs[4].plot(DATA['DERI_SYM/H_INDEX_nT'], lw=1.2, color='black')
    axs[4].set_ylabel("d(SYM-H)/dt\n(nT/min)\n", fontsize=21, fontweight="bold")
    axs[4].yaxis.set_label_position("left")
    axs[4].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False, labelright=False, left=True, labelleft=True)
    axs[4].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[4].tick_params(axis='x', which='minor', labelsize=21)
    hrFmt = mdates.HourLocator(interval=12)
    plt.gca().xaxis.set_minor_locator(hrFmt)
    HourFor = mdates.DateFormatter('%H\n%d/%m')
    plt.gca().xaxis.set_minor_formatter(HourFor)
    hrFmt2 = mdates.HourLocator(interval=24)
    plt.gca().xaxis.set_major_locator(hrFmt2)
    dtFmt = mdates.DateFormatter('%H')
    plt.gca().xaxis.set_major_formatter(dtFmt)
    axs[4].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[4].margins(x=0)
    axs[4].set_xlabel('Date and Time (IST)', fontsize=21, fontweight="bold")
    fig.tight_layout()

    NAME_SUBFOLDER11 = 'PLOTS'
    NAME_SUBFOLDER21 = 'STACKED_1'
    NAME_SUBFOLDER31 = 'PNG'
    NAME_SUBFOLDER41 = 'PDF'
    NAME_SUBFOLDER51 = 'JPEG'
    NAME_SUBFOLDER61 = 'SVG'
    SUBFOLDER11 = PATH_TO_FOLDER1 + NAME_SUBFOLDER11
    os.makedirs(SUBFOLDER11)
    PATH_SUBFOLDER11 = SUBFOLDER11 + '/'
    SUBFOLDER21 = PATH_SUBFOLDER11 + NAME_SUBFOLDER21
    os.makedirs(SUBFOLDER21)
    PATH_SUBFOLDER21 = SUBFOLDER21 + '/'
    SUBFOLDER31 = PATH_SUBFOLDER21 + NAME_SUBFOLDER31
    os.makedirs(SUBFOLDER31)
    PATH_SUBFOLDER31 = SUBFOLDER31 + '/'
    SUBFOLDER41 = PATH_SUBFOLDER21 + NAME_SUBFOLDER41
    os.makedirs(SUBFOLDER41)
    PATH_SUBFOLDER41 = SUBFOLDER41 + '/'
    SUBFOLDER51 = PATH_SUBFOLDER21 + NAME_SUBFOLDER51
    os.makedirs(SUBFOLDER51)
    PATH_SUBFOLDER51 = SUBFOLDER51 + '/'
    SUBFOLDER61 = PATH_SUBFOLDER21 + NAME_SUBFOLDER61
    os.makedirs(SUBFOLDER61)
    PATH_SUBFOLDER61 = SUBFOLDER61 + '/'
    GNAME1 = 'STACKED_1.png'
    GNAME2 = 'STACKED_1.pdf'
    GNAME3 = 'STACKED_1.jpeg'
    GNAME4 = 'STACKED_1.svg'
    GNAME11 = PATH_SUBFOLDER31 + GNAME1
    GNAME21 = PATH_SUBFOLDER41 + GNAME2
    GNAME31 = PATH_SUBFOLDER51 + GNAME3
    GNAME41 = PATH_SUBFOLDER61 + GNAME4
    plt.savefig(GNAME11, dpi=500, bbox_inches='tight')
    plt.savefig(GNAME21, dpi=500, bbox_inches='tight')
    plt.savefig(GNAME31, dpi=600, bbox_inches='tight')
    plt.savefig(GNAME41, dpi=300, bbox_inches='tight')

    rc('font', weight='bold')
    # DATA.plot(figsize=(9, 16),subplots=True, sharex=True, sharey=False,legend=False, lw=0.5, color='blue')
    # # gs = fig.add_gridspec(8, hspace=0)
    # # axs = gs.subplots(sharex=True, sharey=False)
    fig1 = plt.figure(figsize=(18, 10))
    gs = fig1.add_gridspec(5, hspace=0.1)
    axs = gs.subplots(sharex=True, sharey=False)
    axs[0].plot(DATA['FLOW_SPEED__GSE_km/s'], lw=1.2, color='black')
    axs[0].set_ylabel("Vsw\n(km/s)", fontsize=21, fontweight="bold")
    axs[0].yaxis.set_label_position("left")
    axs[0].tick_params(direction='in', labelsize=21, length=3, width=3, grid_alpha=0.5, right=False, labelright=False,
                       left=True, labelleft=True)
    axs[0].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[0].margins(x=0)
    axs[0].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[0].set_ylim(ymin=0)
    axs2 = axs[0].twinx()
    axs2.plot(DATA['FLOW_PRESSURE_nPa'], lw=1.2, color='blue')
    axs2.set_ylabel("Psw\n(nPa)", fontsize=21, fontweight="bold", color='blue')
    axs2.yaxis.set_label_position("right")
    ymin1 = round(DATA['FLOW_PRESSURE_nPa'].min())
    ymax1 = round(DATA['FLOW_PRESSURE_nPa'].max())
    axs2.set_yticks(np.arange(ymin1, ymax1, 4))
    axs2.tick_params(direction='in', labelcolor='blue', labelsize=21, length=2, width=2, grid_alpha=0.5, right=True,
                     labelright=True,
                     left=False, labelleft=False)
    axs2.xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs2.margins(x=0)
    axs2.set_ylim(ymin=0)
    # axs[0].legend(['Vsw'], frameon=False, loc=0, ncol=3, fontsize=21, markerscale=15)
    # axs2.legend(['Psw'], frameon=False, loc=7, fontsize=21, markerscale=15)

    axs[1].plot(DATA['BZ__GSE_nT'], lw=1.2, color='red')
    axs[1].set_ylabel("IMF B$_{Z}$\n(nT)", fontsize=21, fontweight="bold")
    axs[1].yaxis.set_label_position("left")
    ymin = round(DATA['BZ__GSE_nT'].min())
    ymax = round(DATA['BZ__GSE_nT'].max())
    axs[1].set_yticks(np.arange(ymin, ymax, 10))
    axs[1].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[1].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[1].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[1].margins(x=0)

    axs[2].plot(DATA['ELECTRIC_FIELD_mV/m'], lw=1.2, color='green')
    axs[2].set_ylabel("EF\n(mV/m)\n", fontsize=21, fontweight="bold")
    axs[2].yaxis.set_label_position("left")
    axs[2].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[2].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[2].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[2].margins(x=0)

    axs[3].plot(DATA['SYM/H_INDEX_nT'], lw=1.2, color='black')
    axs[3].set_ylabel("SYM-H\n(nT)", fontsize=21, fontweight="bold")
    axs[3].yaxis.set_label_position("left")
    axs[3].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[3].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[3].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[3].margins(x=0)
    if DATA12.empty == True:
        print("\nTHE Kp INDEX DATA FILE IS EMPTY........................")
    else:
        axs3 = axs[3].twinx()
        #axs3.plot(DATA12['3-H_KP*10_'], lw=1.2, color='blue')
        axs3.bar(DATA12['IST'], DATA12['3-H_KP*10_'], align='center', width=0.25, edgecolor='blue', color='none')
        axs3.set_ylabel("Kp", fontsize=21, fontweight="bold", color='blue')
        axs3.yaxis.set_label_position("right")
        ymin2 = round(DATA12['3-H_KP*10_'].min())
        ymax2 = round(DATA12['3-H_KP*10_'].max())
        axs3.set_yticks(np.arange(ymin2, ymax2, 10))
        axs3.tick_params(direction='in', labelcolor='blue', labelsize=21, length=2, width=2, grid_alpha=0.5, right=True,
                         labelright=True, left=False, labelleft=False)
        axs3.xaxis.grid(which='both', linestyle=':', linewidth=0.4)
        axs3.margins(x=0)
        axs3.set_ylim(ymin=0)
        axs3.set_xlim(xmin=pd.Timestamp(START_DATE_TIME), xmax=pd.Timestamp(END_DATE_TIME))
    axs[4].plot(DATA['DERI_SYM/H_INDEX_nT'], lw=1.2, color='black')
    axs[4].set_ylabel("d(SYM-H)/dt\n(nT/min)\n", fontsize=18, fontweight="bold")
    axs[4].yaxis.set_label_position("left")
    axs[4].tick_params(direction='in', labelsize=21, length=2, width=2, grid_alpha=0.5, right=False,
                       labelright=False, left=True, labelleft=True)
    axs[4].xaxis.grid(which='both', linestyle=':', linewidth=0.4)
    axs[4].tick_params(axis='x', which='minor', labelsize=21)
    hrFmt = mdates.HourLocator(interval=12)
    plt.gca().xaxis.set_minor_locator(hrFmt)
    HourFor = mdates.DateFormatter('%H\n%d/%m')
    plt.gca().xaxis.set_minor_formatter(HourFor)
    hrFmt2 = mdates.HourLocator(interval=24)
    plt.gca().xaxis.set_major_locator(hrFmt2)
    dtFmt = mdates.DateFormatter('%H')
    plt.gca().xaxis.set_major_formatter(dtFmt)
    axs[4].axvline(pd.Timestamp('2021-03-20 05:30:00+05:30'), color='r', linestyle='--', linewidth=3)
    axs[4].margins(x=0)
    axs[4].set_xlabel('Date and Time (IST)', fontsize=21, fontweight="bold")
    fig1.tight_layout()

    NAME_SUBFOLDER211 = 'STACKED_2'
    NAME_SUBFOLDER311 = 'PNG'
    NAME_SUBFOLDER411 = 'PDF'
    NAME_SUBFOLDER511 = 'JPEG'
    NAME_SUBFOLDER611 = 'SVG'
    SUBFOLDER211 = PATH_SUBFOLDER11 + NAME_SUBFOLDER211
    os.makedirs(SUBFOLDER211)
    PATH_SUBFOLDER211 = SUBFOLDER211 + '/'
    SUBFOLDER311 = PATH_SUBFOLDER211 + NAME_SUBFOLDER311
    os.makedirs(SUBFOLDER311)
    PATH_SUBFOLDER311 = SUBFOLDER311 + '/'
    SUBFOLDER411 = PATH_SUBFOLDER211 + NAME_SUBFOLDER411
    os.makedirs(SUBFOLDER411)
    PATH_SUBFOLDER411 = SUBFOLDER411 + '/'
    SUBFOLDER511 = PATH_SUBFOLDER211 + NAME_SUBFOLDER511
    os.makedirs(SUBFOLDER511)
    PATH_SUBFOLDER511 = SUBFOLDER511 + '/'
    SUBFOLDER611 = PATH_SUBFOLDER211 + NAME_SUBFOLDER611
    os.makedirs(SUBFOLDER611)
    PATH_SUBFOLDER611= SUBFOLDER611 + '/'
    GNAME11 = 'STACKED_2.png'
    GNAME21 = 'STACKED_2.pdf'
    GNAME31 = 'STACKED_2.jpeg'
    GNAME41 = 'STACKED_2.svg'
    GNAME111 = PATH_SUBFOLDER311 + GNAME11
    GNAME211 = PATH_SUBFOLDER411 + GNAME21
    GNAME311 = PATH_SUBFOLDER511 + GNAME31
    GNAME411 = PATH_SUBFOLDER611 + GNAME41
    plt.savefig(GNAME111, dpi=500, bbox_inches='tight')
    plt.savefig(GNAME211, dpi=500, bbox_inches='tight')
    plt.savefig(GNAME311, dpi=600, bbox_inches='tight')
    plt.savefig(GNAME411, dpi=300, bbox_inches='tight')
    # ---------------------------------------------PLOTTING IS OVER-----------------------------------------------------
    # ----------------------------------SECTION 3 IS OVER---------------------------------------------------------------
except OSError:
    print("\nYOU ENTERED WRONG DATES....PLEASE RE RUN THE CODE AND ENTER DATES PROPERLY")
print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 01-11-2021---------------------------SREEKUMAR HARIDAS--------------------