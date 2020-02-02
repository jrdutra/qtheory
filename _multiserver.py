from math import factorial
from . import _arrival
from . import _service
from . import _utils

def _eval_Ws(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
     
    ls = _eval_Ls(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    mlambda = _arrival._eval_lambda(arr_date_time, index_period_beginning)

    ws = ls / mlambda

    return ws

def _eval_Wq(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
    lq = _eval_Lq(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    mlambda = _arrival._eval_lambda(arr_date_time, index_period_beginning)

    wq = lq / mlambda

    return wq

def _eval_Ls(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    lq = _eval_Lq(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    roh = _eval_roh(arr_date_time, index_period_beginning, start_service, end_service)

    ls = lq + roh

    return ls

def _eval_Lq(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    roh = _eval_roh(arr_date_time, index_period_beginning, start_service, end_service)

    p0 = _eval_p0(c, arr_date_time, index_period_beginning, start_service, end_service)

    lq = ((roh ** (c + 1))/(factorial(c-1) * ((c-roh) ** 2))) * p0

    return lq

def _eval_pn(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    if c < 1:
        raise ValueError("The system has to have at last 1 server")

    if n < 0:
        raise ValueError("The number of clients/items in the queue must be at last 0")

    roh = _eval_roh(arr_date_time, index_period_beginning, start_service, end_service)
    p0 = _eval_p0(c, arr_date_time, index_period_beginning, start_service, end_service)
    pn = 0

    if n < c:
        pn = ((roh ** n) / factorial(n)) * p0
    
    else:
        pn = ((roh ** n) / (factorial(c) * (c ** (n-c)))) * p0

    return pn

def _eval_p0(c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
    
    if c < 1:
        raise ValueError("The system has to have at last 1 server")

    roh = _eval_roh(arr_date_time, index_period_beginning, start_service, end_service)

    p0 = 0
    summ = 0

    if roh/c < 1:

        for n in range(0, c):
            
            aux = ((roh ** n) / factorial(n))
            summ = summ + aux

        term_a = summ
        term_b = ((roh ** c) / factorial(c))
        term_c = (1 / (1 - (roh / c)))

        res = term_a + (term_b * term_c)

        p0 = (res ** (-1))
        
    
    else:
        raise ValueError("roh/c must be lower then 1, but it is " + (roh/c))
    
    return p0

def _eval_roh(arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    mlambda = _arrival._eval_lambda(arr_date_time, index_period_beginning)

    mi = _service._eval_mi(start_service, end_service)

    
    
    roh = mlambda/mi

    return roh

def _eval_lambda_n(n=0, arr_date_time=[], index_period_beginning=[]):
    lambda_n = 0
    if n >= 0:
        lambda_n = _arrival._eval_lambda(arr_date_time, index_period_beginning)
    else:
        raise ValueError("n must be bigger then 0, but n=" + n)
    return lambda_n

def _eval_mi_n(n=0, c=1, start_service=[], end_service=[]):
    mi_n = 0

    if n < 0:
        raise ValueError("n must be equals or bigger then 0, but n=" + n)

    elif c < 1:
        raise ValueError("c must be at last 1, but c=" + n)

    else:
        mi = _service._eval_mi(start_service, end_service)

        if n < c:
            mi_n = n * mi
        else:
            mi_n = c * mi
    
    return mi_n
