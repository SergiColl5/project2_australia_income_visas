import pandas as pd
import numpy as np
import my_functions as mf

# Reading the two files i need.
migration = pd.read_excel('../data/downloaded_excel.xlsx',sheet_name='1.4')
income = pd.read_excel('../data/income_industry.xlsx',sheet_name='Table 2.1')

# Main cleaning for both
migration=mf.BasicCleanig(migration,5,5)
income=mf.BasicCleanig(income,5,5)


