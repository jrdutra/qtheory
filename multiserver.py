from math import factorial
from . import _multiserver

#-------------------------------------------------
# Variables description
#-------------------------------------------------
# n is the number of people/items in the queue.
# c is the number of servers of the queue system.
#-------------------------------------------------

def ws(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
     
    ws = _multiserver._eval_Ws(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return ws

def wq(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    wq = _multiserver._eval_Wq(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return wq

def ls(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    ls = _multiserver._eval_Ls(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return ls

def lq(c,  arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

    lq = _multiserver._eval_Lq(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return lq

def pn(n, c,  arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
    
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
    pn = _multiserver._eval_pn(n, c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return pn

def p0(c, arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):
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
    p0 = _multiserver._eval_p0(c, arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return p0

def roh(arrival_times=[], index_period_beginning_arrival=[], leave_times=[], index_period_beginning_leave=[]):

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
    roh = _multiserver._eval_roh(arrival_times, index_period_beginning_arrival, leave_times, index_period_beginning_leave)

    return roh


def lambda_n(n=0, arr_date_time=[], index_period_beginning=[]):
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

def mi_n(n=0, c=1, leave_times=[], index_period_beginning=[]):
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
    mi_n = _multiserver._eval_mi_n(n, c, leave_times, index_period_beginning)
    
    return mi_n
