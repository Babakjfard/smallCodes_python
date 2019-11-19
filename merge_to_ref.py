# Babak - This is after the output file has created in such a fomat that is
# compatible with the input files for the analysis (after running modify_inputs.py)
# 
# $ python merge_to_ref.py <reference_file_path> <inputfile_path>

# Import Modules
import os
import numpy as np
import pandas as pd
import numpy.ma as ma
import sys 
import time
import datetime

# get list of .txt files from the reference_folder
col_names = ['year', 'month', 'day', 'tmax', 'an_max', '5th', '6th', 'tmin','an_min',
'9th', '10th']
df_ref = pd.read_csv(sys.argv[1], header=None, delimiter=r"\s+", names=col_names)
df_inp = pd.read_csv(sys.argv[2])

df_joined = df_ref.merge(df_inp, on=['year', 'month', 'day'])
df_joined.to_csv('/Users/babak.jfard/python/NCH_codes/jagedish/test.csv', index=False,
 header=None, sep=' ')
print("done!")

