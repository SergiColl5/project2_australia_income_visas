import pandas as pd
import numpy as np
import my_functions as mf
import os

# Reading the two files i need.
migration = pd.read_excel('../data/downloaded_excel.xlsx',sheet_name='1.4')
income = pd.read_excel('../data/income_industry.xlsx',sheet_name='Table 2.1')

# Main cleaning for both
migration=mf.BasicCleanig(migration,5,5)
income=mf.BasicCleanig(income,5,5)


#more cleaning and stacking 
new_header = list(migration.iloc[0])
old_header = list(migration.columns)
migration.columns = new_header
migration.drop(4,inplace=True)
migration.drop(columns='Total',inplace=True)


#Stack and set dataframe

migration = mf.stackAndDataframe(migration)
new_columns=['Year','Activity','Sponsored_visas']
migration.columns=new_columns
migration['Year']= migration['Year'].apply(lambda x : x.split('–')[0])
migration['Sponsored_visas']=migration['Sponsored_visas'].apply(mf.charactersout)
income = mf.stackAndDataframe(income)
new_columns=['Year','Activity','Median_income']
income.columns=new_columns
income['Activity']=income['Activity'].apply(lambda x: x.lower())
migration['Activity']=migration['Activity'].apply(lambda x: x.lower())

#Export to excel file
if not os.path.exists('../data'):
            os.mkdir('../data')

income.to_excel('../data/income_clean.xlsx')
migration.to_excel('../data/migration_clean.xlsx')

print('Both cleaned files have been saved into "Data" folder')
