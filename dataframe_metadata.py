import pandas as pd
import numpy as np
import pprint
from tabulate import tabulate



def dataframe_metadata(dataframe,print_metadata=True):

    columns = dataframe.columns

    table = [["Col #","Column Name","Data Type","Entries","Missing Entries","Percent Missing Entries"]]
    
    for i,col in enumerate(columns):

        percent_missing_entries = round((pd.isnull(dataframe[col]).sum() / len(dataframe[col]))*100,0)

        table.append([i,col,dataframe[col].dtypes,len(dataframe[col]),pd.isnull(dataframe[col]).sum(),"{}%".format(percent_missing_entries)])


    if print_metadata:

        print("Total Entries in dataset: {}".format(len(dataframe)))

        print(tabulate(table))

        # return pd.DataFrame(table[1:],columns=table[0])


    else:

        return pd.DataFrame(table[1:],columns=table[0])
    

