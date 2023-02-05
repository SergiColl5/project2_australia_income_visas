import pandas as pd
from pandas import json_normalize
import ast
import requests 
import json
import os
from dotenv import load_dotenv
password = os.getenv('password')
user = os.getenv('user')
url_migration_request = "https://data.gov.au/data/dataset/dba45e7c-81f4-44aa-9d82-1b9a0a121017/resource/1133d1f9-68e7-4d2f-96fb-45104769b7dc/download/migration_trends_statistical_package_2021_22.xlsx"
def requestAPIxlsx (url):
    '''This function download an excel file using an API url and saves it into a folder called "data" in the same directory.
        it creates the folder if it doesn't exists.'''
            
    response_xlsx = requests.get(url)
    if response_xlsx.status_code==200:
        if not os.path.exists('../data'):
            os.mkdir('../data')
        with open('../data/downloaded_excel.xlsx','wb') as f:
            f.write(response_xlsx.content)
        return print('Your file has been downloaded to you folder "data".')
    else: 
        return print('Failed to download file. Response status code:', response_xlsx.status_code)
requestAPIxlsx(url_migration_request)