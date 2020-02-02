from math import factorial
from . import _arrival
from . import _service
from . import _multiserver

#-------------------------------------------------
# Variables description
#-------------------------------------------------
# n is the number of people/items in the queue.
# c is the number of servers of the queue system.
#-------------------------------------------------

def eval_Ws(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
     
    ls = eval_Ls(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    mlambda = _arrival._eval_lambda(arr_date_time, index_period_beginning)

    ws = ls / mlambda

    return ws

def eval_Wq(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
    lq = _multiserver._eval_Lq(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    mlambda = _arrival._eval_lambda(arr_date_time, index_period_beginning)

    wq = lq / mlambda

    return wq

def eval_Ls(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    lq = _multiserver._eval_Lq(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    roh = _multiserver._eval_roh(arr_date_time, index_period_beginning, start_service, end_service)

    ls = lq + roh

    return ls

def eval_Lq(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    lq = _multiserver._eval_Lq(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    return lq

def eval_pn(n, c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
    """This funtion evaluate the probability do have 0 persons/items in the queue

        Parameters:

        n (int): It is the number of people in the queue. Must be equals or bigger then 0.

        c (int): It is the number of servers in the queue. Must be equals or bigger then 1.

        arr_date_time (str[]): It is the array of datetime. 
        The format must be: dd-mm-yyyy HH:MM:SS.

        index_period_beginning (int[]): It is the array of beggining positions in the date_time array.

        start_service (str[]): It is the array of datetime meaning the starting of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        end_service (str[]): It is the array of datetime meaning the ending of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        Returns:

        double:roh value

    """
    pn = _multiserver._eval_pn(n, c, arr_date_time, index_period_beginning, start_service, end_service)

    return pn

def eval_p0(c, arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):
    """This funtion evaluate the probability do have 0 persons/items in the queue

        Parameters:

        c (int): It is the number of servers in the queue. Must be equals or bigger then 1.

        arr_date_time (str[]): It is the array of datetime. 
        The format must be: dd-mm-yyyy HH:MM:SS.

        index_period_beginning (int[]): It is the array of beggining positions in the date_time array.

        start_service (str[]): It is the array of datetime meaning the starting of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        end_service (str[]): It is the array of datetime meaning the ending of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        Returns:

        double:roh value

    """
    p0 = _multiserver._eval_p0(c, arr_date_time, index_period_beginning, start_service, end_service)

    return p0

def eval_roh(arr_date_time=[], index_period_beginning=[], start_service=[], end_service=[]):

    """This funtion evaluate the roh = lambda/mi.

        Parameters:

        arr_date_time (str[]): It is the array of datetime. The format must be
        dd-mm-yyyy HH:MM:SS.

        index_period_beginning (int[]): It is the array of beggining positions in the date_time array.

        start_service (str[]): It is the array of datetime meaning the starting of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        end_service (str[]): It is the array of datetime meaning the ending of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        Returns:

        double:roh value

    """
    roh = _multiserver._eval_roh(arr_date_time, index_period_beginning, start_service, end_service)

    return roh


def eval_lambda_n(n=0, arr_date_time=[], index_period_beginning=[]):
    """This funtion evaluate the lambda n.

        Parameters:

        n (int): It is the number of people in the queue. Must be equals or bigger then 0.

        arr_date_time (str[]): It is the array of datetime. 
        The format must be: dd-mm-yyyy HH:MM:SS.

        index_period_beginning (int[]): It is the array of beggining positions in the date_time array.

        Returns:

        double:lambda_n value

    """
    lambda_n = _multiserver._eval_lambda_n(n, arr_date_time, index_period_beginning)

    return lambda_n

def eval_mi_n(n=0, c=1, start_service=[], end_service=[]):
    """This funtion evaluate the mi n.

        Parameters:

        n (int): It is the number of people in the queue. Must be equals or bigger then 0.

        c (int): It is the number of servers in the queue. Must be equals or bigger then 1.

        start_service (str[]): It is the array of datetime meaning the starting of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        end_service (str[]): It is the array of datetime meaning the ending of the service.
        The format must be: dd-mm-yyyy HH:MM:SS.

        Returns:

        double: mi_n value

    """
    mi_n = _multiserver._eval_mi_n(n, c, start_service, end_service)
    
    return mi_n
