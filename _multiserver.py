from math import factorial
from . import _stats

def _eval_Ws(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
     
    ls = _eval_Ls(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    mlambda = _stats._eval_rate(arrival_times, index_period_beginning_arrival)

    ws = ls / mlambda

    return ws

def _eval_Wq(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
    lq = _eval_Lq(c,  arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    mlambda = _stats._eval_rate(arrival_times, index_period_beginning_arrival)

    wq = lq / mlambda

    return wq

def _eval_Ls(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    lq = _eval_Lq(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    roh = _eval_roh(arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    ls = lq + roh

    return ls

def _eval_Lq(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    roh = _eval_roh(arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)
    p0 = _eval_p0(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    lq = ((roh ** (c + 1))/(factorial(c-1) * ((c-roh) ** 2))) * p0

    return lq

def _eval_pn(n, c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
    
    if c < 1:
        raise ValueError("The system has to have at last 1 server")

    if n < 0:
        raise ValueError("The number of clients/items in the queue must be at last 0")

    roh = _eval_roh(arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)
    p0 = _eval_p0(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)
    pn = 0

    if n < c:
        pn = ((roh ** n) / factorial(n)) * p0
    
    else:
        pn = ((roh ** n) / (factorial(c) * (c ** (n-c)))) * p0

    return pn

def _eval_p0(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
    
    if c < 2:
        raise ValueError("The system has to have at last 2 server")

    roh = _eval_roh(arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

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

def _eval_roh(arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    mlambda = _stats._eval_rate(arrival_times, index_period_beginning_arrival)

    mi = _stats._eval_rate(leave_times, index_period_beginning_leave)

    roh = mlambda/mi

    return roh

def _eval_lambda_n(n=0, arr_date_time=[], index_period_beginning=[]):
    lambda_n = 0
    if n >= 0:
        lambda_n = _stats._eval_rate(arr_date_time, index_period_beginning)
    else:
        raise ValueError("n must be bigger then 0, but n=" + n)

    return lambda_n

def _eval_mi_n(n=0, c=1, leave_times=[], index_period_beginning=[]):
    mi_n = 0

    if n < 0:
        raise ValueError("n must be equals or bigger then 0, but n=" + n)

    elif c < 1:
        raise ValueError("c must be at last 1, but c=" + n)

    else:
        mi = _stats._eval_rate(leave_times, index_period_beginning)

        if n < c:
            mi_n = n * mi
        else:
            mi_n = c * mi
    
    return mi_n
