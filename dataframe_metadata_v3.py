import pandas as pd
import numpy as np
import pprint
from tabulate import tabulate


class GetMetaData():
    """
    Class object that generates the metdata of a dataframe.

    Functionalities include: get the metadata of the dataframe, 
    tabulates the metadata and returns the metadata
    """

    def __init__(self,dataframe):

        self.df = dataframe

        self.total_rows = len(dataframe)


    def create_metadata(self):
        """Creates a metadata of the dataframe of interest. Shows the total entries/rows, 
            list of columns, number and percentage of missing entries in each column. 

        Args:
            dataframe (pandas dataframe): The dataframe of interest. 
            return_metadata (bool, optional): Defaults to True.

        """

        dataframe = self.df

        columns = dataframe.columns

        table = [["Col #","Column Name","Data Type","Total Rows","Missing Values","Missing Values %"]]

        for i,col in enumerate(columns):

            percent_missing_entries = round((pd.isnull(dataframe[col]).sum() / len(dataframe[col]))*100,2)

            table.append([
                            i+1,
                            col,
                            dataframe[col].dtypes,
                            len(dataframe[col]),
                            pd.isnull(dataframe[col]).sum(),"{}%".format(percent_missing_entries)]
                        )

        return table


    def print_metadata(self):

        result = self.create_metadata()

        print(f"Total Number of Rows/Entries: {self.total_rows}")

        print(tabulate(result))

    
    def return_metadata(self):
        """
        Return the result as pandas dataframe
        """

        result = self.create_metadata()

        return pd.DataFrame(result[1:],columns=result[0])

if __name__ == "__main__":


    df = pd.DataFrame([[1,2,3],[3,4,5]],columns=["A","B","C"])

    print(GetMetaData(df).return_metadata())