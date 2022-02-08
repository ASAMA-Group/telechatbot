import functools
import time
import datetime



def time_alarm(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("hi guys!!!")
        
        timy = datetime.datetime.now().strftime("%H:%M")
        counter = 2
        for i in range(counter):
            if timy == "21:58":
                print(f"class time: {timy}")
            time.sleep(10)
        
        result = func(*args, **kwargs)
        return result
    return wrapper