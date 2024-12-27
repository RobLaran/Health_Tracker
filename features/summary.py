from datetime import date 
import math

class Summary:
    def __init__(self, database):
        self.database = database
        self.year = date.today().year
        self.month = date.today().month
    
    def summaries(self, userid):
        self.data = self.database.getUserLogs(userid)
        
        
        avgtimeslept = self.averageTimeslept()
        totaltimeslept = self.totalTimeslept()
        
        print(f"""
--- Monthly Summary of {date.today().strftime("%B %Y")} ---
Average weight: {self.averageWeight()} kg
Average height: {self.averageHeight()} cm
Average time slept: {avgtimeslept[0]}hr{avgtimeslept[1]}min
Average calories burned: {self.averageCaloriesBurned()} kcal
Average water intake: {self.averageWaterIntake()} ml
Total time slept: {totaltimeslept[0]}hr{totaltimeslept[1]}min
Total calories burned: {self.totalCaloriesburned()} kcal
Total water intake: {self.totalWaterIntake()} ml
        """)
    
    def calculateAverage(self, type):
        total = self.calculateTotal(type)
        
        if not total:
            return 0
        
        numLogs = 0
        for dt in self.data:
            if self.data[dt][type] != 0 and date.fromisoformat(dt).year == self.year and date.fromisoformat(dt).month == self.month:
                numLogs += 1
        
        return round(total / numLogs, 2)    
    
    def calculateTotal(self, type):
        total = 0
        for dt in self.data:
            if date.fromisoformat(dt).year == self.year and date.fromisoformat(dt).month == self.month:
                total += self.data[dt][f"{type}"]
            
        return round(total, 2)
    
    def averageWeight(self):
        return self.calculateAverage("weight")
    
    def averageHeight(self):
        return self.calculateAverage("height")
    
    def averageTimeslept(self):
        return self.convertToHrAndMin(self.calculateAverage("bed time"))
        
    def averageWaterIntake(self):
        return self.calculateAverage("water intake")
    
    def averageCaloriesBurned(self):
        return self.calculateAverage("calories burned")
    
    def totalTimeslept(self):
        return self.convertToHrAndMin(self.calculateTotal("bed time"))

    def totalCaloriesburned(self):
        return self.calculateTotal("calories burned")
    
    def totalWaterIntake(self):
        return self.calculateTotal("water intake")
    
    def convertToHrAndMin(self, minutes):
        minutes = int(minutes)
        hrs = math.floor(minutes / 60)
        mins = minutes - (hrs * 60)
        return (hrs, mins)
