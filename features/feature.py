from abc import ABC, abstractmethod

class FeatureInterface(ABC):
    
    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def viewLogs(self):
        pass