import datetime

def get_current_time()->datetime:
    """
    Getting the current time

    Arguments
    ---------
    None
        
    Returns
    -------
    Datetime
    """
    now = datetime.datetime.now()
    return now

def add_current_time(now:datetime, duration:int)->datetime:
    """
    Adding the duration in current time
    
    Arguments
    ---------
    now:datetime
        It contains the current time
    duration: int
        Takes the duration in seconds for increment

    Returns
    -------
    datetime

    """
    time_change = datetime.timedelta(seconds=duration)
    new_time = now + time_change
    return new_time
