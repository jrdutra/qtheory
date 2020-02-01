from . import _arrival
from . import _service

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
