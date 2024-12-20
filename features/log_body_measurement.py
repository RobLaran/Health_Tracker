from features.feature import FeatureInterface
from tabulate import tabulate
from datetime import date as dt

class LogBodyMeasurement(FeatureInterface):
    def __init__(self, database):
        self.database = database
        self.date = dt.today().isoformat()
        
    def log(self, userid, date, weight=0, height=0):
        logs = self.database.getUserLogs(userid)
        
        if len(date.strip()) == 0:
            date = self.date
        
        self.database.updateWeight(weight, userid, date)
        self.database.updateHeight(height, userid, date)
                
    def viewLogs(self, userid):
        bmLogs  = []
        
        logs = self.database.getUserLogs(userid)
        
        if logs:
            for date in logs:
                data = [date, logs[date]['weight'], logs[date]['height']]
                bmLogs.append(data)
        
            bmLogs.sort()
            currentWeight = bmLogs[-1][1]
            currentHeight = bmLogs[-1][2]
            
            avgweight = self.calculateAVGWeight(bmLogs)
            avgheight = self.calculateAVGHeight(bmLogs)
            bmi, status = self.calculateBMI(currentWeight, currentHeight)
            
            headers = ['Date', 'Weight(kg)','Height(cm)']
            print(tabulate(bmLogs, headers, tablefmt='grid'))
            
            print('\n--- Summary ---')
            print(f'Current weight: {currentWeight} kg')
            print(f'Current height: {currentHeight} cm')
            print(f'Average weight: {avgweight} kg')
            print(f'Average height: {avgheight} cm')
            print(f'BMI: {bmi}')
            print(f'Status: {status}')
        
    def calculateBMI(self, weight, height):
        if weight and height:
            bmi = weight / (pow(height / 100, 2))
            
            if bmi <= 18.4:
                status = 'Underweight'
            elif bmi >= 18.5 and bmi <= 24.9:
                status = 'Normal'
            elif bmi >= 25.0 and bmi <= 39.9: 
                status = 'Overweight'
            else:
                status = 'Obese'
        else:
            bmi = 0
            status = "Undefined"
            
        return (round(bmi, 2), status)
    
    def calculateAVGWeight(self, data):
        numberOfData = len(data)
        sum = 0 
        
        for weight in data:
            sum += weight[1]
        
        avg = sum / numberOfData
        return round(avg, 2)
    
    def calculateAVGHeight(self, data):
        numberOfData = len(data)
        sum = 0 
        
        for height in data:
            sum += height[2]
        
        avg = sum / numberOfData
        return round(avg, 2)
        