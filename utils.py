import scipy.stats as st
from datetime import datetime, timedelta
import pandas as pd

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

#------------------------------------------------------
#        ARRIVALS
#------------------------------------------------------

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

