# 11/18/2019 Babak J.Fard
# To modify the input file, as asked by Jageddish, therefore the Apparent Emperature
# is also added as a last column

# run the code as modify_inputs <folder_path>

# Import Modules
import os
import numpy as np
import pandas as pd
import numpy.ma as ma
import sys 
import time
import datetime

# get the folder name 
folder_path = sys.argv[1]
# folder_path ='/Users/babak.jfard/python/NCH_codes/jagedish/DewPointT'

# get directories inside that into a list. This will be the name NC-region
#regions = os.listdir(folder_path)
regions = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

# do loop inside each folder
for this_region in regions:
    
    region_App_temp = pd.DataFrame(columns=['year', 'month', 'day', 'dew_temp'])
    # Get the name of files into a list --> year
    years_t = os.listdir(os.path.join(folder_path, this_region))

    # Loop over year (each file)
    for this_year in years_t:
        # read in as a dataframe
        df = pd.read_csv(str(folder_path + '/'+this_region+'/'+this_year), 
        header=None, names=['day_count', 'stations', 'temp_dew'])

        df = df.iloc[1:]

        # change the first column into the day number
        year = this_year[:4]
        df['date'] = [datetime.date(int(year), 1, 1)+datetime.timedelta(x-1) for x in df.day_count]
        df['year'] = df['date'].apply(lambda x:x.year)
        df['month'] = df['date'].apply(lambda x:x.month)
        df['day'] = df['date'].apply(lambda x:x.day)

        df2 = pd.DataFrame({'year':df.year,'month':df.month, 'day':df.day,'dew_temp':df.temp_dew})

        region_App_temp = region_App_temp.append(df2)
    region_App_temp.sort_values(by=['year', 'month', 'day'], inplace=True)    
    region_App_temp.to_csv(str(folder_path +'/'+this_region+'_output.csv'), index=False)

print('Finished! Check your files.')





        

        # Create a data frame of AT(year, month, day, dew_temp)

        # write the dataframe in a csv file

