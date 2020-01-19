from . import utils
from datetime import datetime, timedelta
import pandas as pd

def first_func(start_service=[], end_service=[]):
    #Execute if both pair is OK by data format or same size.

    df = _eval_real_relative_frequencys(start_service, end_service)

    return df

def _eval_real_relative_frequencys(start_service=[], end_service=[]):
    #Execute if both pair is OK by data format or same size.
    df_repetitions = _eval_service_minutes_occurrence(start_service, end_service)

    total_minutes = df_repetitions.sum()['repetitions']

    df_repetitions['real_relative_frequency'] = df_repetitions['repetitions'].divide(other = total_minutes)

    return df_repetitions

def _eval_service_minutes_occurrence(start_service=[], end_service=[]):
    #Clear not string values.
    start_service = utils._cls_not_str(start_service)
    end_service = utils._cls_not_str(end_service)

    #Execute if both pair is OK by data format or same size.
    if utils._verify_vect_pair(start_service, end_service):
        df = _eval_approximate_duration(start_service, end_service)
        #Calculate the repetitions
        repeats = df['approximate_duration'].value_counts()

        list_time = []
        for linha in repeats.index:
            list_time.append(linha.total_seconds()/60)
            
        list_repetitions = []
        for linha in repeats.values:
            list_repetitions.append(linha)

        df_repetitions = utils._build_df(list_time, list_repetitions, 'minutes', 'repetitions')
        return df_repetitions

def _eval_approximate_duration(start_service=[], end_service=[]):
    df = utils._build_df(start_service, end_service, 'start_service', 'end_service')
    # Convert to date time format
    df['start_service'] = pd.to_datetime(df['start_service'], format='%Y-%m-%d %H:%M:%S')
    df['end_service'] = pd.to_datetime(df['end_service'], format='%Y-%m-%d %H:%M:%S')
    
    # Calculate service_duration
    df['service_duration'] = df['end_service'] - df['start_service']

    #Aproximate the service suration do integer minutes
    df['approximate_duration'] = df['service_duration'].dt.ceil('1min')

    return df

def _eval_total_minutes(start_service=[], end_service=[]):
    #Clear not string values.
    start_service = utils._cls_not_str(start_service)
    end_service = utils._cls_not_str(end_service)

    df = _eval_approximate_duration(start_service, end_service)

    total_seconds = 0

    for i in range(df['service_duration'].count()):
        total_seconds = total_seconds + df['service_duration'][i].total_seconds()
    total_minutes = total_seconds/60
    
    return total_minutes