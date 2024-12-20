from .feature import FeatureInterface
from tabulate import tabulate
from datetime import date as dt

class LogWaterIntake(FeatureInterface):
    def __init__(self, database, userid):
        self.database = database
        self.userid = userid
        self.hasGoal = False
        self.goal = 0
        self.date = dt.today().isoformat()
        self.checkGoal()
    
    def log(self, date, waterml=0):
        logs = self.database.getUserLogs(self.userid)
        
        if len(date.strip()) == 0:
            date = self.date
            
        self.database.updateWaterIntake(waterml, self.userid, date)

    def viewLogs(self):
        wiLogs  = []
        
        logs = self.database.getUserLogs(self.userid)
        
        if logs:
            for date in logs:
                data = [date, logs[date]['water intake']]
                wiLogs.append(data)
        
            wiLogs.sort()
            total = self.calculateTotal()
            avg = self.calculateAvg(total, logs)
            
            headers = ['Date', 'Water intake(ml)']
            print(tabulate(wiLogs, headers, tablefmt='grid'))
            
            print('\n--- Summary ---')
            print(f'Total water intake: {total} ml')
            print(f'Average water intake: {avg} ml')
            # goal feature
            
            if self.hasGoal and self.date in logs:
                currentIntake = logs[self.date]['water intake'] 
                print(f'Goal: {self.goal} ml')
                
                if currentIntake != self.goal:
                    print(f'Drink {(self.goal - currentIntake)} ml to reach your goal!')
                else:
                    print('You have reached your goal!')
            # display the requirement to reach the goal 
            
    def setGoal(self, goal):
        self.goal = goal
        self.database.updateWaterIntakeGoal(goal, self.userid, self.date)
        
    def checkGoal(self):
        logs = self.database.getUserLogs(self.userid)
        
        if self.date in logs:
            goal = logs[self.date]['water intake goal']
            
            if goal != 0:
                self.hasGoal = True    
                self.goal = goal
            else:
                self.hasGoal = False        
            
    def calculateTotal(self):
        logs = self.database.getUserLogs(self.userid)
        
        total = 0
        for date in logs:
            total += logs[date]['water intake']
            
        return round(total, 2)

    def calculateAvg(self, total, logs):
        numLogs = 0
        for date in logs:
            print(logs[date]['water intake'])
            if logs[date]['water intake'] != 0:
                numLogs += 1
        
        return round(total / numLogs, 2)
         