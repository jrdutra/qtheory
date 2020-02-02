import scipy.stats as st
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

#input format ["yyyy-mm-dd HH:MM:SS"]
def _cls_seconds(arr=[]):
    toreturn=[]
    if(_is_date_time_formated(arr)):
        for item in arr:
            item = item[:17] + "00"
            toreturn.append(item)
        return toreturn
    

def _is_date_time_formated(arr=[]):
    for d in arr:
        if d == "NULL":
            raise ValueError('The value is NULL.')

        #verify the item lenth
        if len(d) != 19:
            raise ValueError('Incompatible data lenth.', 'Expected format: yyyy-mm-dd HH:MM:SS')
        
        #Verifing the date format
        date = d.split(" ")[0]
        if len(date) != 10:
            raise ValueError('Incompatible date format.', 'Expected format: yyyy-mm-dd')
        
        #separating date items
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]

        if len(year) != 4:
            raise ValueError('Incompatible year format.', 'Expected format: yyyy')
        if len(month) != 2:
            raise ValueError('Incompatible month format.', 'Expected format: mm')
        if len(day) != 2:
            raise ValueError('Incompatible day format.', 'Expected format: dd')
        if int(month) > 12:
            raise ValueError('Incompatible month value: ' + month)
        if int(day) > 31:
            raise ValueError('Incompatible day value: ' + day)
        
        #Verifing the time format
        time = d.split(" ")[1]
        if len(time) != 8:
            raise ValueError('Incompatible time format.', 'Expected format: HH:MM:SS')
        
        #separating time items
        hour = time.split(":")[0]
        minute = time.split(":")[1]
        second = time.split(":")[2]

        if len(hour) != 2:
            raise ValueError('Incompatible hour format.', 'Expected format: HH')
        if len(minute) != 2:
            raise ValueError('Incompatible minute format.', 'Expected format: MM')
        if len(second) != 2:
            raise ValueError('Incompatible second format.', 'Expected format: SS')
        if int(hour) > 24:
            raise ValueError('Incompatible hour value: ' + hour)
        if int(minute) > 60:
            raise ValueError('Incompatible minute value: ' + hour)
        if int(second) > 60:
            raise ValueError('Incompatible second value: ' + hour)
    return True

def _cls_not_str(vect=[]):
    v = vect
    ret = []
    for item in v:
        if type(item) is str:
            ret.append(item)
    return ret

def _verify_vect_pair(start_service=[], end_service=[]):
    
    if len(start_service) != len(end_service):
        raise ValueError('Incompatible size of both vectors.')
        
    if not _is_date_time_formated(start_service):
        raise ValueError('Incompatible format.')

    if not _is_date_time_formated(end_service):
        raise ValueError('Incompatible format.')

    return True

def _build_df(vect1, vect2, title1, title2):
    #building the dataframe of arrivals
    lm =  list(zip(vect1, vect2))
    df = pd.DataFrame(lm, columns = [title1, title2])
    return df

