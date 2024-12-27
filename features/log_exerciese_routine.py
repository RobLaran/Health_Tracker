from . import FeatureInterface
from tabulate import tabulate
import math

class LogExerciseRoutine(FeatureInterface):
    def __init__(self, database):
        self.database = database
    
    def log(self, calburned, activity, duration, date, userid):
        if len(date) == 0 or not date:
            date = self.currentDate
        
        mins = self.convertToMins(duration)
        self.database.updateCalories(calburned, date, userid)
        self.database.updateActivity(activity, date, userid)
        self.database.updateDuration(mins, date, userid)

    def viewLogs(self, userid):
        erLogs  = []
        
        logs = self.database.getUserLogs(userid)
        if logs:
            for date in logs:
                duration = self.convertToHrAndMin(logs[date]['duration'])
                
                data = [date, logs[date]['calories burned'],
                        logs[date]['activity'], f'{duration[0]}hr{duration[1]}min']
                erLogs.append(data)
                
            erLogs.sort()
            headers = ['Date', 'Burned calories', "Activity", "Duration"]
            print(tabulate(erLogs, headers, tablefmt='grid'))
            
            calburned = self.calculateAverage(logs, userid)
            print('\n--- Summary ---')
            print(f"Average calories burned: {calburned} kcal")
            self.activityList(userid)
        return super().viewLogs()
    
    def convertToMins(self, duration):
        return (duration[0] * 60) + duration[1]
    
    def convertToHrAndMin(self, minutes):
        hrs = math.floor(minutes / 60)
        mins = minutes - (hrs * 60)
        return (hrs, mins)
    
    def calculateAverage(self, logs, userid):
        total = self.calculateTotal(userid)
        
        if not total:
            return 0
        
        numLogs = 0
        for date in logs:
            if logs[date]['calories burned'] != 0:
                numLogs += 1
        
        return int(round(total / numLogs, 2))
    
    def calculateTotal(self, userid):
        logs = self.database.getUserLogs(userid)
        
        total = 0
        for date in logs:
            total += logs[date]['calories burned']
            
        return round(total, 2)
    
    def loadActivities(self, logs):
        activities = set()
        
        for date in logs:
            if logs[date]['activity']:
                activities.add(logs[date]['activity'])

        return activities
        
    def activityList(self, userid):
        logs = self.database.getUserLogs(userid)
        
        list = {'Activites' : self.loadActivities(logs)}
        
        print(tabulate(list, headers='keys', tablefmt='grid'))