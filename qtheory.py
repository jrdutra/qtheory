import pandas as pd
from datetime import datetime, timedelta
from .utils import _cls_seconds
from .utils import _build_arrivals_per_minutes
from .utils import _build_sample_minutes
from .utils import _build_arrivals_df
from .utils import _poison_distribution
from .utils import _exponential_distribution

def arrival_theoretical_comparation(arr_date_time=[], index_period_beginning=[], distribution='poisson'):
    client_amout = len(arr_date_time)
    df = _eval_real_relative_frequencys(arr_date_time, index_period_beginning)
    totalMinutes = sum(df['arrivals_per_minutes'].values)
    mlambda = client_amout/totalMinutes

    dictionary = {}
    aux = []

    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['arrivals_per_minutes'].values:
        aux.append(a)
    dictionary['arrivals_per_minutes'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    if distribution == 'poisson':

        df['poisson_relative_frequency'] = _poison_distribution(mlambda, df['arrivals_per_minutes'].values)
        aux = []
        for a in df['poisson_relative_frequency'].values:
            aux.append(a)
        dictionary['poisson_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['exponential_relative_frequency'] = _exponential_distribution(mlambda, df['arrivals_per_minutes'].values)
        aux = []
        for a in df['exponential_relative_frequency'].values:
            aux.append(a)
        dictionary['exponential_relative_frequency'] = aux
        
    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary

def real_relative_frequencys(arr_date_time=[], index_period_beginning=[]):
    df = _eval_real_relative_frequencys(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []
    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['arrivals_per_minutes'].values:
        aux.append(a)
    dictionary['arrivals_per_minutes'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    return dictionary

def _eval_real_relative_frequencys(arr_date_time=[], index_period_beginning=[]):
    df = _eval_arrivals_per_minutes(arr_date_time, index_period_beginning)
    #calculate the total minutes of all observation
    totalMinutes = sum(df['arrivals_per_minutes'].values)
    #divide all lines of the column arrivals_per_minuts for totalMinutes
    df['real_relative_frequency'] = df['arrivals_per_minutes'].divide(other = totalMinutes)
    return df

def arrivals_per_minutes(arr_date_time=[], index_period_beginning=[]):
    df = _eval_arrivals_per_minutes(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []
    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['arrivals_per_minutes'].values:
        aux.append(a)
    dictionary['arrivals_per_minutes'] = aux

    return dictionary


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
