class Time:
    
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return a string representation of the Time object."""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __add__(self, t2):
        """Return the result of adding two Time objects using sum_times() method."""
        return self.sum_times(t2)


    def sum_times(self, t2):
        """Add two Time objects and return the sum as a new Time object."""
        sum_time = Time(0, 0, 0)
        
        # Sum the hours, minutes, and seconds
        sum_time.hour = self.hour + t2.hour
        sum_time.minute = self.minute + t2.minute
        sum_time.second = self.second + t2.second
        
        # Handle seconds overflow (if seconds >= 60, convert them to minutes)
        while sum_time.second >= 60:
            sum_time.second -= 60
            sum_time.minute += 1
        
        # Handle minutes overflow (if minutes >= 60, convert them to hours)
        while sum_time.minute >= 60:
            sum_time.minute -= 60
            sum_time.hour += 1
        
        return sum_time
    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        '''convert a time object to a single integer representing the 
        number of seconds from mid-night'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True
    def sec_to_time(seconds):
        '''convert a given number of seconds to a time object in 
            hour, minute, second format'''
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time



