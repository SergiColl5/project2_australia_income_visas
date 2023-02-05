import pandas as pd
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
    x = str(x)
    if '<' in x:
        x = x.replace('<','')
        return float(x)
    else:
        return float(x)