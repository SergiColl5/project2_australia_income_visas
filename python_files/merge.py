import pandas as pd
# I import both cleaned xlsx files and merge them
income = pd.read_excel('../data/income_clean.xlsx')
migration= pd.read_excel('../data/migration_clean.xlsx')
all_together = pd.merge(migration,income, on=['Year','Activity'],how='left')
all_together = all_together.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y'])
all_together.to_excel('../data/all_together.xlsx')

