import json
from datetime import date as dt

class Database:
    def __init__(self):
        self.db = self.loadDB()
        
    """ for modifying and retrieving user's logs and data"""        
    def updateUserLogs(self, log, userid):
        data = self.getData()
        
        for key in data:
            if key == userid:
                logs = data[key]['data']
                newLog = log
                
                logs.update(newLog)
                
                self.updateLog(data)
                return
        
    def getUserLogs(self, userid):
            data = self.getData()
            
            for key in data:
                if key == userid:
                    logs = data[key]['data']
                    return logs
                
    def getData(self):
        with open('database/db.json', 'r') as file:
            data = json.load(file)
            file.close()
            return data
        
    def updateLog(self, data):
        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)
            file.close()
            
    def updateData(self, dataname, value, date, userid):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date][f"{dataname}"] = value
        else:
            match dataname:
                case 'weight':
                    log = self.createData(date=date, weight=value)

                case 'height':
                    log = self.createData(date=date, height=value)

                case 'water intake':
                    log = self.createData(date=date, waterIntake=value)

                case 'water intake goal':
                    log = self.createData(date=date, waterIntakeGoal=value)

                case 'bed time':
                    log = self.createData(date=date, timeSlept=value)
                    
                case 'calories burned':
                    log = self.createData(date=date, caloriesBurned=value)
                    
                case 'activity':
                    log = self.createData(date=date, activity=value)
                    
                case 'duration':
                    log = self.createData(date=date, duration=value)
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateLog(data)
            
    """ log bed time sleep """
    def updateTimeSlept(self, userid, timeslept, date):
        self.updateData('bed time', timeslept, date, userid)

    """ log water intake """
    def updateWaterIntake(self, waterml, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date]['water intake'] = waterml
        else:
            log = self.createData(date=date,waterIntake=waterml)
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateLog(data)   
        
    def updateWaterIntakeGoal(self, waterml, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
            
        if date in logs:
            logs[date]['water intake goal'] = waterml
        else:
            log = self.createData(date=date,waterIntakeGoal=waterml)
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateLog(data) 

    """ log body measurement """  
    def updateWeight(self, weight, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date]['weight'] = weight
        else:
            log = self.createData(date=date, weight=weight)
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateLog(data)
    
    def updateHeight(self, height, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date]['height'] = height
        else:
            log = self.createData(date=date, height=height)
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateLog(data)
        
    """ log exercise routine """
    def updateCalories(self, calBurned, date, userid):
        self.updateData('calories burned', calBurned, date, userid)
        
    def updateActivity(self, activity, date, userid):
        self.updateData('activity', activity, date, userid)
        
    def updateDuration(self, duration, date, userid):
        self.updateData('duration', duration, date, userid)
        
        
    """ main database functionalities """
    def getUsers(self):
        users = {}
        data = self.getData()
            
        for key in data:
            users.update({data[key]['username'] : data[key]['password']})

        return users
    
    def generateUser(self, username, password):
        date_today = dt.today().isoformat()
        
        user = {abs(hash(username)) : 
                    {'username' : username,
                        'password' : password,
                        'data' : self.createData(date=date_today)
                    }}
        return user
    
    def addUser(self, username, password):
        user = self.generateUser(username, password)
        data = self.getData()
        data.update(user)
        self.updateLog(data)
    
    def loadDB(self):
        data = self.getData()
            
        if data:
            return data
        else:
            return None
            
    def refresh(self):
        self.db = self.loadDB()
        
    def getUserID(self, username):
        data = self.getData()
            
        for key in data:
            if data[key]['username'] == username:
                return key
            
    def createData(self, date=None, weight=0, height=0, waterIntake=0, waterIntakeGoal=0,
             timeSlept=0, caloriesBurned=0, activity=None, duration=0):
        data = {
                date: {
                    "weight": weight,
                    "height": height,
                    "water intake": waterIntake,
                    'water intake goal' : waterIntakeGoal,
                    "bed time": timeSlept,
                    "calories burned": caloriesBurned,
                    "activity": activity,
                    "duration": duration
                }}
        
        return data
            
        
       
        