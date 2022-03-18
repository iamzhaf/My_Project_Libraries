#
#
# Created By: Zhafran
# Created On: 2nd July 2021
#
#
#


import numpy as np
import pandas as pd
import os,sys
import scipy.stats as stats
import math
from tabulate import tabulate


def first_moment(variable):

    return round(np.mean(variable),4)


def second_moment(variable):

    return round(np.var(variable),6)


def median(variable):

    return np.nanmedian(variable)


def get_max(variable):

    return np.max(variable)


def get_min(variable):

    return np.min(variable)


def get_summary_statistics(variable):


    statistics = {
                    "N":len(variable),"Max":get_max(variable),"Min":get_min(variable),"Mean":first_moment(variable),"Median":median(variable),"Variance":second_moment(variable),
                    "Standard Deviation":math.sqrt(second_moment(variable)),"Skewness":round(stats.skew(variable),3),"Excess Kurtosis":round(stats.kurtosis(variable,nan_policy="omit"),3)
                 }

    return statistics



def print_summary_statistics(data,variables=None):
    """Computes the summary statistics (i.e. N,min,max,range,25th,50th,75th,IQR,mean,variance,standard deviation,skewness, and excess kurtosis) of a variable.

    Args:
        data ([pandas dataframe | pandas series]): The underlying data for statistical analysis
        variable ([list|None]): The variable of interest for summary statisical
    """

    temp_results_holder = {}

    if isinstance(data,pd.DataFrame):

        if variables == None:

            variables = data.columns

        result_table_column = ["Statistics"] + [x for x in variables]


        for v in variables:

            temp_results_holder[v] = get_summary_statistics(data[v])


    if isinstance(data,np.ndarray) or isinstance(data,pd.Series):

        result_table_column = ["Statistics","Values"]

        temp_results_holder["v"] = get_summary_statistics(data)


    # Create results table

    # print(result_table_column)

    results_table = [["N"],["Max"],["Min"],["Mean"],["Median"],["Variance"],["Standard Deviation"],["Skewness"],["Excess Kurtosis"]]

    for v in temp_results_holder.keys():

        for i,m in enumerate(temp_results_holder[v].keys()):

            results_table[i].append(temp_results_holder[v][m])

    # print summary statisics

    results_table = pd.DataFrame(np.insert(np.array(results_table),0,np.array(result_table_column),0),columns=result_table_column)

    print(tabulate(results_table.iloc[1:,:],headers=results_table.iloc[0,:].values,numalign="left"))




if __name__ == "__main__":

    pass
