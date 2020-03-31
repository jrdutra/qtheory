from . import _stats

#----------------------------------
# occurrence public functions
#----------------------------------

def rate(arr_date_time=[], index_period_beginning=[]):
    return _stats._eval_rate(arr_date_time, index_period_beginning)

def frequency(arr_date_time=[], index_period_beginning=[]):
    df = _stats._eval_frequency(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []

    for m in df['ocurrence'].values:
        aux.append(m)
    dictionary['ocurrence'] = aux
    
    aux = []

    for a in df['frequency'].values:
        aux.append(a)
    dictionary['frequency'] = aux

    return dictionary

def real_relative_frequency(arr_date_time=[], index_period_beginning=[]):
    df = _stats._eval_real_relative_frequency(arr_date_time, index_period_beginning)
    
    dictionary = {}
    aux = []
    for m in df['ocurrence'].values:
        aux.append(m)
    dictionary['ocurrence'] = aux
    
    aux = []
    for a in df['frequency'].values:
        aux.append(a)
    dictionary['frequency'] = aux

    aux = []
    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    return dictionary

def real_theoretical_comparation(arr_date_time=[], index_period_beginning=[], distribution='poisson'):
    
    client_amout = len(arr_date_time)

    df = _stats._eval_real_relative_frequency(arr_date_time, index_period_beginning)
    totalMinutes = sum(df['frequency'].values)

    rate = client_amout/totalMinutes

    dictionary = {}
    aux = []

    for m in df['ocurrence'].values:
        aux.append(m)
    dictionary['ocurrence'] = aux
    
    aux = []

    for a in df['frequency'].values:
        aux.append(a)
    dictionary['frequency'] = aux

    aux = []

    for a in df['real_relative_frequency'].values:
        aux.append(a)
    dictionary['real_relative_frequency'] = aux

    if distribution == 'poisson':

        df['theoretical_relative_frequency'] = _stats._poison_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['theoretical_relative_frequency'] = _stats._exponential_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux
        
    elif distribution == 'exponentialnorm':

        df['theoretical_relative_frequency'] = _stats._exponentialnorm_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux

    elif distribution == 'exponentialpow':

        df['theoretical_relative_frequency'] = _stats._exponentialpow_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux

    elif distribution == 'erlang':

        df['theoretical_relative_frequency'] = _stats._erlang_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux
    
    elif distribution == 'gamma':

        df['theoretical_relative_frequency'] = _stats._gamma_distribution(rate, df['ocurrence'].values)
        aux = []
        for a in df['theoretical_relative_frequency'].values:
            aux.append(a)
        dictionary['theoretical_relative_frequency'] = aux

    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary