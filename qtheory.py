from datetime import datetime  
from datetime import timedelta 
import pandas as pd

def calculate_zeros(arr_date_time=[], index_period_beginning=[]):
    #convert in a pd dataframe
    df=pd.DataFrame(data=arr_date_time)
    df_values = df[0]
    #convert de line of the pd in a python datetime value
    df_date_time =  pd.to_datetime(df_values, format='%Y-%m-%d %H:%M:%S')
    #get the ranges of observations
    rans = _build_ranges(index_period_beginning)
    #start the zeros amount
    qtZeros = 0
    # evaluate all minuts with zero arriving in the 
    # range of observations
    for ran in rans:
        #pega primeira data do intervalo
        database = df_date_time[ran[0]]
        for i in range(ran[0], ran[1]):
            if database != df_date_time[i]:
                qtZeros = qtZeros + 1
            database + timedelta(minutes=1)     
    print(qtZeros)

def _build_ranges(index_period_beginning=[]):
    vect_return = []
    for i, pivot in enumerate(index_period_beginning):
        if i < len(index_period_beginning)-1:
            ran = [pivot, index_period_beginning[i+1]-1]
            vect_return.append(ran)
    return vect_return