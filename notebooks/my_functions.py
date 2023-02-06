import pandas as pd
import requests 
def BasicCleanig (dataframe,NumberOfValuesInRow,NumberOfValuesInColum):
    '''This function recevies a DataFrame, the minimum number of values that I want in my rows and columns.
        It deletes the empty rows, the empty columns, and the duplicates.
        Returns the DataFrame with the changes aplied.'''
    dataframe.dropna(axis=1, thresh= NumberOfValuesInColum, inplace=True)
    dataframe.dropna(axis=0, thresh=NumberOfValuesInRow, inplace=True)
    dataframe.drop_duplicates(inplace=True)
    return dataframe
    
def stackAndDataframe (df):
    '''this function receives a Dataframe and it stacks and converts the resulto into a new data frame with a format more appropiated'''
    df.set_index('Year',inplace=True)
    df = pd.DataFrame(df.stack())
    df.reset_index(inplace=True)
    return df

def charactersout (x):
    '''This functions takes out the character < and convert the result into a float.'''
    x = str(x)
    if '<' in x:
        x = x.replace('<','')
        return float(x)
    else:
        return float(x)

def requestAPI (url):
    '''This function takes an URL in API format, and returns the response in json format if we get a correct response.'''

    # Get the response for the url.
    response = requests.get(url)

    # Check the code of the response and return accordingly.
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return print( f'Request failed, this is the error :   {response}')