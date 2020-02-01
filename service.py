from . import _service
from . import _utils

#---------------------------------------
# Service public functions
#---------------------------------------

def eval_mi(start_service=[], end_service=[]):
    return _service._eval_mi(start_service, end_service)

def service_minutes_occurrence(start_service=[], end_service=[]):

    df = _service._eval_service_minutes_occurrence(start_service, end_service)

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
    df = _service._eval_real_relative_frequencys(start_service, end_service)

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
    df = _service._eval_real_relative_frequencys(start_service, end_service)
    
    #total_atendance = df.sum()['repetitions']
    #total_minutes = service._eval_total_minutes(start_service, end_service)

    #mi = total_minutes/total_atendance
    mi = _service._eval_mi(start_service, end_service)

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

        df['poisson_relative_frequency'] = _utils._poison_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['poisson_relative_frequency'].values:
            aux.append(a)
        dictionary['poisson_relative_frequency'] = aux

    elif distribution == 'exponential':

        df['exponential_relative_frequency'] = _utils._exponential_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['exponential_relative_frequency'].values:
            aux.append(a)
        dictionary['exponential_relative_frequency'] = aux
    
    elif distribution == 'exponentialnorm':

        df['exponentialnorm_relative_frequency'] = _utils._exponentialnorm_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['exponentialnorm_relative_frequency'].values:
            aux.append(a)
        dictionary['exponentialnorm_relative_frequency'] = aux

    elif distribution == 'exponentialpow':

        df['exponentialpow_relative_frequency'] = _utils._exponentialpow_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['exponentialpow_relative_frequency'].values:
            aux.append(a)
        dictionary['exponentialpow_relative_frequency'] = aux

    elif distribution == 'erlang':

        df['erlang_relative_frequency'] = _utils._erlang_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['erlang_relative_frequency'].values:
            aux.append(a)
        dictionary['erlang_relative_frequency'] = aux
    
    elif distribution == 'gamma':

        df['gamma_relative_frequency'] = _utils._gamma_distribution(mi, df['repetitions'].values)
        aux = []
        for a in df['gamma_relative_frequency'].values:
            aux.append(a)
        dictionary['gamma_relative_frequency'] = aux

    else:
        raise ValueError('Unrecognized Distribution: ' + distribution)

    return dictionary