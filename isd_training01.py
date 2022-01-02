# Title: Dataframe transformation and calculations

# 2022-01-02 - The following python script is designed to serve as a
# component of a larger data pipeline for metabolomic studies. The included
# table consists of 2 columns, which represent daily measurements of
# food and food added, respectively. The amount of food consumed from one
# day to the next can be calculated, for example, by subtracting row 1
# from row 0. A condition must be introduced, however, when food is added.
# In such a scenario, one must subtract from the added food value, instead
# of the measured amount of the same day (see row 2 and 6 as examples).

# Import relevant libraries
import pandas as pd

# Generate practice dataset
df = pd.DataFrame([[8,0],[7.1,0],[0.8,20.6],[13.9,0],[9.5,0],[6.7,0],
                   [3.2,15.5],[12.2,0]])

# Isolate the individual commands
df_calc_1_all = df.diff(periods = -1)             # Subtract row n from row n-1
df_calc_2_all = df.diff(periods = 1, axis = 1)    # Subtract col 0 from col 1
df_calc_3_col_0 = df.iloc[:,0].diff(periods = -1) # Subtract rows only col 0
df_calc_4_col_1 = df.iloc[:,1].transform('shift') # Shift down rows in col 1

# Using a combination of the expressions above, execute the following
# command: While the value in column 1 is 0, calculate the difference between
# rows in column 0. However, when the value in column 1 is not 0,
# calculate instead the difference between the row in column 0 and the
# preceding row in column 1.

# Attempt 1
c0 = df.iloc[:,0]
c1 = df.iloc[:,1]
for i in range(len(df)):
    if c1[c1 == 0]:
        c0.diff(periods = -1)
     else:
        c1.transform('shift')
        df.diff(periods = 1, axis = 1)

# Attempt 2
c0 = df.iloc[:,0]
c1 = df.iloc[:,1]
 for i in df:
    if c1[c1 != 0]:
        df.diff(periods = 1, axis = 1)
    else:
        c0.diff(periods = -1)
