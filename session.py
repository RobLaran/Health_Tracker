import os
import socket
from datetime import date as dt
import json
from encrypt import EncryptPassword

class SessionManager:
    def __init__(self, database):
        self.users = None
        self.user = None
        self.userID = None
        self.active = False
        self.database = database
        self.encrypt = EncryptPassword()
    
    def login(self):
        print('''--------------------------''')
        print('Login User:')
        username = input('Enter username: ').strip()
        password = input('Enter password: ').strip()
        
        if self.users and username in self.users and self.encrypt.verify(self.users[username], password):
            print('logged in')
            self.user = username
            self.userID = self.database.getUserID(username)
            self.active = True
            self.saveSession(username=username)
            return True
        else:
            print('incorrect username or password')
            return False
            
    def logout(self):
        if self.active:
            self.deleteSession()
            self.user = None
            self.active = False
    
    def saveSession(self, username):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        
        date_today = dt.today().isoformat()
        
        with open('session.json', 'w') as file:
            data = {
                'username' : username,
                'ip address' : ip,
                'last logged in' : date_today,
                'id' : self.userID
            }
            
            json.dump(data, file, indent=4)
            file.close()
    
    def deleteSession(self):
        if os.path.exists('session.json'):
            os.remove('session.json')
    
    def loadSession(self):
        if os.path.exists('session.json'):
            with open('session.json', 'r') as file:
                username = json.load(file)['username']
                
                if username:
                    self.user = username
                    self.active = True
                    self.userID = self.database.getUserID(username)
                    
                file.close()
    
    def loadUsers(self):
        self.users = self.database.getUsers()