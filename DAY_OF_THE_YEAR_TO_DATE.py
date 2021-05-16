#  THIS IS A SIMPLE PYTHON PROGRAM THAT CONVERT THE DOY ENTERED IN TO THE CORRESPONDING DATE OF THE YEAR USING datetime.strptime()

from datetime import datetime
year = input("PLEASE ENTER THE YEAR ( e.g. 2016): ")   # ENTER THE YEAR AS A STRING
doy = input('PLEASE ENTER THE DAY OF THE YEAR  (e.g. 315):')     # ENTER THE DOY AS A STRING

# adjusting day num
doy.rjust(3 + len(doy), '0')
# converting to date
res = datetime.strptime(year + "-" + doy, "%Y-%j").strftime("%d-%m-%Y")

# printing result
# print("Resolved date : " + str(res))
print("THE DATE (DD/MM/YYYY) CORRESPONDING TO THE DOY {} IN THE YEAR {} IS {} ".format(doy, year, str(res)))