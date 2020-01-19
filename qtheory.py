import pandas as pd
from datetime import datetime, timedelta
from . import utils
from . import arrivals
from . import service

#---------------------------------------
# Public Service functions
#---------------------------------------

def service_minutes_occurrence(start_service=[], end_service=[]):

    df = service._eval_service_minutes_occurrence(start_service, end_service)

    dictionary = {}
    aux = []

    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []

    for a in df['repetitions'].values:
        aux.append(a)
    dictionary['repetitions'] = aux

    return dictionary

def service_relative_frequencys(start_service=[], end_service=[]):
    df = service._eval_real_relative_frequencys(start_service, end_service)

    dictionary = {}
    aux = []
    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['repetitions'].values:
        aux.append(a)
    dictionary['repetitions'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    return dictionary

def service_theoretical_comparation(start_service=[], end_service=[], distribution='poisson'):
    df = service._eval_real_relative_frequencys(start_service, end_service)
    
    total_atendance = df.sum()['repetitions']
    total_minutes = service._eval_total_minutes(start_service, end_service)

    mlambda = total_minutes/total_atendance

    dictionary = {}
    aux = []
    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['repetitions'].values:
        aux.append(a)
    dictionary['repetitions'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    if distribution == 'poisson':

        df['poisson_relative_frequency'] = utils._poison_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['poisson_relative_frequency'].values:
            aux.append(a)
        dictionary['poisson_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['exponential_relative_frequency'] = utils._exponential_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['exponential_relative_frequency'].values:
            aux.append(a)
        dictionary['exponential_relative_frequency'] = aux
    
    elif distribution == 'exponentialnorm':

        df['exponentialnorm_relative_frequency'] = utils._exponentialnorm_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['exponentialnorm_relative_frequency'].values:
            aux.append(a)
        dictionary['exponentialnorm_relative_frequency'] = aux

    elif distribution == 'exponentialpow':

        df['exponentialpow_relative_frequency'] = utils._exponentialpow_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['exponentialpow_relative_frequency'].values:
            aux.append(a)
        dictionary['exponentialpow_relative_frequency'] = aux

    elif distribution == 'erlang':

        df['erlang_relative_frequency'] = utils._erlang_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['erlang_relative_frequency'].values:
            aux.append(a)
        dictionary['erlang_relative_frequency'] = aux
    
    elif distribution == 'gamma':

        df['gamma_relative_frequency'] = utils._gamma_distribution(mlambda, df['repetitions'].values)
        aux = []
        for a in df['gamma_relative_frequency'].values:
            aux.append(a)
        dictionary['gamma_relative_frequency'] = aux

    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary


#---------------------------------------
# Public Arrivals functions
#---------------------------------------
def arrivals_per_minutes(arr_date_time=[], index_period_beginning=[]):
    df = arrivals._eval_arrivals_per_minutes(arr_date_time, index_period_beginning)
    
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

def arrivals_relative_frequencys(arr_date_time=[], index_period_beginning=[]):
    df = arrivals._eval_real_relative_frequencys(arr_date_time, index_period_beginning)
    
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

def arrivals_theoretical_comparation(arr_date_time=[], index_period_beginning=[], distribution='poisson'):
    client_amout = len(arr_date_time)
    df = arrivals._eval_real_relative_frequencys(arr_date_time, index_period_beginning)
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

        df['poisson_relative_frequency'] = utils._poison_distribution(mlambda, df['arrivals_per_minutes'].values)
        aux = []
        for a in df['poisson_relative_frequency'].values:
            aux.append(a)
        dictionary['poisson_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['exponential_relative_frequency'] = utils._exponential_distribution(mlambda, df['arrivals_per_minutes'].values)
        aux = []
        for a in df['exponential_relative_frequency'].values:
            aux.append(a)
        dictionary['exponential_relative_frequency'] = aux
        
    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary

