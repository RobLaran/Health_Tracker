from database import Database
from session import SessionManager
from features import LogBodyMeasurement
from features import LogWaterIntake
from encrypt import EncryptPassword

class CLI:
    def __init__(self):
        self.database = Database()
        self.session = SessionManager(self.database)
        self.session.loadUsers()
        self.session.loadSession()
        self.logbodymeasurement = LogBodyMeasurement(self.database)
        self.logwaterintake = LogWaterIntake(self.database, self.session.userID)
        self.encrypt = EncryptPassword()
    
    def run(self):
        if self.session.active:
            self.mainMenu(self.session.user)
        else:
            self.userAuth()

    def userAuth(self):
       while True:
            print('''--------------------------''')
            print('User Authentication:')
            print('''--------------------------
    1) Log in
    2) Register
    3) Exit''')
            
            response = int(input('Select input: '))
            
            match response:
                case 1:
                    if self.loginUser():
                        self.mainMenu(self.session.user)
                    pass
                case 2:
                    self.registerUser()
                    pass
                case 3:
                    print("exiting...")
                    exit()
                
    def loginUser(self):
        return self.session.login()
    
    def registerUser(self):
       while True:
            print('''--------------------------''')
            print('Register User:')
            username = str(input('Enter username: '))
            password = str(input('Enter password: '))
            rePassword = str(input('Enter confirm password: '))
            encryptedPassword = self.encrypt.securePassword(password)
            
            if self.session.users and username and password:
                if not username in self.session.users and password == rePassword:
                    print('successfully registered')
                    
                    self.database.addUser(username, encryptedPassword)
                    self.database.refresh()
                    self.session.loadUsers()
                    return
                else:
                    print('unsuccessfully registered')
                    return
            elif username and password and password == rePassword:
                print('successfully registered')
                
                self.database.addUser(username, encryptedPassword)
                self.database.refresh()
                self.session.loadUsers(self.database.getUsers())
                return
            else:
                print('unsuccessfully registered')
                return
                
    def mainMenu(self, username):
        while True:
            print('''--------------------------''')
            print(f'Hi {username}')
            print('Welcome to Health Tracker:')
            print('''--------------------------
    1) Log body measurement
    2) Log water intake
    3) Log bed time sleep
    4) Log exercise routine
    5) Logout
    6) Exit''')
            try:
                response = int(input('Select input: '))
                
                match response:
                    case 1:
                        self.logBodyMeasurement()
                    case 2:
                        self.logWaterIntake()
                    case 3:
                        self.logBedTime()
                    case 4:
                        self.logExerciseRoutine()
                    case 5:
                        self.session.logout()
                        self.run()
                        print('logging out...')
                        return
                    case 6:
                        print("exiting...")
                        exit()
            except ValueError:
                print('please enter the right input')
    
    def logBodyMeasurement(self):
        while True:
            print('''--------------------------''')
            print('Log body measurement:')
            print('''--------------------------
    1) Add data
    2) View log
    3) Back''')
            response = int(input("Select input: "))
            
            match response:
                case 1:
                    date = input("Enter date(yyyy-mm-dd): ")
                    weight = int(input('Enter weight(in kg): '))
                    height = int(input('Enter height(in cm): '))
                    self.logbodymeasurement.log(self.session.userID, date, weight, height)
                case 2:
                    self.logbodymeasurement.viewLogs(self.session.userID)
                case 3:
                    return
    
    def logWaterIntake(self):
        while True:
            print('''--------------------------''')
            print('Log water intake:')
            print('''--------------------------
        1) Add data
        2) View log
        3) Set goal
        4) Back''')
            response = int(input("Select input: "))
                
            match response:
                case 1:
                    date = input("Enter date(yyyy-mm-dd): ")
                    waterml = int(input('Enter water intake(in ml): '))
                
                    self.logwaterintake.log(date, waterml)
                case 2:
                    self.logwaterintake.viewLogs()
                case 3:
                    if not self.logwaterintake.hasGoal:
                        setGoal = input('Set goal? (y/n): ')
                        
                        if setGoal == 'y':
                            self.logwaterintake.hasGoal = True
                            goal = int(input('Enter goal: '))
                            self.logwaterintake.setGoal(goal)
                            print('New goal added')
                    else:
                        goal = int(input('Edit goal(enter new goal): '))
                        
                        if goal == 0:
                            self.logwaterintake.hasGoal = False
                            self.logwaterintake.setGoal(goal)
                            print('Goal cleared')
                        else:
                            self.logwaterintake.setGoal(goal)
                            print('New goal added')
                        pass
                    
                case 4:
                    return
    
    def logBedTime(self):
        print('''--------------------------''')
        print('Log bed time:')
        print('''--------------------------
    1) Add data
    2) View log
    3) Exit''')
        pass
    
    def logExerciseRoutine(self):
        print('''--------------------------''')
        print('Log exercise routine:')
        print('''--------------------------
    1) Add data
    2) View log
    3) Exit''')
        pass
    
    