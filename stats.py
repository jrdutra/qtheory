from . import _stats
from . import _utils

#----------------------------------
# occurrence public functions
#----------------------------------

def eval_rate(arr_date_time=[], index_period_beginning=[]):
    return _stats._eval_rate(arr_date_time, index_period_beginning)

def occurrence_per_minutes(arr_date_time=[], index_period_beginning=[]):
    df = _stats._eval_occurrence_per_minutes(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []

    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []

    for a in df['occurrence_per_minutes'].values:
        aux.append(a)
    dictionary['occurrence_per_minutes'] = aux

    return dictionary

def occurrence_relative_frequencys(arr_date_time=[], index_period_beginning=[]):
    df = _stats._eval_real_relative_frequencys(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []
    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []
    for a in df['occurrence_per_minutes'].values:
        aux.append(a)
    dictionary['occurrence_per_minutes'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    return dictionary

def occurrence_theoretical_comparation(arr_date_time=[], index_period_beginning=[], distribution='poisson'):
    client_amout = len(arr_date_time)
    df = _stats._eval_real_relative_frequencys(arr_date_time, index_period_beginning)
    totalMinutes = sum(df['occurrence_per_minutes'].values)
    mlambda = client_amout/totalMinutes

    dictionary = {}
    aux = []

    for m in df['minutes'].values:
        aux.append(m)
    dictionary['minutes'] = aux
    
    aux = []

    for a in df['occurrence_per_minutes'].values:
        aux.append(a)
    dictionary['occurrence_per_minutes'] = aux

    aux = []

    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    if distribution == 'poisson':

        df['poisson_relative_frequency'] = _utils._poison_distribution(mlambda, df['occurrence_per_minutes'].values)
        aux = []
        for a in df['poisson_relative_frequency'].values:
            aux.append(a)
        dictionary['poisson_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['exponential_relative_frequency'] = _utils._exponential_distribution(mlambda, df['occurrence_per_minutes'].values)
        aux = []
        for a in df['exponential_relative_frequency'].values:
            aux.append(a)
        dictionary['exponential_relative_frequency'] = aux
        
    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary