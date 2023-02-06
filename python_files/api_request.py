import pandas as pd
from pandas import json_normalize
import ast
import requests 
import json
import os
from dotenv import load_dotenv
import my_functions as mf
password = os.getenv('password')
user = os.getenv('user')
url_migration_request = "https://data.gov.au/data/dataset/dba45e7c-81f4-44aa-9d82-1b9a0a121017/resource/1133d1f9-68e7-4d2f-96fb-45104769b7dc/download/migration_trends_statistical_package_2021_22.xlsx"

mf.requestAPIxlsx(url_migration_request)