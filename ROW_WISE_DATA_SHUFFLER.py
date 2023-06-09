# THIS IS A SIMPLE PYTHON PROGRAM WHICH SHUFFLE THE DATA IN THE ENTERED TEXT FILE
import time
start = time.time()
import os
import pandas as pd
# List of file names
PWD1 = os.getcwd()
PWD = PWD1+'/'
input_file_name='BNG_1993May_21_25_Quiet.txt'
DATA_PATH1 = PWD+input_file_name
DATA_1= pd.read_csv(DATA_PATH1, delimiter='\t', header=None) 
def shuffle_rows_in_dataframe(df):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    return shuffled_df
shuffled_df = shuffle_rows_in_dataframe(DATA_1)
output_file = '{}_Shuffled.txt'.format(input_file_name)
if os.path.exists(output_file):
    # Delete the file
    os.remove(output_file)
    print(f"The file '{output_file}' has been deleted.")
else:
    print(f"The file '{output_file}' does not exist.")
# Open the output file in write mode
print(f"The file '{output_file}' has been created.")
shuffled_df.to_csv(output_file, index=False)

print("Files Shuffled successfully!")

print("\nTOTAL EXECUTION TIME OF THE PROGRAM IS: '%s' minutes........!!!!!!!!!" %((time.time() - start)/60))
# --------------------------------------------THANK YOU FOR USING THE CODE----------------------------------------------
# -----------------------------------------ON 03-06-2023---------------------------SREEKUMAR HARIDAS--------------------