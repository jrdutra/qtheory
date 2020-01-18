from datetime import datetime, timedelta
from .utils import _cls_seconds
from .utils import _poison_distribution
from .utils import _exponential_distribution
import pandas as pd

def _eval_real_relative_frequencys(arr_date_time=[], index_period_beginning=[]):
    df = _eval_arrivals_per_minutes(arr_date_time, index_period_beginning)
    #calculate the total minutes of all observation
    totalMinutes = sum(df['arrivals_per_minutes'].values)
    #divide all lines of the column arrivals_per_minuts for totalMinutes
    df['real_relative_frequency'] = df['arrivals_per_minutes'].divide(other = totalMinutes)
    return df

def _eval_arrivals_per_minutes(arr_date_time=[], index_period_beginning=[]):
    #set all seconds data to zero
    arr_date_time = _cls_seconds(arr_date_time)
    #convert in a pd dataframe
    df=pd.DataFrame(data=arr_date_time)
    df_values = df[0]
    repeats = df_values.value_counts()
    ocurrences = repeats.value_counts()

    arrivals_per_minutes = _build_arrivals_per_minutes(ocurrences, df_values, index_period_beginning)

    sample_minutes = _build_sample_minutes(ocurrences)

    df = _build_arrivals_df(sample_minutes, arrivals_per_minutes)

    return df

#  return the numbers of occurrences of zero arrivals
def _eval_zeros_arrivals(df_values, index_period_beginning=[]):
    #convert de line of the pd in a python datetime value
    df_date_time =  pd.to_datetime(df_values, format='%Y-%m-%d %H:%M:%S')
    #get the ranges of observations
    rans = _build_ranges(index_period_beginning)
    #start the zeros amount
    zerosAmount = 0
    # evaluate all minuts with zero arriving in the 
    # range of observations
    for ran in rans:
        #pega primeira data do intervalo
        database = df_date_time[ran[0]]
        for i in range(ran[0], ran[1]):
            if database != df_date_time[i]:
                zerosAmount = zerosAmount + 1
            database + timedelta(minutes=1)     
    return zerosAmount

#return the ranges of queue evaluation
def _build_ranges(index_period_beginning=[]):
    vect_return = []
    for i, pivot in enumerate(index_period_beginning):
        if i < len(index_period_beginning)-1:
            ran = [pivot, index_period_beginning[i+1]-1]
            vect_return.append(ran)
    return vect_return

def _build_arrivals_df(sample_minutes=[], arrivals_per_minutes=[]):
    #building the dataframe of arrivals
    lm =  list(zip(sample_minutes, arrivals_per_minutes))
    df = pd.DataFrame(lm, columns = ['minutes','arrivals_per_minutes'])
    return df

def _build_arrivals_per_minutes(ocurrences, df_values, index_period_beginning):
    #build an array of ocurrences per minutes
    ocurrences_per_minutes = ocurrences.values
    zerosAmount = _eval_zeros_arrivals(df_values, index_period_beginning)
    aux = [zerosAmount]
    for f in ocurrences_per_minutes:
        aux.append(f)
    ocurrences_per_minutes = aux
    return ocurrences_per_minutes

def _build_sample_minutes(ocurrences):
    arrivals_per_minutes = ocurrences.index.values
    aux = [0] #create de space to put the zeros arrivals informations
    for c in arrivals_per_minutes:
        aux.append(c)
    arrivals_per_minutes = aux
    return arrivals_per_minutes