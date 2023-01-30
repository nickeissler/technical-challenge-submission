import sys
from pathlib import Path
import pandas as pd
import os


#Given a list of dataframes, combine them
def combine_csv_files(input):
    #Remove program name from list
    arguments = len(input)
    #Must be at least 2 args
    if (arguments <= 2):
        sys.exit("Error: At least two arguments required")

    #Check if every argument is a valid file
    for arg in input:
        file_path = Path(arg)
        if not (file_path.is_file()):
            sys.exit("Error: At least one file does not exist")

    #Create list to store csv files
    df_list = []
    #Loop through every argument (that is not program name)
    for i in range(1, arguments):
        file_path = Path(input[i])
        #Terminate if a file does not exist
        if not (file_path.is_file()):
            sys.exit("Error: At least one file does not exist")
        else:
            fname = os.path.basename(input[i])
            data = pd.read_csv(input[i])
            data['filename'] = fname
            df_list.append(data)


    #Exit if the dataframes do not have the same columns
    if not all([set(df_list[0].columns) == set(df.columns) for df in df_list]):
        sys.exit("Error: At least two files have differing columns")

    combined_df = pd.DataFrame()

    for df in df_list:
        combined_df = pd.concat([combined_df, df], axis=0)

    print(combined_df)
    return combined_df

def get_user_input():
    return sys.argv

def main():
    combine_csv_files(get_user_input())

if __name__ == '__main__':
    main()


