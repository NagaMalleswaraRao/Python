#Importing libraries
import numpy as np
import pandas as pd

#reading excel file (if it's in the same folder)
file_name = 'Data.xlsx'
pd.read_excel(file_name)

#assigning data from excel file to a data frame
file_name = 'Data.xlsx'
df = pd.read_excel(file_name)
print(df)

