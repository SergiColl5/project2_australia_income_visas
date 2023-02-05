import pandas as pd
import numpy as np
import my_functions as cl

# Reading the two files i need.
migration = pd.read_excel('../data/downloaded_excel.xlsx',sheet_name='1.4')
income = pd.read_excel('../data/income_industry.xlsx',sheet_name='Table 2.1')

# I clean the data importing functions already created. And also changing specific items, rename columns and set correct indexes.
migration= cl.BasicCleanig(migration,4,4)
new_header = list(migration.iloc[0])
old_header = list(migration.columns)
migration.columns = new_header
migration.drop(4,inplace=True)
migration.drop(columns='Total',inplace=True)
migration = cl.stackAndDataframe(migration)
new_columns=['Year','Activity','Sponosored_visas']
migration.columns=new_columns

