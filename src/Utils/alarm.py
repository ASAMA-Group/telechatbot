import functools
import time
from datetime import timedelta , datetime



def time_alarm():

    timy2 = datetime.now() 
    delta2 = timedelta(hours=20 , minutes=00)
    if timy2 == '22:47':
        return f'start class:{timy2}'
    else:
        return f'az class gozashteh: {timy2 - delta2}'
