# THIS IS A SIMPLE PYTHON PROGRAM CAN BE USED FOR DOWNLOADING ATEC DATA (HIGH SPEED INTERNET CONNECTION IS NECESSARY) PRODUCT - Global Navigation Satellite System -
#Total Electron Content (GNSS-TEC) database at the URL"https://stdb2.isee.nagoya-u.ac.jp/GPS/GPS-TEC/"
import time
start = time.time()
import shutil
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['timezone'] = 'Asia/Calcutta'
#import matplotlib.dates as mdates
from matplotlib import rc
from datetime import datetime, date
import numpy as np
import requests
import cartopy.crs as ccrs
from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter)
#import netCDF4 as nc 
import xarray as xr
os.environ["PROJ_LIB"] = "C:\\Utilities\\Python\\Anaconda\\Library\\share"; #fixr
# from mpl_toolkits.basemap import Basemap
# import matplotlib as mpl
# ---------------------------------SECTION 1--USER INPUTS-AND SAVE IT IN TO A TEXT FILE---------------------------------
input_log = {}
Date_of_the_Day = input("ENTER THE DATE (AS dd-mm-yyyy): ")
Hour = input("ENTER THE HOUR (e.g. '00 or 23' ): ")
PWD1 = os.getcwd()
PWD = PWD1+'/'
# print(PWD)
for variable in ["Date_of_the_Day","Hour"]:
    input_log[variable] = eval(variable)
with open("Input_Parameters_GLOBAL_aTEC_V1.txt", 'w') as f1:
    str_input_log = repr(input_log)
    f1.write("input_log = " + str_input_log + "\n")
#----------------------------------------------SECTION 1 OVER-----------------------------------------------------------
#-----------------------------------------CONVERTING DATE TO DOY--------------------------------------------------------
date_value_1=datetime.strptime(Date_of_the_Day,'%d-%m-%Y')
Date_Value=datetime(date_value_1.year,date_value_1.month,date_value_1.day)
day_of_year = Date_Value.strftime('%j')
#-------------------------------------------------CONVERSION IS OVER----------------------------------------------------
#---------------------------------------CREATING FOLDERS TO SAVE FILES--------------------------------------------------
Date_of_the_Day2 = datetime.strptime(Date_of_the_Day, '%d-%m-%Y')
Date_of_the_Day3 = Date_of_the_Day2.strftime('%d_%m_%Y')
FOLDER11 = 'DOWNLOADED_NC_FILE_{}'.format(Date_of_the_Day3)
FOLDER1 = PWD + FOLDER11
if os.path.exists(FOLDER1):
    shutil.rmtree(FOLDER1)
os.makedirs(FOLDER1)
PATH_TO_FOLDER1 = FOLDER1 + '/'  # PATH IN TO FOLDER1

FOLDER112 = 'CONVERTED_CSV_FILE_{}'.format(Date_of_the_Day3)
FOLDER12 = PWD + FOLDER112
if os.path.exists(FOLDER12):
    shutil.rmtree(FOLDER12)
os.makedirs(FOLDER12)
PATH_TO_FOLDER12 = FOLDER12 + '/'  # PATH IN TO FOLDER12

FOLDER1122 = 'FIGURES_{}'.format(Date_of_the_Day3)
FOLDER122 = PWD + FOLDER1122
if os.path.exists(FOLDER122):
    shutil.rmtree(FOLDER122)
os.makedirs(FOLDER122)
PATH_TO_FOLDER122 = FOLDER122 + '/'  # PATH IN TO FOLDER122
#--------------------------------------------FOLDER CREATION IS OVER----------------------------------------------------

#---------------------------------AUTOMATICALLY CREATTING THE NAME OF THE URL AND DOWNLOADING---------------------------

url = 'https://stdb2.isee.nagoya-u.ac.jp/GPS/shinbori/AGRID2/nc/{}/{}/{}{:02d}{:02d}{}_atec.nc'.format(date_value_1.year, day_of_year,date_value_1.year,date_value_1.month,date_value_1.day,Hour)
r = requests.get(url, allow_redirects=True)
FILE_PATH = PATH_TO_FOLDER1+'Global_ATEC_{}_{}_{}.nc'.format(date_value_1.year, day_of_year,Hour)
open(FILE_PATH, 'wb').write(r.content)
print("\nTHE GLOBAL ATEC DATA FILE(.nc) IS DOWNLOADED IN PWD FOR THE DATE '", Date_of_the_Day,"'....\n")
#-----------------------------------------URL AUTOMATION AND DOWNLODING IS OVERIS OVER----------------------------------
#----------------------------------------READING THE DOWNLOADED NC FILE AND CONVERTED THE GRID INTO A CSV FILE---------
#DATA = nc.Dataset(FILE_PATH) # READ THE .nc FILE USING NetCDF
DATA = xr.open_dataset(FILE_PATH) # READ THE .nc FILE USING xarray

latitude=DATA.variables['lat'] #or latitude=DATA.lat
latitude_array=latitude.values#but DATA.variables('lat')[:] is not forking for me; don't know why

longitude=DATA.variables['lon'] #or longitude=DATA.lon
longitude_array=longitude.values#but DATA.variables('lon')[:] is not forking for me; don't know why

ATEC=DATA.variables['atec']# or ATEC=DATA.atec
ATEC_array=ATEC.values

TIME=DATA.variables['time'] 
TIME_ARRAY=TIME.values
#-----------------------------------------URL AUTOMATION AND DOWNLODING IS OVERIS OVER----------------------------------

#-------------------------------------PLOTTING THE ATEC DATA------------------------------------------------------------
#-------------------------------------PLOTTING USING CARTOPY------------------------------------------------------------
LONGITUDE_GRID, LATITUDE_GRID= np.meshgrid(longitude_array,latitude_array)
#-------------------------------------PLOTTING GLOBAL ATEC------------------------------------------------------------
for Time_Block in np.arange(0,12,1):
    rc('font', weight='bold')
    rc('axes', linewidth=3)
    colorticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    xticks=np.arange(-120,180,60)
    yticks=np.arange(-60,90,30)
    fig=plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    ax.set_extent([-180, 210, -90, 120],crs=ccrs.PlateCarree())
    ax.coastlines(resolution='10m', lw=1.5)
    pcolor=ax.pcolormesh(LONGITUDE_GRID,LATITUDE_GRID,(ATEC[:,:,Time_Block]),transform=ccrs.PlateCarree(),vmin=0, vmax=100,cmap='jet', )
    ax.tick_params(axis='both', which='major', labelsize=32)
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.xaxis.grid(which='both', color='gray',alpha=0.5,linestyle='--' , linewidth=1)
    ax.yaxis.grid(which='both', color='gray',alpha=0.5,linestyle='--', linewidth=1)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.tick_params(direction='in', labelsize=32, length=3, width=3)
    ax.set_xlabel('Longitude (degree)', fontsize=33, fontweight="bold")
    ax.set_ylabel('Latitude (degree)', fontsize=33, fontweight="bold")
    cbar=plt.colorbar(pcolor, ax=ax,fraction=.0225,pad=0.07,ticks=colorticks)
    cbar.set_label(label='aTEC (TECU)\n', size = 26,fontweight="bold") # To write Lable on right side
    #cbar.ax.set_title(label='ATEC (TECU/min)\n', size = 26,fontweight="bold")
    cbar.ax.tick_params(labelsize=27, direction='in',length=3, width=3)
    cbar.ax.yaxis.set_ticks_position('right')
    ax1= plt.gca()
    plt.setp(ax1.spines.values(), linewidth=2)
    fig.subplots_adjust(left=.15, right=1-.08,bottom=.1, top=1-.06)
    #plt.show()
    GNAME3 = 'GLOBAL_ATEC_PLOT_{}_{}_{}.jpeg'.format(Date_of_the_Day3,Hour,Time_Block)
    GNAME31 = PATH_TO_FOLDER122 + GNAME3
    plt.savefig(GNAME31, dpi=1000, bbox_inches='tight')

#------------------SAVE THE LONGITUDES, LATITUDES, ATECS OF THE SELECTED TIME FRAME TO A CSV FILE------------------------------------

    ATEC_TIME_BLOCK = np.asarray(ATEC[:,:,Time_Block]) #asarray IS USED TO SAVE A MULTI-DIMENSIONAL DATA (HERE ATEC) TO AN ARRAY
    NROWS = len(ATEC_TIME_BLOCK)
    NCOLS = len(ATEC_TIME_BLOCK[0])
    XLONGITUDE_GRID = LONGITUDE_GRID.reshape(NROWS*NCOLS,1)
    YLATITUDE_GRID = LATITUDE_GRID.reshape(NROWS*NCOLS,1)
    ATEC_TIME_BLOCK2 = ATEC_TIME_BLOCK.reshape(NROWS*NCOLS,1)
    FINAL_GRID_DATA = np.concatenate((XLONGITUDE_GRID,YLATITUDE_GRID,ATEC_TIME_BLOCK2 ),axis=1)
    FILE_PATH2 = PATH_TO_FOLDER12+'ATEC_DATA_{}_{}_{}.csv'.format(Date_of_the_Day3,Hour,Time_Block) # READ THE GRID ATEC DATA TO A CSV FILE WITH HEADERS "LONGITUDE,LATITUDE,ATEC"
    FILE = open(FILE_PATH2, 'a')
    np.savetxt(FILE, FINAL_GRID_DATA, delimiter=",", fmt='%0.3f', header="LONGITUDE,LATITUDE,ATEC", comments='')
    FILE.close()
    print("\nTHE GLOBAL ATEC DATA IS SAVED TO A CSV IN THE RESPECTIVE FOLDER IN PWD FOR THE DATE '", Date_of_the_Day,"'FOR THE HOUR'",Hour,"' FOR THE TIME INTERVAL'",Time_Block,"'...\n")
#---------------------------------------------DATA IS SAVED-------------------------------------------------------------------------


#-------------------------------------PLOTTING ATEC OVER INDIAN SECTOR--------------------------------------------------------------

    rc('font', weight='bold')
    rc('axes', linewidth=3)
    colorticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    xticks=np.arange(60,130,10)
    yticks=np.arange(0,40,10)
    fig=plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    ax.set_extent([60, 120, 0, 30],crs=ccrs.PlateCarree())
    ax.coastlines(resolution='10m', lw=1.5)
    #pcolor=ax.contourf(YLATITUDE1,XLONGITUDE1,ON2GRIDSMOOTH,origin='lower',transform=ccrs.PlateCarree(),vmin=0, vmax=1,cmap='jet')
    pcolor=ax.pcolormesh(LONGITUDE_GRID,LATITUDE_GRID,(ATEC[:,:,Time_Block]),transform=ccrs.PlateCarree(),vmin=0, vmax=100,cmap='jet', )
    ax.tick_params(axis='both', which='major', labelsize=32)
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.xaxis.grid(which='both', color='gray',alpha=0.5,linestyle='--' , linewidth=1)
    ax.yaxis.grid(which='both', color='gray',alpha=0.5,linestyle='--', linewidth=1)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.tick_params(direction='in', labelsize=32, length=3, width=3)
    ax.set_xlabel('Longitude (degree)', fontsize=33, fontweight="bold")
    ax.set_ylabel('Latitude (degree)', fontsize=33, fontweight="bold")
    cbar=plt.colorbar(pcolor, ax=ax,fraction=.0225,pad=0.07,ticks=colorticks)
    cbar.set_label(label='aTEC (TECU)\n', size = 26,fontweight="bold") # To write Lable on right side
    #cbar.ax.set_title(label='ATEC (TECU/min)\n', size = 26,fontweight="bold")
    cbar.ax.tick_params(labelsize=27, direction='in',length=3, width=3)
    cbar.ax.yaxis.set_ticks_position('right')
    ax1= plt.gca()
    plt.setp(ax1.spines.values(), linewidth=2)
    fig.subplots_adjust(left=.15, right=1-.08,bottom=.1, top=1-.06)
    #plt.show()
    GNAME31 = 'INDIAN_ATEC_PLOT_{}_{}_{}.jpeg'.format(Date_of_the_Day3,Hour,Time_Block)
    GNAME311 = PATH_TO_FOLDER122 + GNAME31
    plt.savefig(GNAME311, dpi=1000, bbox_inches='tight')
#-------------------------------------PLOTTING USING CARTOPY IS OVER------------------------------------------------------------


#-------------------------------------PLOTTING USING BASEMAP------------------------------------------------------------

# mp=  Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c')
# # mp=  Basemap(projection='cyl',llcrnrlat=5,urcrnrlat=30, 
# #                 llcrnrlon=50,urcrnrlon=105,resolution='c')

# LONGITUDE_GRID, LATITUDE_GRID= np.meshgrid(longitude_array,latitude_array)

# LONGITUDE_GRID_1, LATITUDE_GRID_1= mp(LONGITUDE_GRID,LATITUDE_GRID)


# # rc('font', weight='bold')
# # rc('axes', linewidth=3)
# # colorticks=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# # fig=plt.figure(figsize=(16, 9))
# # c_schem=mp.pcolor(LONGITUDE_GRID_1,LATITUDE_GRID_1,np.squeeze(ATEC[:,:,Time_Block]),vmin=0.0, vmax=0.25,cmap='jet')
# # #c_schem=mp.scatter(LONGITUDE_GRID_1,LATITUDE_GRID_1,np.squeeze(ATEC[:,:,3]),cmap='PiYG')
# # mp.drawcoastlines()
# # mp.drawparallels(np.arange(-90,90,30),labels=[1,1,0,1], fontsize=20)
# # mp.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1], rotation=45, fontsize=20)
# # cbar=mp.colorbar(c_schem, fraction='10%',pad='10%',ticks=colorticks,location='right')
# # plt.show

# rc('font', weight='bold')
# rc('axes', linewidth=3)
# colorticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# fig=plt.figure(figsize=(16, 9))
# c_schem=mp.pcolor(LONGITUDE_GRID_1,LATITUDE_GRID_1,np.squeeze(ATEC[:,:,Time_Block]),vmin=0.0, vmax=1.0,cmap='jet')
# #c_schem=mp.scatter(LONGITUDE_GRID_1,LATITUDE_GRID_1,np.squeeze(ATEC[:,:,3]),cmap='PiYG')
# mp.drawcoastlines()
# mp.drawparallels(np.arange(-90,90,30),labels=[1,1,0,1], fontsize=20)
# mp.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1], rotation=45, fontsize=20)
# cbar=mp.colorbar(c_schem, fraction='10%',pad='10%',ticks=colorticks,location='right')
# plt.show


# latitude=DATA.lat
# longitude=DATA.lon
# ATEC=DATA.atec
# TIME=DATA.time
# la=ATEC[:,:,3].latitude
# lo=ATEC[:,:,3].longitude

# ATEC0=ATEC[:,:,3]
# YLATITUDE,XLONGITUDE = np.meshgrid(lo,la)
# YLATITUDE1,XLONGITUDE1 = np.meshgrid(lo,la)
# ATEC0GRID = np.asarray(ATEC0)
# NROWS = len(ATEC0GRID)
# NCOLS = len(ATEC0GRID[0])
# XLONGITUDE_GRID = XLONGITUDE.reshape(NROWS*NCOLS,1)
# YLATITUDE_GRID = YLATITUDE.reshape(NROWS*NCOLS,1)
# ATEC0GRID_NEW = ATEC0GRID.reshape(NROWS*NCOLS,1)
# FINAL_GRID_DATA = np.concatenate((XLONGITUDE_GRID, YLATITUDE_GRID, ATEC0GRID_NEW),axis=1)
# FILE_PATH2 = PATH_TO_FOLDER12+'Global_ATEC_{}_{}_{}.csv'.format(date_value_1.year, day_of_year,Hour)
# FILE = open(FILE_PATH2, 'a')
# np.savetxt(FILE, FINAL_GRID_DATA, delimiter=",", fmt='%0.3f', header="LATITUDE,LONGITUDE,ATEC0GRID", comments='')
# FILE.close()
# plt.pcolormesh(YLATITUDE1,XLONGITUDE1,ATEC0GRID,)
# plt.show()
# n=len(DATA.time)
# for T in range(0, n):   
#     print(T)
#     plt.pcolormesh(ATEC[:,:,T])
#     plt.show()
#-------------------------------------PLOTTING USING BASEMAP IS OVER------------------------------------------------------------
#------------------------------------------------PLOTTING IS OVER-------------------------------------------------------

print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 22-03-2023---------------------------SREEKUMAR HARIDAS--------------------
