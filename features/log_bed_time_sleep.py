from . import FeatureInterface
from tabulate import tabulate
import math

class LogBedTimeSleep(FeatureInterface):
    def __init__(self, database):
        self.database = database
        pass

    def log(self, userid, timeslept, date):
        if len(date.strip()) == 0:
            date = self.currentDate
        
        mins = self.convertTimeSleptToMins(timeslept)
        self.database.updateTimeSlept(userid, mins, date)

    def viewLogs(self, userid):
        btsLogs  = []
        
        logs = self.database.getUserLogs(userid)
        if logs:
            for date in logs:
                timeslept = self.convertToHrAndMin(logs[date]['bed time'])
                
                data = [date, f'{timeslept[0]}hr{timeslept[1]}min']
                btsLogs.append(data)
                
            avg = self.convertToHrAndMin(self.calculateAverage(logs, userid))
        
            btsLogs.sort()
            headers = ['Date', 
                       'Time slept']
            print(tabulate(btsLogs, headers, tablefmt='grid'))
            
            print('\n--- Summary ---')
            print(f'Average time slept: {avg[0]}hr{avg[1]}min ')
        
    def calculateAverage(self, logs, userid):
        total = self.calculateTotal(userid)
        
        if not total:
            return 0
        
        numLogs = 0
        for date in logs:
            if logs[date]['bed time'] != 0:
                numLogs += 1
        
        return int(round(total / numLogs, 2))
    
    def calculateTotal(self, userid):
        logs = self.database.getUserLogs(userid)
        
        total = 0
        for date in logs:
            total += logs[date]['bed time']
            
        return round(total, 2)
    
    """ 
        convert hr and min to minutes format
        minutes = (hrs * 60) + mins
        
        convert minutes format to hour and minute format
        hr = math.floor(minutes / 60)
        min = minutes - (hr * 60)
    """
    def convertTimeSleptToMins(self, timeslept):
        return (timeslept[0] * 60) + timeslept[1]

    def convertToHrAndMin(self, minutes):
        hrs = math.floor(minutes / 60)
        mins = minutes - (hrs * 60)
        return (hrs, mins)
    
        