import datetime

def get_current_time()->datetime:
    """
    """
    now = datetime.datetime.now()
    return now

def add_current_time(now:datetime, duration:int)->datetime:
    """
    
    """
    time_change = datetime.timedelta(seconds=duration)
    new_time = now + time_change
    return new_time
