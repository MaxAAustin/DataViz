"""
Import block.
Pandas and Matplotlib used for data analysis
chardet used in pre-processing to determine the file encoding
"""

import pandas as pd
from matplotlib import cm as cm 
import matplotlib.pyplot as plt
import matplotlib
import chardet
import seaborn as sns
from mpl_toolkits.basemap import Basemap
"""
This method detects the filetype and returns the string with the encoding type.
Input: file path + name as a string
Output: string with file encoding name (e.g. UTF-8, ISO-9959-1, etc.)
Below, this method was called on a sample of the dataset as the 180,000 rows and 
135 columns took too long to process before. The coding is 'ISO-8859-1'
"""
def detect_filetype(filename):
    read_name = open(filename,'rb').read()
    result = chardet.detect(read_name)
    res = result['encoding']
    return res

#enc = detect_filetype("data/gtds_sample.csv")
#print(enc)

"""
Dataset notes:
It's encoded in ISO-8859-1 format, rather than UTF-8 (determined using the detect_filetype() above)
There are mixed data types in the following columns: 4,6,31,33,61,62,63,76,79,90,92,94,96,114,115,121.
REMINDER: Filenames include the full path if the data file is in another folder. 
For this reason, it's customary to house the data file in the same directory as your Python script.
"""

df = pd.read_csv("data/gtds.csv",encoding='ISO-8859-1', low_memory = False)

#print(df.head())  # Prints the first 5 rows and their column names to the console
#print(df.columns) # Prints the names of the columns. Will truncate if there are more that 10 or so headers. 

# Renames the column headers using the format dataframe.rename(columns={'original_name':'new_name'})
df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region_txt':'Region', 
                   'city': 'City', 'latitude':'Lat', 'longitude':'Long','attacktype1_txt':'Attack_Type',
                   'target1':'Target','nkill':'Num_Killed','nwound':'Num_Wounded','summary':'Summary',
                   'gname':'Group','targtype1_txt':'Target_Type','weaptype1_txt':'Weapon_Type','motive':'Motive'},inplace=True)

# Eliminates columns with citations and other data we don't need.
df = df[['eventid','Year','Month','Day','Country', 'Region', 'City','Lat','Long','Attack_Type', 'Target', 'Num_Killed', 'Num_Wounded', 
         'Summary', 'Group','Target_Type', 'Weapon_Type', 'Motive']]

#print(df.columns) # Prints new column names and slimmed down dataframe