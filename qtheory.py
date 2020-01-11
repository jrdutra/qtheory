from datetime import datetime  
from datetime import timedelta 
import pandas as pd

def eval_occurrences(arr_date_time=[], index_period_beginning=[]):
    #convert in a pd dataframe
    df=pd.DataFrame(data=arr_date_time)
    df_values = df[0]
    repeats = df_values.value_counts()
    ocurrences = repeats.value_counts()

    ocurrences_per_minutes = _eval_ocurrences_per_minutes(ocurrences, df_values, index_period_beginning)

    arrivals_per_minutes = _eval_arrivals_per_minutes(ocurrences)

    df = _build_arrivals_df(arrivals_per_minutes, ocurrences_per_minutes)

    return df

#  return the numbers of occurrences of zero arrivals
def _eval_zeros_occurrences(df_values, index_period_beginning=[]):
    #convert de line of the pd in a python datetime value
    df_date_time =  pd.to_datetime(df_values, format='%Y-%m-%d %H:%M:%S')
    #get the ranges of observations
    rans = _build_eval_ranges(index_period_beginning)
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
def _build_eval_ranges(index_period_beginning=[]):
    vect_return = []
    for i, pivot in enumerate(index_period_beginning):
        if i < len(index_period_beginning)-1:
            ran = [pivot, index_period_beginning[i+1]-1]
            vect_return.append(ran)
    return vect_return

def _build_arrivals_df(arrivals_per_minutes=[], ocurrences_per_minutes=[]):
    #building the dataframe of arrivals
    lm =  list(zip(arrivals_per_minutes, ocurrences_per_minutes))
    df = pd.DataFrame(lm, columns = ['minutes','arrival_per_minutes'])
    return df

def _eval_ocurrences_per_minutes(ocurrences, df_values, index_period_beginning):
    ocurrences_per_minutes = ocurrences.values
    zerosAmount = _eval_zeros_occurrences(df_values, index_period_beginning)
    aux = [zerosAmount]
    for f in ocurrences_per_minutes:
        aux.append(f)
    ocurrences_per_minutes = aux
    return ocurrences_per_minutes

def _eval_arrivals_per_minutes(ocurrences):
    arrivals_per_minutes = ocurrences.index.values
    aux = [0] # já deixa  o espaço para entrar os valores de zero chegadas
    for c in arrivals_per_minutes:
        aux.append(c)
    arrivals_per_minutes = aux
    return arrivals_per_minutes