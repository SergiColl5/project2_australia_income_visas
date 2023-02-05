import pandas as pd
import numpy as np
from functions import cleaning_functions as clean

# Reading the two files i need.
migration = pd.read_excel('../data/downloaded_excel.xlsx',sheet_name='1.4')
income = pd.read_excel('../data/income_industry.xlsx',sheet_name='Table 2.1')

# Main cleaning for both
migration=clean.BasicCleanig(migration,5,5)
income=clean.BasicCleanig(income,5,5)


