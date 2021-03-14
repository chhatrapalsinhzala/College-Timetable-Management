import time
import datetime

def get_time(time_string):
    hours, minutes = [int(x) for x in time_string.split(':')]
    return time(hours, minutes)

def convert_to_date(date):
    """"
    Takes date in format YYYY-mm-dd
    Returns datetime object
    """
    if not date:
        return ''
    year,month, day,  = [int(val) for val in date.split('-')]
    return datetime(year, month, day)