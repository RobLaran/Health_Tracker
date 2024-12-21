from abc import ABC, abstractmethod
from datetime import date

class FeatureInterface(ABC):
    @property
    def currentDate(self):
        return  date.today().isoformat()
    
    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def viewLogs(self):
        pass