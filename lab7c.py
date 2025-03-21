#!/usr/bin/env python3
# Student ID: [seneca_id]
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second


def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1

        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1
        
        while time.second < 0:
             time.second += 60
             time.minute -=1
        while time.minute < 0:
             time.minute += 60
             time.hour -= 1

        
    return None

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Handle carry over for seconds
    carry_minutes = sum.second // 60
    sum.second = sum.second - (carry_minutes * 60)

    # Add carry over to minutes
    sum.minute = sum.minute + carry_minutes

    # Handle carry over for minutes
    carry_hours = sum.minute // 60
    sum.minute = sum.minute - (carry_hours * 60)

    # Add carry over to hours
    sum.hour = sum.hour + carry_hours
        
    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

...
...
def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time
...
...

# Testing the function
time1 = Time(9, 50, 0)
print(format_time(time1))  # '09:50:00'

change_time(time1, 1800)
print(format_time(time1))  # '10:20:00'

time2 = Time(10, 20, 0)
change_time(time2, -1800)
print(format_time(time2))  # '09:50:00'

time3 = Time(10, 0, 0)
change_time(time3, -1800)
print(format_time(time3))  # '09:30:00'