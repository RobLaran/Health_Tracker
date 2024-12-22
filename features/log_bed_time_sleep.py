from . import FeatureInterface

class LogBedTimeSleep(FeatureInterface):
    def __init__(self, database):
        self.database = database
        pass

    def log(self, userid):
        return super().log()

    def viewLogs(self, userid):
        return super().viewLogs()