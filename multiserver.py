from . import _arrival
from . import _service
from . import _multiserver

#-------------------------------------------------
# Variables description
#-------------------------------------------------
# n is the number of people/items in the queue.
# c is the number of servers of the queue system.
#-------------------------------------------------

def eval_lambda_n(n=0, arr_date_time=[], index_period_beginning=[]):
    """This funtion evaluate the lambda n.

        Parameters:

            n (int): It is the number of people in the queue. Must be equals or bigger then 0.

            arr_date_time (str[]): It is the array of datetime. The format must be
            dd-mm-yyyy HH:MM:SS.

            arr_date_time (int[]): It is the array of beggining positions in the date_time array.

        Returns:

            double:lambda_n value

    """
    lambda_n = _multiserver._eval_lambda_n(n, arr_date_time, index_period_beginning)

    return lambda_n

def eval_mi_n(n=0, c=1, start_service=[], end_service=[]):
    """This funtion evaluate the mi n.

        Parameters:

            n (int): It is the number of people in the queue. Must be equals or bigger then 0.

            start_service (str[]): It is the array of datetime meaning the starting of the service.
            The format must be dd-mm-yyyy HH:MM:SS.

            end_service (str[]): It is the array of datetime meaning the ending of the service.
            The format must be dd-mm-yyyy HH:MM:SS.

        Returns:
        
            double: mi_n value

    """
    mi_n = _multiserver._eval_mi_n(n, c, start_service, end_service)
    
    return mi_n
