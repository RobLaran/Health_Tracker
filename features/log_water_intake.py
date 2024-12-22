from .feature import FeatureInterface
from tabulate import tabulate

class LogWaterIntake(FeatureInterface):
    def __init__(self, database):
        self.database = database
        self.hasGoal = False
        self.goal = 0
    
    def log(self, date, userid, waterml=0):
        if len(date.strip()) == 0:
            date = self.currentDate
            
        self.database.updateWaterIntake(waterml, userid, date)

    def viewLogs(self, userid):
        wiLogs  = []
        self.checkGoal(userid)
        
        logs = self.database.getUserLogs(userid)
        if logs:
            for date in logs:
                data = [date, logs[date]['water intake']]
                wiLogs.append(data)
        
            wiLogs.sort()
            total = self.calculateTotal(userid)
            avg = self.calculateAvg(total, logs)
            
            headers = ['Date', 'Water intake(ml)']
            print(tabulate(wiLogs, headers, tablefmt='grid'))
            
            print('\n--- Summary ---')
            print(f'Total water intake: {total} ml')
            print(f'Average water intake: {avg} ml')
            
            # goal feature
            if self.hasGoal and self.currentDate in logs:
                currentIntake = logs[self.currentDate]['water intake'] 
                print(f'Goal: {self.goal} ml')
                
                # display the requirement to reach the goal 
                if currentIntake != self.goal:
                    print(f'Drink {(self.goal - currentIntake)} ml to reach your goal!')
                else:
                    print('You have reached your goal!')
            
    def setGoal(self, goal, userid):
        if userid:
            self.goal = goal
            self.database.updateWaterIntakeGoal(goal, userid, self.currentDate)
        
    def checkGoal(self, userid):
        if userid:
            logs = self.database.getUserLogs(userid)
            if self.currentDate in logs:
                goal = logs[self.currentDate]['water intake goal']
                
                if goal != 0:
                    self.hasGoal = True    
                    self.goal = goal
                else:
                    self.hasGoal = False        
            
    def calculateTotal(self, userid):
        logs = self.database.getUserLogs(userid)
        
        total = 0
        for date in logs:
            total += logs[date]['water intake']
            
        return round(total, 2)

    def calculateAvg(self, total, logs):
        if not total:
            return 0
        
        numLogs = 0
        for date in logs:
            if logs[date]['water intake'] != 0:
                numLogs += 1
        
        return round(total / numLogs, 2)
         