from datetime import datetime, timedelta
import pandas as pd
import scipy.stats as st
from . import _utils

#----------------------------------
# Stats private functions
#----------------------------------

def _eval_real_relative_frequency(arr_date_time=[], index_period_beginning=[]):
    df = _eval_frequency(arr_date_time, index_period_beginning)
    #calculate the total minutes of all observation
    totalMinutes = sum(df['frequency'].values)
    #divide all lines of the column occurrence_per_minuts for totalMinutes
    df['real_relative_frequency'] = df['frequency'].divide(other = totalMinutes)
    return df

def _eval_frequency(arr_date_time=[], index_period_beginning=[]):
    #set all seconds data to zero
    arr_date_time = _utils._cls_seconds(arr_date_time)
    #convert in a pd dataframe
    df=pd.DataFrame(data=arr_date_time)

    df_values = df[0]

    repeats = df_values.value_counts()
    
    no_zero_frequency = repeats.value_counts()

    frequency = _build_frequency_per_minutes(no_zero_frequency, df_values, index_period_beginning)

    sample_minutes = _build_sample_minutes(no_zero_frequency)

    df = _build_frequency_df(sample_minutes, frequency)

    return df

def _eval_rate(arr_date_time=[], index_period_beginning=[]):
    #Execute if both pair is OK by data format or same size.

    client_amout = len(arr_date_time)

    df = _eval_real_relative_frequency(arr_date_time, index_period_beginning)

    totalMinutes = sum(df['frequency'].values)

    rate = client_amout/totalMinutes

    return rate

#--------------------------------------------------------------------------------
#  return the numbers of occurrences of zero occurrence
def _eval_zeros_occurrence(df_values, index_period_beginning=[]):
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

def _build_frequency_df(sample_minutes=[], frequency=[]):
    #building the dataframe of occurrence
    df = _utils._build_df(sample_minutes, frequency, 'ocurrence', 'frequency')
    return df

def _build_frequency_per_minutes(no_zero_frequency, df_values, index_period_beginning):
    #build an array of ocurrences per minutes
    no_zero_frequency = no_zero_frequency.values
    zerosAmount = _eval_zeros_occurrence(df_values, index_period_beginning)
    aux = [zerosAmount]
    for f in no_zero_frequency:
        aux.append(f)
    frequency = aux
    return frequency

def _build_sample_minutes(ocurrences):
    occurrence_per_minutes = ocurrences.index.values
    aux = [0] #create de space to put the zeros occurrence informations
    for c in occurrence_per_minutes:
        aux.append(c)
    occurrence_per_minutes = aux
    return occurrence_per_minutes

#--------------------------------------------------------------------------------
#  Distributions

def _poison_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.poisson.pmf(x,lamb))
    return aux

def _exponential_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.expon.pdf(x, 0, lamb))
    return aux

def _exponentialnorm_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.exponnorm.pdf(x, lamb))
    return aux

def _exponentialpow_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.exponpow.pdf(x, lamb))
    return aux

def _erlang_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.erlang.pdf(x, lamb))
    return aux

def _gamma_distribution(lamb, vet=[]):
    aux=[]
    for x in vet:
        aux.append(st.gamma.pdf(x, lamb))
    return aux
