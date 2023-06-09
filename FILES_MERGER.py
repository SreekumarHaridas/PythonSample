# THIS IS A SIMPLE PYTHON PROGRAM WHICH CREATE THE LOCAL TIME BASED EEF DATA
import time
start = time.time()
import os
# List of file names
input_files = ['LT_BASED_VTEC_DATA_25_02_2023_ELE_ANGLE_30_WITH_DATE.txt', 'LT_BASED_VTEC_DATA_26_02_2023_ELE_ANGLE_30_WITH_DATE.txt', 'LT_BASED_VTEC_DATA_27_02_2023_ELE_ANGLE_30_WITH_DATE.txt', 'LT_BASED_VTEC_DATA_28_02_2023_ELE_ANGLE_30_WITH_DATE.txt', 'LT_BASED_VTEC_DATA_01_03_2023_ELE_ANGLE_30_WITH_DATE.txt','LT_BASED_VTEC_DATA_02_03_2023_ELE_ANGLE_30_WITH_DATE.txt','LT_BASED_VTEC_DATA_03_03_2023_ELE_ANGLE_30_WITH_DATE.txt']

output_file = 'MERGED_FILE_BAN.txt'
if os.path.exists(output_file):
    # Delete the file
    os.remove(output_file)
    print(f"The file '{output_file}' has been deleted.")
else:
    print(f"The file '{output_file}' does not exist.")
# Open the output file in write mode
print(f"The file '{output_file}' has been created.")
with open(output_file, 'w') as outfile:
    # Iterate through each input file
    for file_name in input_files:
        # Open each input file in read mode
        with open(file_name, 'r') as infile:
            # Read the content of the input file
            content = infile.read()
            # Write the content to the output file
            outfile.write(content)

print("Files merged successfully!")

print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 16-05-2023---------------------------SREEKUMAR HARIDAS--------------------