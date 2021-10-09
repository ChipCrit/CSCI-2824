class Clock:
    def get_position(self, max_hours, mins_passed):
        import math
        mins =0
        hours =0
        if(mins_passed<max_hours*60):
            hours = math.floor(mins_passed/60)  
            mins = mins_passed%60
            return (hours,mins)
        else:
            mins = mins_passed % (60*max_hours)
            hours = math.floor(mins/60)
            mins = mins -(60*hours)
            return (hours, mins)