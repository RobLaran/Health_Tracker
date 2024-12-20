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
                
                self.updateData(data)
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
        
    def updateData(self, data):
        with open('database/db.json', 'w') as file:
            json.dump(data, file, indent=4)
            file.close()
            
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
            log = {
                date: {
                    "weight": 0,
                    "height": 0,
                    "water intake": waterml,
                    'water intake goal' : 0,
                    "bed time": 0,
                    "calories burned": 0
                }}
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateData(data)   
        
    def updateWaterIntakeGoal(self, waterml, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
            
        if date in logs:
            logs[date]['water intake goal'] = waterml
        else:
            log = {
                date: {
                    "weight": 0,
                    "height": 0,
                    "water intake": 0,
                    'water intake goal' : waterml,
                    "bed time": 0,
                    "calories burned": 0
                }}
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateData(data) 

    """ for updating data in body measurement   """  
    def updateWeight(self, weight, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date]['weight'] = weight
        else:
            log = {
                date: {
                    "weight": weight,
                    "height": 0,
                    "water intake": 0,
                    "bed time": 0,
                    "calories burned": 0
                }}
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateData(data)
    
    def updateHeight(self, height, userid, date):
        data = self.getData()
            
        for key in data:
            if key == userid:
                logs = data[key]['data']
                break
            
        if date in logs:
            logs[date]['height'] = height
        else:
            log = {
                date: {
                    "weight": 0,
                    "height": height,
                    "water intake": 0,
                    "bed time": 0,
                    "calories burned": 0
                }}
            
            self.updateUserLogs(log, userid)
            return
                
        self.updateData(data)
        
        
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
                                    'data' : {
                                        date_today : {
                                            'weight' : 0,
                                            'height' : 0,
                                            'water intake' : 0,
                                            'water intake goal' : 0,
                                            'bed time' : 0,
                                            'calories burned' : 0
                            }}}}
        return user
    
    def addUser(self, username, password):
        user = self.generateUser(username, password)
        data = self.getData()
        data.update(user)
        self.updateData(data)
    
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
            
        
       
        